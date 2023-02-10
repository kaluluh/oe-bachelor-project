<template>
<!--<img src="./assets/logo.png">-->
  <nav-bar class="roboto-font-regular"></nav-bar>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, "Arial Black", sans-serif;
}
@font-face {
  font-family: 'roboto-serif-regular';
  src: url('~@/assets/fonts/RobotoSerif-Regular.ttf');
}
@font-face {
  font-family: 'roboto-serif-medium';
  src: url('~@/assets/fonts/RobotoSerif-Medium.ttf');
}
.roboto-font-regular {
  font-family: roboto-serif-regular;
}
</style>

