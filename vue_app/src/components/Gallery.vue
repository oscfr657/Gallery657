<template>
  <div >
    <div v-if="loading" class="collection_list" >
    Loading...
    </div>
    <div v-if="error" class="collection_list" >
      {{ error }}
    </div>
    <div class="collection_list" v-if="collections">
      <ul>
        <router-link v-for="collection in collections" tag="li" :key="collection.pk" :to="{ name: 'collection', params: { number:collection.pk } }">
          <button >{{ collection.title| capitalize }}</button>
        </router-link>
      <ul>
    </div>
    <div >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "gallery657",
  data() {
    return {
      loading: false,
      error: false,
      collections: false
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.loading = true;
      this.$http.get("/gallery/api/collection/").then(
        response => {
          if (response.status == '200' ) {
            this.collections = response.body;
            this.loading = false;
          }
        },
        response => {
          console.log("API error");
          this.error = true;
          this.loading = false;
        }
      );
    }
  },
  filters: {
    capitalize(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    }
  }
};
</script>
