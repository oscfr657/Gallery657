
<template>
  <div >
    <div v-if="loading" >
    Loading...
    </div>
    <div v-if="error" >
      {{ error }}
    </div>
    <div id="collection_view">

    <div v-for="art in collection" class="art_item">
    <img :src="art.media_file" :alt="art.title"/>
    </div>

    </div>
  </div>
</template>


<script>

export default {
  name: 'collection',
  data: function () {
    return {
      loading: false,
      error: null,
      collection: [],
    }
  },
  created: function () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData: function () {
      this.error = this.collection = null
      this.loading = true
      if (this.$route.params.collection) {
        this.collection = this.$route.params.collection
        this.$http.get('/gallery/api/art/?collection='+this.collection).then(response => {
          this.collection = response.body.results;
          }, response => {
            console.log('error');
          });
      }
    }
  }
}
</script>