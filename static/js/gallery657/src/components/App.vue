<template>
  <div>
  <h2>{{ msg }}</h2>
  <router-link class=galleries to="/art">Art</router-link>
  <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to my galleries'
    }
  }
}
</script>
