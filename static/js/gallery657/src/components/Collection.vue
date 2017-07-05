
<template>
<div class="collection">

<div v-for="art in collection" class="art_item">
<img :src="art.media_file" :alt="art.title"/>
</div>

</div>
</template>


<script>

export default {
  name: 'collection',
  data () {
    return {
      collection: [],
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
      if (this.$route.params.collection) {
        this.collection = this.$route.params.collection
        console.log(this.collection);
        this.$http.get('/gallery/api/media_file/?collection='+this.collection).then(response => {
          this.collection = response.body.results;
          }, response => {
            console.log('error');
          });
      }
    }
  }
}
</script>