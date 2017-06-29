<template>
  <div id="list">
  <router-link class=galleries to="/art">Paintings</router-link>
  <router-view></router-view>
  </div>
  <div >
  <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'gallery',
  data () {
    return {
      msg: 'Welcome to my galleries'
    }
  }
}
</script>
