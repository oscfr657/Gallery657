
<script>
import Collection from './Collection.vue'
import Gallery from './Gallery.vue'

export default {
  routes: [
    { path: '/',
      component: Gallery,
        children: [
          {
            path: '/:number/',
            name: 'collection',
            component: Collection
          }
        ]
    },
  ]
}
</script>
