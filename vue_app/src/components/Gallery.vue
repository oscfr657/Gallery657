<template>
  <div >
    <div class="collection_list" v-if="collections">
      <ul>
        <li v-for="collection in collections" :key="collection.pk">
          <router-link :to="{ name: 'collection', params: { number:collection.pk } }">
            {{ collection.title| capitalize }}
          </router-link>
        </li>
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
      collections: false
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$http.get("/gallery/api/collection/").then(
        response => {
          if (response.status == '200' ) {
            this.collections = response.body;
          }
        },
        response => {
          console.log("API error");
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
