<template>
    <input type="checkbox" id="background-mode-toggle" @click="changeBackgroundColor">
    <label class="change-mode-label" for="background-mode-toggle"></label>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { setBackgroundColor } from '@/ts-files/backgroundColor';

export default defineComponent({
    // setup() {

    // },
    methods: {
        changeBackgroundColor(): void {
            // let backgroundColorButton = document.getElementById("background-mode-toggle") as HTMLInputElement | null
            // let header = document.getElementById("header")
            // let infoDiv = document.getElementsByClassName("card")
            // let infoDivTitles = document.getElementsByClassName("card-title")
            // let infoDivSubTitles = document.getElementsByClassName("card-subtitle")
            // let profile = document.getElementById("profile")
            // let container = document.getElementsByClassName("container")

            // if (backgroundColorButton !== null) {
            //     if (backgroundColorButton.checked === true) {
            //         document.body.style.background = "#edeced"
            //         document.body.style.color = "black"

            //         if (header !== null) {
            //             header.style.background = "#aab2bd"
            //         }

            //         if (infoDiv !== null) {
            //             for (let i = 0; i < infoDiv.length; i++) {
            //                 const element = infoDiv[i] as HTMLElement
            //                 element.style.background = "#aab2bd"
            //                 element.style.color = "black"
            //             }
            //         }

            //         if (infoDivTitles !== null) {
            //             for (let i = 0; i < infoDivTitles.length; i++) {
            //                 const element = infoDivTitles[i] as HTMLElement
            //                 element.style.color = "black"
            //             }
            //         }

            //         if (infoDivSubTitles !== null) {
            //             for (let i = 0; i < infoDivSubTitles.length; i++) {
            //                 const element = infoDivSubTitles[i] as HTMLElement
            //                 element.style.color = "rgba(0, 0, 0, 0.5)"
            //             }
            //         }

            //         if (profile !== null) {
            //             profile.style.background = "#aab2bd"
            //         }

            //         if (container !== null) {
            //             for (let i = 0; i < container.length; i++) {
            //                 const element = container[i] as HTMLElement
            //                 element.style.background = "#aab2bd"
            //             }
            //         }
            //     }
            //     else {
            //         document.body.style.background = "#000000"
            //         document.body.style.color = "#FFFFFF"

            //         if (header !== null) {
            //             header.style.background = "#121212"
            //         }

            //         if (infoDiv !== null) {
            //             for (let i = 0; i < infoDiv.length; i++) {
            //                 const element = infoDiv[i] as HTMLElement
            //                 element.style.background = "#121212"
            //                 element.style.color = "white"
            //             }
            //         }

            //         if (infoDivTitles !== null) {
            //             for (let i = 0; i < infoDivTitles.length; i++) {
            //                 const element = infoDivTitles[i] as HTMLElement
            //                 element.style.color = "aliceblue"
            //             }
            //         }

            //         if (infoDivSubTitles !== null) {
            //             for (let i = 0; i < infoDivSubTitles.length; i++) {
            //                 const element = infoDivSubTitles[i] as HTMLElement
            //                 element.style.color = "rgba(255, 255, 255, 0.3)"
            //             }
            //         }

            //         if (profile !== null) {
            //             profile.style.background = "#121212"
            //         }

            //         if (container !== null) {
            //             for (let i = 0; i < container.length; i++) {
            //                 const element = container[i] as HTMLElement
            //                 element.style.background = "#121212"
            //             }
            //         }
            //     }
            // }
            setBackgroundColor()
        }
    }
})
</script>


<style>
.change-mode-label {
    width: 50px;
    height: 25px;
    position: fixed;
    display: block;
    background: #242422;
    border-radius: 20px;
    box-shadow: inset 0px 1px 2px rgba(0, 0, 0, 0.4), inset 0px -1px 2px rgba(255, 255, 255, 0.3);
    cursor: pointer;
    transition: 0.3s;
    right: 1vw;
}

.change-mode-label:after {
    content: "";
    width: 20px;
    height: 20px;
    position: absolute;
    top: 2.75px;
    left: 2.75px;
    background: linear-gradient(180deg, #777, #3a3a3a);
    border-radius: 100px;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

#background-mode-toggle {
    width: 0;
    height: 0;
    visibility: hidden
}

#background-mode-toggle:checked+.change-mode-label {
    background: #ebebeb;
}

#background-mode-toggle:checked+.change-mode-label:after {
    left: 47.5px;
    transform: translateX(-100%);
    background: linear-gradient(180deg, rgba(187, 134, 252, 0.2), rgb(187, 134, 252));
}
</style>