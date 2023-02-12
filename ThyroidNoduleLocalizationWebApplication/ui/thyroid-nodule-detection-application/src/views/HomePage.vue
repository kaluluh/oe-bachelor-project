<template>
  <div id="home" class="container-fluid custom-class">
    <div class="row">
      <div class="col-md-6" style="; min-height:100px;">
        <div style="width: 100%;margin-top: 20%">
          <div style="text-align: right">
            <a style="color: #01BC8E;font-size: 40px;text-align: left">Fight against thyroid cancer</a>
            <p style="font-size: 19px;">Lorem ipsum dolor sit amet consectetur. Consectetur dui convallis accumsan congue urna urna. Turpis morbi nec sit quis eu porttitor mauris nisl sed. Leo velit ac et enim ut gravida dui nulla morbi. Iaculis mauris orci in egestas duis tempor tortor.</p>
            <div style="text-align: left;margin-left: 14%">
              <button class="main-btn-style" style="text-align: center;width:250px;" type="button">
                <router-link to="/analysis">
                Make analysis by AI
                </router-link>
              </button>
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
  name: "HomePage",
  data() {
    return {
      backgroundImage: require('../assets/images/mainpagebgpic.jpeg')
    }
  }
};
</script>

<style scoped>
#home a{
  color: white;
  text-decoration: none;
  font-family: roboto-serif-medium,serif;
}
#home p{
  font-family: roboto-serif-regular,serif;
}
</style>