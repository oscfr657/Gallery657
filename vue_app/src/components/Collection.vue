
<template>
  <div >
    <div v-if="loading" class="collection_view">
    Loading...
    </div>
    <div v-else-if="error" class="collection_view">
      {{ error }}
    </div>
    <div class="collection_view">
      <div v-for="art in collection" :key="art.pk" class="art_item">
        <img @click="showArt(art.pk)" v-if="art.thumb_nail!==null" :src="art.thumb_nail" :alt="art.title"/>
        <img @click="showArt(art.pk)" v-else-if="art.media_file!==null" :src="art.media_file" :alt="art.title"/>
      </div>
    </div>

    <art
      v-show="isArt"
      @close="closeArt"
      :artpk="artpk"
    />
  </div>
</template>

<script>
import art from "./Art.vue";
export default {
  name: "collection",
  components: {
    art
  },
  data() {
    return {
      loading: true,
      error: false,
      collection: [],
      isArt: false,
      artpk: 0
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    $route: "fetchData"
  },
  methods: {
    showArt(art_pk) {
      this.artpk = art_pk;
      this.isArt = true;
    },
    closeArt() {
      this.isArt = false;
    },
    fetchData() {
      this.error = false;
      this.loading = true;
      if (this.$route.params.number) {
        this.$http
          .get("/gallery/api/art/?collection=" + this.$route.params.number)
          .then(
            response => {
              this.loading = false;
              this.collection = response.body;
            },
            response => {
              console.log("Collection not found error");
              console.log(response);
              this.error = response.status +": Collection not found.";
              this.loading = false;
            }
          );
      }
    }
  }
};
</script>