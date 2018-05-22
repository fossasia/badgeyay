import Route from '@ember/routing/route';

export default Route.extend({
  beforeModel() {
    return this.get('session').fetch().catch(function() {});
  },
  model() {
    const userObj = this.get('session.currentUser');
    if (userObj !== undefined) {
      const uid = this.get('session.uid');
      this.get('store').pushPayload({
        data: [{
          id         : uid,
          type       : 'user',
          attributes : {
            'name'     : userObj.displayName,
            'email'    : userObj.email,
            'photoUrl' : userObj.photoURL
          },
          relationships: {}
        }]
      });
    }
  }
});
