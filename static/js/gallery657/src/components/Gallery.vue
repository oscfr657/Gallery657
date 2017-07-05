<template>
  <div >
    <div id="collection_list">
    <ul >
      <li v-for="collection in collections" >
        <router-link class="galleries" :to="{ name: 'collection', params: { collection:collection.pk } }">{{ collection.title| capitalize }}</router-link>
      </li>
    </ul>
    </div>
    <div id="collection_view">
    <router-view></router-view>
    </div>
  </div>
</template>

<script>

export default {
  name: 'gallery',
  data () {
    return {
      collections: [
        { title: 'paintings', pk: 1 },
      ]
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
