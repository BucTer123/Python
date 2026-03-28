const usr = document.getElementById("username");
const psw = document.getElementById("password");
const btn = document.getElementById("log");

btn.addEventListener("click", function () {
    if (usr.value === "" || psw.value === "") {
        window.alert("ERROR!: Write username and password!");
    } else {
        window.alert("Opening :")
        window.open("main_file/hello.html");
    }
})