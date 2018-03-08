<template>
  <div >
    <div v-if="loading" >
    Loading...
    </div>
    <div v-if="error" >
      {{ error }}
    </div>
    <div id="collection_list">
      <router-link v-for="collection in collections" :to="{ name: 'collection', params: { collection:collection.pk } }">
      <br>
      <button>{{ collection.title| capitalize }}</button><br></router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'gallery',
  data: function () {
    return {
      loading: false,
      error: null,
      collections: [
        { title: 'Loading', pk: 0 },
      ]
      }
  },
  created: function () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
      this.error = this.collections = null
      this.loading = true
      this.$http.get('/gallery/api/collection/').then(response => {
        this.collections = response.body.results;
        }, response => {
          console.log('error');
        });
    }
  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
}

</script>
