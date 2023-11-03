<template>
  <div id="nav-bar">
  <nav class="navbar navbar-expand-lg navbar-light" style="background: #F2F2F1">
    <a class="navbar-brand" style="margin-left: 4%;font-size: 40px"></a>
    <div class="collapse navbar-collapse justify-content-lg-end" style="margin-left: 150mm">
      <div class="navbar-nav" style="width: 80%;font-size: 18px;">
<!--        <a class="col-2 black-font-color nav-item nav-link text-center">-->
<!--          <router-link to="/">-->
<!--          Home-->
<!--          </router-link>-->
<!--        </a>-->
        <a class="col-2 black-font-color nav-item nav-link text-center">
          <router-link :to="{name:'Statistics'}">
            Statistics
          </router-link>
        </a>
        <a class="col-2 black-font-color nav-item nav-link text-center">
          <router-link :to="{name:'Analysis'}">
          Analysis
          </router-link>
        </a>
<!--        <a class="col-2 black-font-color nav-item nav-link text-center">-->
<!--          <router-link :to="{name:'Database'}">-->
<!--          Database-->
<!--          </router-link>-->
<!--        </a>-->
        <button type="button" class="col-2 main-btn-style" style="margin-left: 40px;" href="#">Login</button>
      </div>
    </div>
  </nav>
  </div>
  <router-view/>
</template>

<script>
export default {

};
</script>

<style scoped>
#nav-bar{
  font-family: roboto-serif-regular,serif;
}
.nav-link:hover {
  border: 2px solid #01BC8E;
  border-radius: 5px;
}
.nav-link:focus {
  border: 2px solid #01BC8E;
  border-radius: 5px;
}

.nav-link:active {
  border: 2px solid #01BC8E;
  border-radius: 5px;
}

.black-font-color{
  color: black;
}
#nav-bar a.router-link-exact-active{
  /*color: #01BC8E;*/
  font-family: roboto-serif-medium,serif;
  text-shadow: 2px 2px 2px whitesmoke;
  font-weight: bold;
}
#nav-bar a {
  color: black;
  font-family: roboto-serif-regular,serif;
  text-decoration: none;
}
</style>
