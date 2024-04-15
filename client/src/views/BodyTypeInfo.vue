<template>
    <div class="container">
        <img id="bodytype-img" src="../assets/images/bodytype-info.png" alt="bodytype info">
        <RouterLink to="/profile">
            <button id="back-to-profile-button" class="custom-button">OK</button>
        </RouterLink>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { setBackgroundColor } from '../ts-files/backgroundColor';

export default defineComponent({
    mounted() {
        window.scrollTo(0, 0)
        setBackgroundColor()
    }
})
</script>


<style>
#bodytype-img {
    max-width: 40vw;
    min-width: 400px;
}

#back-to-profile-button {
    margin-top: 20vh;
}
</style>