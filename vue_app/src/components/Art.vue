<template>
  <transition name="art-fade">
    <div class="art-backdrop" @click="close">
      <div class="art" v-if="loading_art" >
      Loading...
      </div>
      <div class="art" v-if="art_error" >
        {{ art_error }}
      </div>
      <div class="art" v-if="art!==null" >
        <img v-if="art.media_file!==null" :src="art.media_file" :alt="art.title"/>
      </div>
    </div>
  </transition>
</template>


<script>
export default {
  name: "art",
  props: ["artpk"],
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
