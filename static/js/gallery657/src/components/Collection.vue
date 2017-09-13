
<template>
<div id="collection_view">

<div v-for="art in collection" class="art_item">
<img :src="art.media_file" :alt="art.title"/>
</div>

</div>
</template>


<script>

export default {
  name: 'collection',
  data: function () {
    return {
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
      if (this.$route.params.collection) {
        this.collection = this.$route.params.collection
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