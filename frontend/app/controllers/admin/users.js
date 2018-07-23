import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    findUser() {
      let email = this.get('userEmail');
      this.transitionToRoute('admin.users.list', email);
    }
  }
});
