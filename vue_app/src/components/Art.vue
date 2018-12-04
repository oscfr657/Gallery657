<template>
  <transition name="art-fade">
    <div class="art-backdrop" >
      <div class="art-close"  @click="close">
        X
      </div>
      <div class="art" v-if="art_error" >
        {{ art_error }}
      </div>
      <div v-else-if="art!==null">
        <div class="art-left" @click="prevArt">
          &lt;
        </div>
        <div class="art-right" @click="nextArt">
          &gt;
        </div>
        <div class="art">
          <img v-if="art.media_file!==null" :src="art.media_file" :alt="art.title"/>
        </div>
      </div>
    </div>
  </transition>
</template>


<script>
export default {
  name: "art",
  props: ["artpk", "index"],
  data() {
    return {
      loading_art: false,
      art_error: false,
      art: null
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    artpk: "fetchData"
  },
  methods: {
    close() {
      this.$emit("close");
    },
    prevArt() {
      this.$emit("prevArt");
    },
    nextArt() {
      this.$emit("nextArt");
    },
    fetchData() {
      this.art_error = false;
      this.loading_art = true;
      this.art = null;
      if (this.artpk) {
        this.$http.get("/gallery/api/art/" + this.artpk).then(
          response => {
            this.loading_art = false;
            this.art = response.body;
          },
          response => {
            console.log("Art error");
            this.art_error = true;
          }
        );
      }
    }
  }
};
</script>
