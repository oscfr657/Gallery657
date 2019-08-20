<template>
    <div class="collections_wrap">
      <div class="collections" v-if="collections">
        <router-link :to="{ name: 'all_art'}" class="collections_button" >Collections</router-link>
        <div class="collection_list">
            <router-link 
                v-for="collection in collections" :key="collection.pk" 
                :to="{ name: 'collection', params: { number:collection.pk } }">
              {{ collection.title| capitalize }}
            </router-link>
        </div>
      </div>
      <router-view></router-view>
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
      this.$http.get("/gallery657/api/collection/").then(
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
