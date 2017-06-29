
<script>
import Art from './Art.vue'
import App from './App.vue'

export default {
  routes: [
    { path: '/', component: App },
    { path: '/:id', name: 'art_id', component: Art }
  ]
}
</script>
