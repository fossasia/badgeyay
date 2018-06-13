'use strict';

const functions = require('firebase-functions');
const admin = require('firebase-admin');
const firebase = require('firebase');
var serviceAccount = require('./config/serviceKey.json');
var clientAccount = require('./config/clientKey.json');

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
const PASSWORD_RESET_LINK = 'http://badgeyay.com/reset/password?token='

exports.sendVerificationMail = functions.auth.user().onCreate((user) => {
  const uid = user.uid;
  if (user.emailVerified) {
    console.log('User has email already verified: ', user.email);
    return 0;
  } else {
    return admin.auth().createCustomToken(uid)
      .then((customToken) => {
        return firebase.auth().signInWithCustomToken(customToken)
      })
      .then((curUser) => {
        return firebase.auth().onAuthStateChanged((user_) => {
          if (!user.emailVerified) {
            user_.sendEmailVerification();
            return console.log('Verification mail sent: ', user_.email);
          } else {
            return console.log('Email is already verified: ', user_.email);
          }
        })
      })
      .catch((err) => {
        console.error(err.message);
      })
  }
});

exports.greetingMail = functions.auth.user().onCreate((user) => {
  const email = user.email;
  const displayName = user.displayName;

  return sendGreetingMail(email, displayName);
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
  });
}

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
