<template>
  <div>
    <router-view />
    <HeaderComponent />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import HeaderComponent from './components/HeaderComponent.vue'

export default defineComponent({
  components: {
    HeaderComponent
  }
  // setup() {

  // },
})
</script>

<style></style>
