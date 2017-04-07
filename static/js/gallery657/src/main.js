
import { routes } from './components/Router.vue'

console.log('test');
console.log(routes);

const router = new VueRouter({
    //mode: 'history',
    base: '/gallery',
    routes
    })

new Vue({
  el: '#gallery',
  router
});
