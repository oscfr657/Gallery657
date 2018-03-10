<template>
  <div >
    <div v-if="loading" >
    Loading...
    </div>
    <div v-if="error" >
      {{ error }}
    </div>
    <div id="collection_list" v-if="collections">
      <router-link v-for="collection in collections" :to="{ name: 'collection', params: { number:collection.pk } }">
      <br>
      <button>{{ collection.title| capitalize }}</button><br></router-link>
    </div>
    <div v-if="collections" >
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

export default {
  name: 'gallery',
  data () {
    return {
      loading: false,
      error: null,
      collections: false
      }
  },
  created () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.error = null
      this.collections = false
      this.loading = true
      this.$http.get('/gallery/api/collection/').then(response => {
        this.loading = false
        this.collections = response.body.results;
        }, response => {
          console.log('error')
        });
    }
  },
  filters: {
    capitalize (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
}

</script>
