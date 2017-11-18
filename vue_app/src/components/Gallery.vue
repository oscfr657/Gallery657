<template>
  <div >
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
      collections: [
        { title: 'paintings', pk: 1 },
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
