
<template>
    <div id="collection_view">
      <div v-for="(art, index) in collection" :key="art.pk" class="art_item">
        <img @click="showArt(art.pk, index)" v-if="art.thumb_nail!==null" :src="art.thumb_nail" :alt="art.title"/>
        <img @click="showArt(art.pk, index)" v-else-if="art.media_file!==null" :src="art.media_file" :alt="art.title"/>
      </div>
      <div class="collection_more">
        <button v-if="this.scroll_url!==null" v-on:click="more()">+</button>
      </div>
    <art
      v-show="isArt"
      @close="closeArt"
      @prevArt="prevArt"
      @nextArt="nextArt"
      :artpk="artpk"
      :index="index"
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
      collection: [],
      isArt: false,
      artpk: 0,
      index: 1,
      scroll_url: false
    };
  },
  beforeMount() {
    this.fetchData();
  },
  watch: {
    $route: "fetchData"
  },
  methods: {
    showArt(art_pk, index) {
      this.isArt = true;
      this.artpk = art_pk;
      this.index = index;
    },
    prevArt() {
      if (this.index > 0 ) {
        this.index = this.index - 1;
      } else {
        this.index = this.collection.length - 1;
      }
      this.artpk = this.collection[this.index].pk
    },
    nextArt() {
      if (this.index < this.collection.length - 1 ) {
        this.index = this.index + 1;
      } else {
        this.index = 0;
      }
      this.artpk = this.collection[this.index].pk
    },
    closeArt() {
      this.isArt = false;
    },
    fetchData() {
      this.loading = true;
      if (this.$route.params.number) {
        this.$http
          .get("/gallery/api/art/?collection=" + this.$route.params.number)
          .then(
            response => {
              this.loading = false;
              this.collection = response.body.results;
              this.scroll_url = response.body.next;
            },
            response => {
              console.log("Collection not found error");
              console.log(response);
              this.loading = false;
            }
          );
      } else {
        this.$http
          .get("/gallery/api/art/")
          .then(
            response => {
              this.loading = false;
              this.collection = response.body.results;
              this.scroll_url = response.body.next;
            },
            response => {
              console.log("No art found error");
              console.log(response);
              this.loading = false;
            }
          );
      }
    },
    scroll() {
      let gallery657 = document.getElementById('gallery657');
      let collections_wrap = gallery657.firstChild;
      collections_wrap.onscroll = function() {
        console.log('collections_wrap 234');
      };
      let collection_view = document.getElementById('collection_view');
      collection_view.onscroll = function() {
        console.log('collection_view 234');
      };
    },

    more() {
      this.$http.get(this.scroll_url).then(
        response => {
          response.body.results.forEach(element => {
            this.collection.push(element);
          });
          this.scroll_url = response.body.next;
          this.loading = false;
        },
        response => {
          console.log("No art found error");
          console.log(response);
          this.loading = false;
        }
      );
    }
  },
  mounted() {
    this.scroll();
  }
};
</script>