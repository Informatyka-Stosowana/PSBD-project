<template>
    <div id="header">
        <div class="user-registration-div" style="font-size: small;">
            <router-link to="/register" id="sign-up-el" class="link-el">Sign up</router-link>
            <router-link to="/" class="link-el">Sign in</router-link>
        </div>
        <router-link to="/" class="link-el">Home</router-link>
        <router-link to="/about" class="link-el">About</router-link>
        <router-link to="/profile" class="link-el">Profile</router-link>
        <BackgroundModeComponent />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import BackgroundModeComponent from './BackgroundModeComponent.vue';

export default defineComponent({
    components: {
        BackgroundModeComponent
    }
    // setup() {

    // },
})
</script>

<style>
#header {
    border-bottom: 1px solid rgba(187, 134, 252, 0.3);
    box-shadow: 0 6px 10px 2px rgba(187, 134, 252, 0.15);
    width: 100vw;
    height: 7vh;
    background-color: #121212;
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    transition: background-color 0.3s;
}

.user-registration-div {
    position: fixed;
    left: 0.5vw;
    font-weight: lighter;
    display: flex;
    flex-direction: row;
    opacity: 0.7;
}
</style>
