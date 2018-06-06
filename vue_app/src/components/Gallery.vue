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
    <div v-if="collections" >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "gallery",
  data() {
    return {
      loading: false,
      error: null,
      collections: false
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    $route: "fetchData"
  },
  methods: {
    fetchData() {
      this.loading = true;
      this.$http.get("/gallery/api/collection/").then(
        response => {
          this.loading = false;
          this.collections = response.body;
        },
        response => {
          console.log("error");
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
