
<script>
import Collection from "./Collection.vue";
import Gallery from "./Gallery.vue";

export default {
  routes: [
    {
      path: "/",
      name: "collection_root",
      component: Gallery,
      children: [
        {
          path: "/:slug/",
          name: "collection_slug",
          component: Collection
        }, {
          path: "/:number/",
          name: "collection_number",
          component: Collection
        }, {
          path: '/',
          name: "all_art",
          component: Collection
        }
      ]
    }
  ]
};
</script>
