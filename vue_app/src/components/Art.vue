<template>
    <div class="art-backdrop" >
      <div class="art-left" @click="prevArt">
        &lt;
      </div>
      <div class="art-close" @click="close">×</div>
      <div class="art-right" @click="nextArt">
        &gt;
      </div>
      <transition name="art-fade">
        <div v-if="art!==null">
          <div class="art">
            <img v-if="art.media_file!==null" :src="art.media_file" :alt="art.title"/>
          </div>
        </div>
      </transition>
    </div>
</template>


<script>
export default {
  name: "art",
  props: ["artpk", "index"],
  data() {
    return {
      loading_art: false,
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
          }
        );
      }
    }
  }
};
</script>
