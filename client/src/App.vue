<template>
  <div id="app">
    <Header></Header>
    <router-view class="container-sm py-5 mt-5 rounded shadow" id="page-body"/>
  </div>
</template>

<script>
  import Header from './components/Header'

  export default {
    name: 'App',
    components: {Header}
  }
</script>

<style>
  #page-body {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background-color: rgba(255, 255, 255, 0.85);
  }

  body, html {
    height: 100%;
  }

  #app {
    background-image: url("assets/background/music-player-2951399_1920.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100%;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  }
</style>
