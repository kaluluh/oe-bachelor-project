<template id="main-page">
  <nav class="navbar navbar-expand-lg navbar-light" style="background: #F2F2F1">
    <a class="navbar-brand" href="#" style="margin-left: 4%;font-size: 40px">Kurva anyad</a>
    <div class="collapse navbar-collapse justify-content-end">
      <div class="navbar-nav" style="width: 80%;font-size: 20px;">
        <a class="col-2 black-font-color nav-item nav-link text-center" href="#">Statistics</a>
        <a class="col-2 black-font-color nav-item nav-link text-center" href="#">Analysis</a>
        <a class="col-2 black-font-color nav-item nav-link text-center" href="#">Database</a>
        <button type="button" class="col-2 main-btn-style" style="margin-left: 40px;" href="#">Login</button>
      </div>
    </div>
  </nav>

  <div class="container-fluid custom-class">
    <div class="row">
      <div class="col-md-6" style="; min-height:100px;">
      <div style="width: 100%;margin-top: 20%">
        <div style="text-align: right">
          <a style="color: #01BC8E;font-size: 40px;font-family: roboto-serif-medium;text-align: left">Fight against thyroid cancer</a>
          <p style="font-size: 19px;">Lorem ipsum dolor sit amet consectetur. Consectetur dui convallis accumsan congue urna urna. Turpis morbi nec sit quis eu porttitor mauris nisl sed. Leo velit ac et enim ut gravida dui nulla morbi. Iaculis mauris orci in egestas duis tempor tortor.</p>
            <div style="text-align: left;margin-left: 14%">
              <button class="main-btn-style" style="text-align: center;width:250px;" type="button">Make analysis by AI</button>
            </div>
        </div>
      </div>
      </div>
      <div class="col-md-6" style="min-height:100px;display: flex;">
        <img class="img-fluid" :src=backgroundImage>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      backgroundImage: require('../assets/images/mainpagebgpic.jpeg')
    }
  }
};
</script>

<style>
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
  /*border: 1px solid lightgrey;*/
  box-shadow: 3px 3px 3px darkgrey;
}
.nav-link:hover {
  border: 2px solid #01BC8E;
  border-radius: 5px;
}
.black-font-color{
  color: black;
}
</style>
