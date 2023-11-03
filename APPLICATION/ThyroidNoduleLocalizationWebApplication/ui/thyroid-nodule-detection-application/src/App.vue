<template>
  <nav-bar></nav-bar>
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

@font-face {
  font-family: 'roboto-serif-regular';
  src: url('~@/assets/fonts/RobotoSerif-Regular.ttf');
}
@font-face {
  font-family: 'roboto-serif-medium';
  src: url('~@/assets/fonts/RobotoSerif-Medium.ttf');
}
.main-btn-style{
  width:95px;
  height: 45px;
  background-color: #01BC8E;
  border-radius: 8px;
  color: white;
  cursor: pointer;
  display: inline-block;
  margin-bottom: 0;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  background-image: none;
  border: 1px solid transparent;
  padding: 6px 12px;
  font-size: 16px;
  user-select: none;
  box-shadow: 2px 2px 2px darkgrey;
  text-align: center;
  font-family: roboto-serif-medium;
}

.main-btn-style:hover {
  box-shadow: 3px 3px 3px darkgrey;
}
</style>

