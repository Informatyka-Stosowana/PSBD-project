export function setBackgroundColor(): void {
            const backgroundColorButton = document.getElementById("background-mode-toggle") as HTMLInputElement | null
            const header = document.getElementById("header")
            const infoDiv = document.getElementsByClassName("card")
            const infoDivTitles = document.getElementsByClassName("card-title")
            const infoDivSubTitles = document.getElementsByClassName("card-subtitle")
            const profile = document.getElementById("profile")
            const container = document.getElementsByClassName("container")

            if (backgroundColorButton !== null) {
                if (backgroundColorButton.checked === true) {
                    document.body.style.background = "#edeced"
                    document.body.style.color = "black"

                    if (header !== null) {
                        header.style.background = "#aab2bd"
                    }

                    if (infoDiv !== null) {
                        for (let i = 0; i < infoDiv.length; i++) {
                            const element = infoDiv[i] as HTMLElement
                            element.style.background = "#aab2bd"
                            element.style.color = "black"
                        }
                    }

                    if (infoDivTitles !== null) {
                        for (let i = 0; i < infoDivTitles.length; i++) {
                            const element = infoDivTitles[i] as HTMLElement
                            element.style.color = "black"
                        }
                    }

                    if (infoDivSubTitles !== null) {
                        for (let i = 0; i < infoDivSubTitles.length; i++) {
                            const element = infoDivSubTitles[i] as HTMLElement
                            element.style.color = "rgba(0, 0, 0, 0.5)"
                        }
                    }

                    if (profile !== null) {
                        profile.style.background = "#aab2bd"
                    }

                    if (container !== null) {
                        for (let i = 0; i < container.length; i++) {
                            const element = container[i] as HTMLElement
                            element.style.background = "#aab2bd"
                        }
                    }
                }
                else {
                    document.body.style.background = "#000000"
                    document.body.style.color = "#FFFFFF"

                    if (header !== null) {
                        header.style.background = "#121212"
                    }

                    if (infoDiv !== null) {
                        for (let i = 0; i < infoDiv.length; i++) {
                            const element = infoDiv[i] as HTMLElement
                            element.style.background = "#121212"
                            element.style.color = "white"
                        }
                    }

                    if (infoDivTitles !== null) {
                        for (let i = 0; i < infoDivTitles.length; i++) {
                            const element = infoDivTitles[i] as HTMLElement
                            element.style.color = "aliceblue"
                        }
                    }

                    if (infoDivSubTitles !== null) {
                        for (let i = 0; i < infoDivSubTitles.length; i++) {
                            const element = infoDivSubTitles[i] as HTMLElement
                            element.style.color = "rgba(255, 255, 255, 0.3)"
                        }
                    }

                    if (profile !== null) {
                        profile.style.background = "#121212"
                    }

                    if (container !== null) {
                        for (let i = 0; i < container.length; i++) {
                            const element = container[i] as HTMLElement
                            element.style.background = "#121212"
                        }
                    }
                }
            }
        }