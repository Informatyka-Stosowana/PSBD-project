<template>
  <div>
    <div class="background-image-div">
      <BackgroundDrugs />
    </div>
    <div class="home">
      <div class="home-window">
        <!-- CPM -->
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">CPM</h5>
            <h6 class="card-subtitle mb-2">Calculated CPM</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
        <!-- BMI -->
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">BMI</h5>
            <h6 class="card-subtitle mb-2">Calculated BMI</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle mb-2">Card subtitle</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle mb-2">Card subtitle</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle mb-2">Card subtitle</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <h6 class="card-subtitle mb-2">Card subtitle</h6>
            <p class="card-text">Value</p>
          </div>
        </div>
      </div>
      <ProfileComponent />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ProfileComponent from '../components/ProfileComponent.vue'
import BackgroundDrugs from '../components/BackgroundDrugs.vue';
import { setBackgroundColor } from '../ts-files/backgroundColor';

export default defineComponent({
  name: 'HomeView',
  components: {
    ProfileComponent,
    BackgroundDrugs
  },
  mounted() {
    window.scrollTo(0, 0)
    setBackgroundColor()
  }
  // setup() {

  // }
});
</script>

<style>
.home-window {
  width: 70vw;
  height: 110vh;
  display: flex;
  justify-content: center;
  align-content: baseline;
  flex-direction: row;
  flex-wrap: wrap;
}

.home {
  padding-top: 2vh;
  display: flex;
  flex-direction: row;
}

.card {
  height: 25vh;
  margin: 1%;
  text-align: center;
  color: #FFFFFF;
  background-color: #121212;
  transition: color 0.3s background-color 0.3s;
}

.card:hover {
  border: 1px solid rgba(187, 134, 252, 0.3);
  box-shadow: 0px 0px 0px 3px rgba(187, 134, 252, 0.2);
}

.card-title {
  color: aliceblue;
  transition: color 0.3s;
}

.card:hover .card-title {
  color: rgba(187, 134, 252, 0.7);
}

.card-subtitle {
  color: rgba(255, 255, 255, 0.3);
  font-weight: normal;
  transition: color 0.3s;
}
</style>