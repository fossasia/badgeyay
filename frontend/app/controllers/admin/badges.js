import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    findBadges() {
      var userTerm = this.get('user');
      this.transitionToRoute('admin.badges.list', userTerm);
    }
  }
});
