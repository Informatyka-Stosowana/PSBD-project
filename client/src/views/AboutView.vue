<template>
  <div>
    <div>
      <BackgroundDrugs />
    </div>
    <div class="about">
      <div class="about-window">
        <h1>This is an about view</h1>
      </div>
      <ProfileComponent />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ProfileComponent from '../components/ProfileComponent.vue'
import BackgroundDrugs from '../components/BackgroundDrugs.vue';
import { setBackgroundColor } from '../ts-files/backgroundColor';

export default defineComponent({
  components: {
    ProfileComponent,
    BackgroundDrugs
  },
  mounted() {
    window.scrollTo(0, 0)
    setBackgroundColor();
  }
  // setup() {

  // },
})
</script>

<style>
.about {
  padding-top: 10vh;
  display: flex;
  flex-direction: row;
}

.about-window {
  width: 70vw;
  height: 110vh;
  display: flex;
  justify-content: center;
}
</style>
