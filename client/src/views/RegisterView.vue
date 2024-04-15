<template>
    <div class="container" style="display: flex; align-items: center; justify-content: center;">
        <h3 style="position: fixed; top: 15vh;">Sign up</h3>
        <div class="mb-3 data-input">
            <label for="exampleFormControlInput1" class="form-label">Username</label>
            <input type="text" class="form-control" placeholder="username" v-model="username">
            <br>
            <label for="exampleFormControlInput1" class="form-label">Email</label>
            <input type="email" class="form-control" placeholder="example@example.com" v-model="email">
            <br>
            <label for="exampleFormControlInput1" class="form-label">Password</label>
            <input type="password" class="form-control" placeholder="******" v-model="password">
            <br>
            <div class="error" v-html="error" style="color: red;" />
            <br>
            <button class="custom-button" @click="registerNewUser()">SIGN UP</button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'
import { setBackgroundColor } from '../ts-files/backgroundColor';
import RegistrationService from '../services/RegistrationService';


export default defineComponent({
    setup() {
        const username = ref("")
        const email = ref("")
        const password = ref("")
        const error = ref("")

        return { username, email, password, error }
    },
    mounted() {
        setBackgroundColor()
    },
    methods: {
        async registerNewUser() {
            try {
                await RegistrationService.register({
                    nazwa_uzytkownika: this.username,
                    email: this.email,
                    haslo: this.password
                })
                this.$router.push('/profile');
            } catch (error: any) {
                console.log(error)
                this.error = error.response.data.error
            }
        }
    }
})
</script>
