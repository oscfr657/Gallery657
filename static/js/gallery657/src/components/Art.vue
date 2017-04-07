
<template>
<div>
<router-link :to="{ name: 'art_id', params: { id:prev}}" v-if="prev">Prev</router-link>
<span class=toinfinity v-else>Prev</span>

<router-link :to="{ name: 'art_id', params: { id:next}}" v-if="next">Next</router-link>
<span class=toinfinity v-else>Next</span>

<h2>{{ art.title }}</h2>

<img v-if="art" :src="art.media_file" :alt="art.title"/>
</div>
</template>


<script>

export default {
  name: 'art',
  data () {
    return {
      prev: null,
      art: null,
      next: null
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
      this.art = null
      var image_id = 1;
      if (this.$route.params.id) {
        image_id = this.$route.params.id;
      }
      this.$http.get('/gallery/api/mediafiles/').then(response => {
        var count = response.body.count
        this.art = response.body.results[image_id-1];
        if (this.art.pk > 1) {
            this.prev = this.art.pk - 1;
        } else {
            this.prev = false;
        }
        if (this.art.pk < count) {
            this.next = this.art.pk + 1;
        } else {
            this.next = false;
        }
        }, response => {
          console.log('error');
        });
    }
  }
}
</script>