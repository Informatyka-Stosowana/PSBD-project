<template>
    <div class="menu">
        <nav>
            <router-link to="/" class="link-el">Home</router-link>
            <router-link to="/about" class="link-el">About</router-link>
            <router-link to="/about" class="link-el">About</router-link>
            <router-link to="/about" class="link-el">About</router-link>
            <router-link to="/about" class="link-el">About</router-link>
            <router-link to="/about" class="link-el">About</router-link>
        </nav>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    // setup() {

    // },
})
</script>

<style>
.menu {
    border: 2px solid black;
    width: 15vw;
    height: 100vh;
    /* min-width: 15vw;
    min-height: 100vw; */
    display: flex;
    justify-content: center;
    padding-top: 5vh;
}
</style>
