import Route from '@ember/routing/route';

export default Route.extend({
  redirect: ()=>{
    var url = this.router.location.formatURL('/not-found');
    if (window.location.pathname !== url) {
      this.transitionTo('/not-found');
    }
  }
});
