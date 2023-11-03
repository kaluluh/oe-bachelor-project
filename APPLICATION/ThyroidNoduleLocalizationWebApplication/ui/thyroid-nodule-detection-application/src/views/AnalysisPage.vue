<template>

  <div id="app">
    <div class="container">
        <div class="mx-auto col-9 col-md-9 col-lg-9 form-block-style" style="margin-top: 0mm;background-color: #0D2837">
          <div class="row" style="margin-left: 5mm;">
            <div class="col-sm-5" style="margin-top: 3mm;">
              <label style="color: white">File</label>
              <input id="file-upload" class="form-control" style="background-color: #F2F2F1; border-radius: 5px;" type="file" @change="uploadFile" ref="file">
            </div>
            <div class="col-sm-2" style="margin-top: 3mm;">
              <label style="color: white">Medical doctor</label>
              <input type="text" class="form-control" >
            </div>
            <div class="col-sm-2" style="margin-top: 3mm;">
              <label style="color: white">Age</label>
              <input type="text" class="form-control" >
            </div>
            <div class="col-sm-2" style="margin-top: 8mm;">
              <button type="submit" class="search-btn-style" @click="submitFile">Load</button>
            </div>
          </div>
        </div>

        <div class="d-inline-block mx-auto col-12 col-md-8 col-lg-7 d-flex align-items-center" style="margin-top: 5mm" v-if="isDetection">
          <table class="table query-table" >
            <thead>
            <tr>
              <th scope="col">Class</th>
              <th scope="col">Score</th>
              <th scope="col">Bounding Box</th>
            </tr>
            </thead>
            <tbody v-for="res in result['predictions']" :key="res.bbox">
            <tr>
              <td v-show="res.class===2">Malignant</td>
              <td v-show="res.class===1">Benign</td>
              <td>{{res.score.toFixed(2)}}</td>
              <td>{{res.bbox[0].toFixed(2)}} {{res.bbox[1].toFixed(2)}} {{res.bbox[2].toFixed(2)}} {{res.bbox[3].toFixed(2)}}</td>
            </tr>
            </tbody>
          </table>
        </div>

        <div class="row align-items-center" style="margin-top: 5mm;margin-left: 40mm" v-if="imageUploaded">
          <div class="col-md-5" style="; min-height:100px;">
            <div>
              <label style="color: white">Original</label>
            </div>
            <div>
              <img v-if="url" :src="url" />
            </div>
          </div>
          <div class="col-md-5" style="; min-height:100px;">
            <div v-if="isDetection">
              <label style="color: white">Detected</label>
            </div>
            <div>
              <img id="ItemPreview" />
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
import axios from "axios";

export default {
  name: "AnalysisPage.vue",
  data() {
    return {
      result: [],
      url:null,
      isDetection: false,
      imageUploaded:false
    }
  },
  mounted() {
  },
  methods: {
    uploadFile(e) {
      this.Images = this.$refs.file.files[0];
      console.log(this.Images);
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
      this.imageUploaded = true;
    },
    submitFile() {
      const formData = new FormData();
      formData.append('file', this.Images);
      const headers = new Headers();
      headers.append('Content-Type','multipart/form-data');
      headers.append('Access-Control-Allow-Origin', 'http://localhost:8080');
      console.log(formData);
      axios.post('http://localhost:8000/detect', formData, { headers }).then((res) => {
        this.result = res.data;
        //the results is a base64 string.  convert it to an image and assign as 'src'
        document.getElementById("ItemPreview").src = "data:image/jpg;base64," + this.result['image'];
        this.isDetection = true;
      });
    }
  }
}
</script>

<style scoped>

.container {
  min-height: 100vh;
}

#app {
  background: #193C4D;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  padding: 100px;
}


.disabled-button-style{
  background-color:#484747;
  border-radius: 5px;
  color: white;
  opacity: 0.3;
  width: 120px;
  height: 38px;
  border:0;
}

.form-control:focus{
  box-shadow: 1px 1px 1px 1px lightgrey;
  border: 1px solid #ced4da;
}

.analysis-button-style{
  background-color: #01BC8E;
  border-radius: 5px;
  color: white;
  width: 252px;
  height: 38px;
  border:0;
}

.edit-button-style{
  margin-right: 5mm;
  background-color:#484747;
  border-radius: 5px;
  color: white;
  opacity: 0.5;
  width: 120px;
  height: 38px;
  border:0;
}

.confirm-button-style{
  background-color: #FF6A63;
  border-radius: 5px;
  color: white;
  width: 120px;
  height: 38px;
  border:0;
}

.exit-from-edit-button-style{
  background-color: #FF6A63;
  border-radius: 5px;
  color: white;
  width: 40px;
  height: 30px;
  border:0;
  margin-top: 1mm;
}

.edit-button-style:active{
  box-shadow: 2px 2px 3px 2px darkgrey;
}
.confirm-button-style:active{
  box-shadow: 2px 2px 3px 2px darkgrey;
}

.selected-table-style{
  background: #EEEEEE;
  border-radius: 5px;
  box-shadow: 2px 2px 2px 2px darkgrey;
  border: darkgrey;
}
.query-table{
  background: #E7E4E4;
  border-radius: 5px;
}
.query-table td{
  font-family: roboto-serif-regular;
  align-content: center;
  text-align: center;
  vertical-align: middle;
  font-size: 16px;
  width:10%;
}
.query-table th{
  font-family: roboto-serif-medium;
  align-content: center;
  text-align: center;
  vertical-align: middle;
  /*height: 15mm;*/
  width:10%;
}

.form-block-style{
  height: 100px;
  width:68%;
  background: #E9E9E8;
  border-radius: 5px;
}

.search-btn-style{
  width:143px;
  height: 41px;
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
  text-align: center;
  font-family: roboto-serif-regular;
}
.search-btn-style:active {
  box-shadow: 2px 2px 3px 2px darkgrey;
  /*transform: translateY(2px);*/
}
.clear-all-btn-style{
  width:143px;
  height: 41px;
  background-color: #FF6A63;
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
  font-family: roboto-serif-regular;
}
.clear-all-btn-style:active {
  box-shadow: 2px 2px 3px 2px darkgrey;
  /*transform: translateY(2px);*/
}
</style>