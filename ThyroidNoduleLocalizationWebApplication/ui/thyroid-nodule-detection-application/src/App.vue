<template>
<!--<img src="./assets/logo.png">-->
  <main-page class="roboto-font-regular"></main-page>
</template>

<script>
import MainPage from "./components/MainPage.vue";

export default {
  name: 'App',
  components: {
    MainPage
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

