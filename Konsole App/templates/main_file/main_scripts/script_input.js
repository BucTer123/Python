const srch_input = document.getElementById("srch");
const btn_sr = document.getElementById("srch_btn");

btn_sr.addEventListener("click", function () {
    if (srch_input.value === "") {
        window.alert("Hi!");
    } else {
        window.alert("BETA!")
    }
})