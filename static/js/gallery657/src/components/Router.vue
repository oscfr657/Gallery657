
<script>
import Art from './Art.vue'

export default {
  routes: [
    { path: '/', component: Art },
    { path: '/:id', name: 'art_id', component: Art }
  ]
}
</script>
