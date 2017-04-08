
<script>
import App from './App.vue'
import Art from './Art.vue'

export default {
  routes: [
    { path: '/', component: App,
      children: [
        { path: 'art', component: Art },
        { path: 'art/:id', name: 'art_id', component: Art }
      ]
    },
  ]
}
</script>
