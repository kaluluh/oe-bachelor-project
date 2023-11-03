<template>
  <div id="app">
    <div class="container">
      <div id="home" class="container-fluid custom-class" style="height: 100%">
        <div class="mx-auto col-12 col-md-8 col-lg-7 form-block-style" style="margin-top: 0mm;background-color: #0D2837">
          <div class="row" style="margin-left: 5mm;">
            <div class="col-sm-3" style="margin-top: 3mm;">
              <label style="color: white">Age</label>
              <div class="d-inline-flex">
                <input type="text" class="form-control radio-inline" placeholder="From" v-model="statisticsQuery.ageFrom">
                <a style="margin-left: 1mm;margin-right: 1mm;">-</a>
                <input type="text" class="form-control radio-inline" placeholder="To" v-model="statisticsQuery.ageTo">
              </div>
            </div>
            <div class="col-sm-2" style="margin-top: 3mm;">
              <label style="color: white">Tirads Score</label>
              <input type="text" class="form-control" v-model="statisticsQuery.tiradsScore">
            </div>
            <div class="form-group col-sm-2" style="margin-top: 3mm;">
              <label for="gender-list" style="color: white">Gender</label>
              <select class="form-control" id="gender-list" v-model="statisticsQuery.gender">
                <option value=""></option>
                <option value="F">Female</option>
                <option value="M">Male</option>
              </select>
            </div>
            <div class="col-sm-5" style="margin-top: 8mm;">
              <button type="submit" class="search-btn-style" style="margin-right: 2mm;" @click="search">Search</button>
              <button type="submit" class="clear-all-btn-style" @click="clearAll">Clear all</button>
            </div>
          </div>
        </div>
      </div>

        <div class="d-inline col-md-15 align-items-center" style="margin-top: 5mm;">

          <div class="col-md-5" style="margin-left: 20mm; min-height:100px;border-radius: 9px">
            <div>
              <div id="chart" style="background-color: #F2F2F1;margin-top: 5mm;">
                <apexchart type="pie" width="380" :options="chartOptions" :series="series"></apexchart>
              </div>
            </div>
          </div>
        </div>
<!--          <div class="mx-auto col-12 col-md-8 col-lg-7 form-block-style" style="float: left; min-height:100px;margin-top: 10mm;margin-left: 50mm">mm-->
<!--              <div class="d-flex" >-->
                <div class="d-inline-block" style="margin-left: 20mm;margin-top: 10mm">
                  <table class="table query-table" v-show="casesList">
                    <thead>
                    <tr>
                      <th scope="col">Case number</th>
                      <th scope="col">Date</th>
                      <th scope="col">Gender</th>
                      <th scope="col">Age</th>
                      <th scope="col">Tirads</th>
                      <th scope="col">Medical Doctor</th>
                      <th scope="col">Radiologist</th>
                    </tr>
                    </thead>
                    <tbody v-for="patientCase in casesList" :key="patientCase.caseId">
                    <tr @click="showCase(patientCase.caseId)" v-show="patientCase.caseId != patientCaseElement.caseId">
                      <!--        <th scope="row"> <img class="img-fluid" :src=vectorRightImage> </th>-->
                      <th scope="row" v-show="patientCaseElement && patientCase.caseId == patientCaseElement.caseId"> <img class="img-fluid" :src=vectorDownImage> </th>
                      <td> {{ patientCase.caseId }}</td>
                      <td> {{ dateTimeFormat(patientCase.created) }}</td>
                      <!--        <td>  </td>-->
                      <td> {{ patientCase.sex }}</td>
                      <td style="align-content: center;"> {{ patientCase.age }} </td>
                      <td> {{ patientCase.tirads }} </td>
                      <td style="align-content: center;"> {{ patientCase.medicalDoctor }} </td>
                      <td style="align-content: center;"> {{ patientCase.radiologist }} </td>
                    </tr>
                    <tr v-show="patientCaseElement && patientCase.caseId == patientCaseElement.caseId" class="selected-table-style">
                      <td colspan="9">
                        <table>
                          <tbody>
                          <tr v-show="!this.isEdit">
                            <!--              <th scope="row"> <img class="img-fluid" :src=vectorDownImage> </th>-->
                            <td> {{ patientCase.caseId }}</td>
                            <td> {{ dateTimeFormat(patientCaseElement.created) }}</td>
                            <!--              <td>  </td>-->
                            <td> {{ patientCaseElement.sex }}</td>
                            <td style="align-content: center;"> {{ patientCaseElement.age }} </td>
                            <td> {{ patientCaseElement.tirads }} </td>
                            <td style="align-content: center;"> {{ patientCaseElement.medicalDoctor }} </td>
                            <td style="align-content: center;"> {{ patientCaseElement.radiologist }} </td>
                          </tr>
                          <tr v-show="this.isEdit">
                            <!--              <th scope="row"> <img class="img-fluid" :src=vectorDownImage> </th>-->
                            <td> {{ patientCase.caseId }}</td>
                            <td> <input type="text" class="form-control" v-model="patientCaseElement.created"></td>
                            <!--              <td>  </td>-->
                            <td style="align-items: center;"> <input type="text"  class="form-control"   v-model="patientCaseElement.sex"> </td>
                            <td style="align-content: center;"> <input type="text" class="form-control" v-model="patientCaseElement.age"> </td>
                            <td> <input type="text" class="form-control"  v-model="patientCaseElement.tirads"> </td>
                            <td style="align-content: center;"> <input type="text" class="form-control" v-model="patientCaseElement.medicalDoctor"> </td>
                            <td style="align-content: center;"> <input type="text" class="form-control" v-model="patientCaseElement.radiologist"></td>
                          </tr>
                          <tr>
                            <td></td>
                            <td colspan="3"><img :src=caseSampleImage></td>
                            <td></td>
                            <td colspan="4">
                              <div class="row" style="font-family: roboto-serif-regular">
                                <div style="text-align: left;">
                                  <a style="font-family: roboto-serif-medium" v-show="patientCaseElement.isDiagnosedByAi == 1">Tirads score set by AI</a>
                                  <a style="font-family: roboto-serif-medium" v-show="patientCaseElement.isDiagnosedByAi == 0 || patientCaseElement.isDiagnosedByAi == null">Tirads score set manually</a>
                                  <p>{{patientCaseElement.tirads}} - {{ tiradsSuspiciousType }}</p>
                                </div>
                                <div class="d-inline-flex">
                                  <button class="disabled-button-style" v-show="!this.isEdit" type="submit" @click="this.isEdit=false;saveCase()" disabled style="margin-right: 5mm;"> Confirm </button>
                                  <button class="confirm-button-style" v-show="this.isEdit" type="submit" @click="saveCase()" style="margin-right: 5mm;"> Confirm </button>
                                  <button class="edit-button-style" type="submit" @click="this.isEdit=true"> Edit </button>
                                  <button class="exit-from-edit-button-style" v-show="this.isEdit" type="submit" @click="this.isEdit=false;"> x </button>
                                </div>
<!--                                <div class="d-inline-flex" style="margin-top: 6mm;">-->
<!--                                  <button class="analysis-button-style" type="submit"> Select for analysis </button>-->
<!--                                </div>-->
                                <div style="text-align: left;margin-top: 4mm;">
                                  <a style="font-family: roboto-serif-medium;">Medical Note</a>
                                  <p v-show="!this.isEdit" style="margin-top: 4mm;font-size: 16px;">
                                    {{ patientCaseElement.medicalNote }}</p>
                                  <p v-show="this.isEdit" style="margin-top: 4mm;font-size: 16px;">
                                    <input type="text" class="form-control" height="50px;" v-model="patientCaseElement.medicalNote">
                                  </p>
                                </div>
                              </div>
                            </td>
                          </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
          </div>
<!--      </div>div-->
<!--    </div>-->


</template>
<script>
import axios from "axios";
import moment from "moment";
import VueApexCharts from "vue3-apexcharts";

export default {
  name: "StatisticsPage",
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    channel1: Number,
    channel2: Number,
  },
  data() {
    return {
      statisticsQuery: {
        ageFrom:null,
        ageTo:null,
        tiradsScore:"",
        gender:""
      },
      tiradsSuspiciousType:null,
      isEdit:false,
      responseData: [],
      casesList:null,
      isShow: false,
      patientCaseElement: [],
      vectorDownImage: require('../assets/images/vector-down.png'),
      vectorRightImage: require('../assets/images/vector-right.png'),
      caseSampleImage: require('../assets/images/case-sample.png'),
      series: [283,60],
      chartOptions: {
        colors: ['#FF6A63','#01BC8E'],
        chart: {
          width: 380,
          type: 'pie',
        },
        labels: ['Malignant' , 'Benign'],
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            },
            legend: {
              position: 'bottom'
            }
          }
        }]
      }
    }
  },
  async created() {
   await axios.get(this.hostname + '/case/get-all')
       .then(response => this.responseData = response.data)
       .catch(error => {
         this.errorMessage = error.message;
         console.error("There was an error!", error);
       });
  },
  methods: {
    search() {
      console.log(this.statisticsQuery);
      axios.post(this.hostname + '/case/run-statistics-query/', this.statisticsQuery)
          .then(response => {
            this.casesList = response.data['patientCasesList'];
            this.responseData = response.data;
            this.series = [Number(this.responseData['positiveCount']),Number(this.responseData['negativeCount'])];
            const malignantLabel = 'Malignant ' + this.responseData['positiveCount'];
            const benignLabel = 'Benign ' + this.responseData['negativeCount'];
            this.chartOptions = {labels:[malignantLabel,benignLabel]}
          }).catch(error => {
        this.response = 'Error' + error.response.status;
      });
    },
    clearAll () {
      this.statisticsQuery.tiradsScore = "";
      this.statisticsQuery.gender = "";
      this.statisticsQuery.ageFrom = null;
      this.statisticsQuery.ageTo = null;
      this.casesList = [];
    },
    showCase (id) {
      console.log(id);
      this.getCaseById(id);
      this.isShow = true;
    },
    setTiradsSuspiciousType(tiradsScore) {
      if (tiradsScore == 5) {
        this.tiradsSuspiciousType = "highly suspicous";
      } else if (tiradsScore == 4){
        this.tiradsSuspiciousType = "moderately suspicous";
      } else if (tiradsScore == 3){
        this.tiradsSuspiciousType = "mildy suspicous";
      } else if (tiradsScore == 2){
        this.tiradsSuspiciousType = "not suspicous";
      } else if (tiradsScore == 1){
        this.tiradsSuspiciousType = "benign";
      }
    },
    dateTimeFormat(value) {
      if( value != null)
        return moment(value).format("YYYY-MM-DD");
      else
        return "unknown";
    },
    getCaseById(id) {
      var indexOfCase = this.casesList.findIndex(x => x.caseId === id);
      this.patientCaseElement = this.casesList[indexOfCase];
      this.setTiradsSuspiciousType(this.patientCaseElement.tirads.charAt(0));
      console.log(this.patientCaseElement);
    },
    saveCase(){
      this.isEdit = false;
      this.setTiradsSuspiciousType(this.patientCaseElement.tirads.charAt(0));
      axios.post(this.hostname + '/case/update/', this.patientCaseElement)
          .catch(error => {
        this.response = 'Error' + error.response.status;
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