<template>
    <div id="profile">
        <div id="profile-image">
            <img src="../assets//images/pudzian.jpg" alt="img">
        </div>
        <div class="info">
            <label for="exampleFormControlInput1" class="form-label">Email address</label>
            <label for="exampleFormControlInput1" class="form-label value">email</label>
            <br>
        </div>
        <button style="min-width: 80px;" class="custom-button" @click="addData">ADD DATA</button>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    // setup() {

    // },
    methods: {
        addData(): void {
            this.$router.push('/profile');
        }
    }
})
</script>

<style>
#profile {
    border: 1px solid rgba(187, 134, 252, 0.3);
    box-shadow: 0px 0px 0px 3px rgba(187, 134, 252, 0.2);
    width: 25vw;
    height: 80vh;
    min-width: 200px;
    border-radius: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: fixed;
    top: 0;
    margin-top: 10vh;
    right: 0;
    margin-right: 2vw;
    background-color: #121212;
    transition: background-color 0.3s;
}

#profile-image {
    width: 6rem;
    height: 6rem;
    margin-top: 5vh;
}

#profile-image img {
    height: 100%;
    width: 100%;
    border-radius: 100px;
    object-fit: contain;
    box-shadow: 0px 0px 20px 0px rgba(187, 134, 252, 0.4);
}

.info {
    width: 20vw;
    height: 50vh;
    padding-top: 2vw;
    display: flex;
    flex-direction: column;
    align-items: left;
    align-content: center;
    flex-wrap: wrap;
    word-wrap: break-word;
}
</style>
