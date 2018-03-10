
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
  data () {
    return {
      loading: false,
      error: null,
      collection: [],
      number: 0
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
      this.loading = true
      if (this.$route.params.number) {
        this.number = this.$route.params.number
        this.$http.get('/gallery/api/art/?collection='+this.number).then(response => {
          this.loading = false
          this.collection = response.body
          }, response => {
            console.log('Collection error');
          });
      }
    }
  }
}
</script>