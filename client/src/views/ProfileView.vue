<template>
    <div class="container">
        <div id="profile-image">
            <img src="../assets//images/pudzian.jpg" alt="img">
        </div>
        <div class="mb-3 data-input">
            <label for="exampleFormControlInput1" class="form-label">Email address</label>
            <br>
            <label for="exampleFormControlInput1" class="form-label value">{{ email }}</label>
            <br>
            <label for="exampleFormControlInput1" class="form-label">Password</label>
            <br>
            <label for="exampleFormControlInput1" class="form-label value">{{ password }}</label>
            <br>
            <label for="exampleFormControlInput1" class="form-label">Age*</label>
            <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="your age">
            <br>
            <label for="exampleFormControlInput1" class="form-label">Weight [kg]*</label>
            <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="your weight">
            <br>
            <label for="exampleFormControlInput1" class="form-label">Height [cm]*</label>
            <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="your height">
            <br>
            <label for="exampleFormControlInput1" class="form-label">Body type</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>Endomorph</option>
                <option value="ectomorph">Ectomorph</option>
                <option value="mesomorth">Mesomorth</option>
            </select>
            <RouterLink to="/profile/bodytype" style="font-size: small;">Get more info about body types</RouterLink>
            <br>
            <br>
            <label for="exampleFormControlInput1" class="form-label">What's your goal?</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>Building muscle mass</option>
                <option value="1">Reduction of fat tissue</option>
                <option value="2">Maintaining body weight</option>
                <option value="3">General improvement in condition</option>
            </select>
            <br>
            <label for="exampleFormControlInput1" class="form-label">What kind of lifestyle do you lead?</label>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="lifestyle-active">
                <label class="form-check-label value" for="flexCheckDefault">
                    Active
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="lifestyle-sedentary" checked>
                <label class="form-check-label value" for="flexCheckChecked">
                    Sedentary
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="lifestyle-student">
                <label class="form-check-label value" for="flexCheckDefault">
                    Student
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="lifestyle-nightowl">
                <label class="form-check-label value" for="flexCheckDefault">
                    Night owl
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="lifestyle-athlete">
                <label class="form-check-label value" for="flexCheckDefault">
                    Athlete
                </label>
            </div>
            <br>
            <label for="exampleFormControlInput1" class="form-label">Additional remarks</label>
            <br>
            <div class="input-group">
                <textarea class="form-control" aria-label="With textarea" placeholder="type your remarks here"
                    id="textarea-remarks"></textarea>
            </div>
            <br>
            <br>
            <button class="custom-button" @click="updpateUserProfile()">SEND</button>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue';
import { setBackgroundColor } from '../ts-files/backgroundColor';

export default defineComponent({
    components: {
    },
    mounted() {
        window.scrollTo(0, 0)
        setBackgroundColor()
    },
    setup() {
        const email = ref("mariusz.pudzianowski@pudzian.pl")
        const password = ref("********")

        return { email, password }
    },
    methods: {
        updpateUserProfile(): void {
            this.$router.push("/")
        }
    }
})
</script>

<style>
.container {
    background-color: #121212;
    width: 50vw;
    min-width: 500px;
    min-height: 85vh;
    margin-top: 10vh;
    padding-top: 5vh;
    padding-bottom: 5vh;
    display: flex;
    align-items: center;
    flex-direction: column;
    margin-bottom: 5vh;
    border-radius: 10px;
    transition: background-color 0.3s;
}

.data-input {
    width: 30vw;
    margin-top: 5vh;
}

.form-control:focus {
    border: 1px solid rgba(55, 0, 179, 0.6);
    box-shadow: 0px 0px 6px 2px rgba(55, 0, 179, 0.5);
}

.value {
    opacity: 0.6;
}
</style>
