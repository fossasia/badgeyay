'use strict';

const functions = require('firebase-functions');
const admin = require('firebase-admin');
const firebase = require('firebase');
const crypto = require('crypto');
var serviceAccount = require('./config/serviceKey.json');
var clientAccount = require('./config/clientKey.json');
const fs = require('fs');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: clientAccount.databaseURL
});

firebase.initializeApp(clientAccount);

const nodemailer = require('nodemailer');

const gmailEmail = functions.config().gmail.email;
const gmailPassword = functions.config().gmail.password;
const mailTransport = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: gmailEmail,
    pass: gmailPassword
  }
});

const APP_NAME = 'Badgeyay';
const BASE_URL = 'http://badgeyay.com/';
const PASSWORD_RESET_LINK = 'http://badgeyay.com/#/reset/password?token=';
var password = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';


var encrypt = function (input, password, callback) {
  var m = crypto.createHash('md5');
  m.update(password)
  var key = m.digest('hex');

  m = crypto.createHash('md5');
  m.update(password + key)
  var iv = m.digest('hex');

  var data = new Buffer(input, 'utf8').toString('binary');

  var cipher = crypto.createCipheriv('aes-256-cbc', key, iv.slice(0, 16));

  // UPDATE: crypto changed in v0.10
  // https://github.com/joyent/node/wiki/Api-changes-between-v0.8-and-v0.10
  var nodev = process.version.match(/^v(\d+)\.(\d+)/);
  var encrypted;

  if (nodev[1] === '0' && parseInt(nodev[2]) < 10) {
    encrypted = cipher.update(data, 'binary') + cipher.final('binary');
  } else {
    encrypted = cipher.update(data, 'utf8', 'binary') + cipher.final('binary');
  }

  var encoded = new Buffer(encrypted, 'binary').toString('base64');

  callback(encoded);
};

var decrypt = function (input, password, callback) {
  // Convert urlsafe base64 to normal base64
  input = input.replace(/-/g, '+').replace(/_/g, '/');
  // Convert from base64 to binary string
  var edata = new Buffer(input, 'base64').toString('binary')

  // Create key from password
  var m = crypto.createHash('md5');
  m.update(password)
  var key = m.digest('hex');

  // Create iv from password and key
  m = crypto.createHash('md5');
  m.update(password + key)
  var iv = m.digest('hex');

  // Decipher encrypted data
  var decipher = crypto.createDecipheriv('aes-256-cbc', key, iv.slice(0, 16));

  // UPDATE: crypto changed in v0.10
  // https://github.com/joyent/node/wiki/Api-changes-between-v0.8-and-v0.10
  var nodev = process.version.match(/^v(\d+)\.(\d+)/);
  var decrypted, plaintext;

  if (nodev[1] === '0' && parseInt(nodev[2]) < 10) {
    decrypted = decipher.update(edata, 'binary') + decipher.final('binary');
    plaintext = new Buffer(decrypted, 'binary').toString('utf8');
  } else {
    plaintext = (decipher.update(edata, 'binary', 'utf8') + decipher.final('utf8'));
  }

  callback(plaintext);
};


String.prototype.format = function () {
  var formatted = this;
  for (var prop in arguments[0]) {
    var regexp = new RegExp('\\{' + prop + '\\}', 'gi');
    formatted = formatted.replace(regexp, arguments[0][prop]);
  }
  return formatted;
};

exports.sendVerificationMail = functions.auth.user().onCreate((user) => {
  const uid = user.uid;
  if (user.emailVerified) {
    console.log('User has email already verified: ', user.email);
    sendGreetingMail(user.email, user.displayName);
    return 0;
  } else {
    let userEmail = user.email;
    const mailOptions = {
      from: `${APP_NAME}<noreply@firebase.com>`,
      to: userEmail,
    };

    encrypt(userEmail, password, encoded => {
      var resp = {
        link: BASE_URL + '#/verify/email?id=' + encoded
      }
      mailOptions.subject = 'Please verify your Email | Badgeyay';
      mailOptions.html = '<p>Please verify your email ID by clicking on this <a href={link}>Link</a></p>'.format(resp);
      return mailTransport.sendMail(mailOptions)
        .then(() => {
          console.log('Verification Mail Sent');
          return 0;
        })
        .catch(err => {
          console.log(err);
          return -1;
        });
    });
    return 0;
  }
});

function sendGreetingMail(email, displayName) {
  const mailOptions = {
    from: `${APP_NAME}<noreply@firebase.com>`,
    to: email,
  };

  mailOptions.subject = `Welcome to Badgeyay`;
  mailOptions.text = `Hey ${displayName || ''}! Welcome to Badgeyay. We welcome you onboard and pleased to offer you service.`;
  return mailTransport.sendMail(mailOptions).then(() => {
    return console.log('Welcome mail sent to: ', email)
  }).catch((err) => {
    console.error(err.message);
    return -1;
  });
}

exports.sendWelcomeMail = functions.https.onRequest((req, res) => {
  let uid = req.query['id'];
  admin.auth().getUser(uid)
    .then(userRecord => {
      let email = userRecord.email;
      let displayName = userRecord.displayName;
      return sendGreetingMail(email, displayName);
    })
    .catch(err => {
      console.log(err);
      return -1;
    })
});

exports.sendResetMail = functions.https.onRequest((req, res) => {
  let token = req.query['token'];
  let email = req.query['email'];
  res.setHeader('Content-Type', 'application/json');
  sendResetMail(token, email)
    .then(() => {
      console.log('Reset mail sent to', email);
      res.json({ data: { attributes: { status: 200 }, id: token, type: 'reset-mails' } });
      return 0;
    })
    .catch(err => {
      console.error(err);
      res.json({ data: { attributes: { status: 500 }, id: token, type: 'reset-mails' } });
      return -1;
    });
});

function sendResetMail(token, email) {
  const mailOptions = {
    from: `${APP_NAME}<noreply@firebase.com>`,
    to: email,
  };

  mailOptions.subject = `Password reset link`;
  mailOptions.html = '<p>Hey ' + email + '! Here is your password reset <a href=\'' + PASSWORD_RESET_LINK
    + token + '\'>Link</a><p>';
  return mailTransport.sendMail(mailOptions);
}
