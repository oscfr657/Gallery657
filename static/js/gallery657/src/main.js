
import { routes } from './components/Router.vue'

const router = new VueRouter({
    //mode: 'history',
    base: '/gallery/',
    routes
    })

new Vue({
  el: '#gallery',
  router
});
