
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
      console.log('test 0')
      console.log(this)
      console.log('test 1')
      this.error = null
      this.loading = true
      console.log('collection this 0')
      console.log(this.$route)
      console.log('collection this 1')
      console.log(this.$router)
      if (this.$route.params.number) {
        console.log('collection if routes')
        this.number = this.$route.params.number
        console.log(this.number)
        console.log('collection if routes')
        this.$http.get('/gallery/api/art/?collection='+this.number).then(response => {
          this.loading = false
          this.collection = response.body.results;
          }, response => {
            console.log('Collection error');
          });
      }
    }
  }
}
</script>