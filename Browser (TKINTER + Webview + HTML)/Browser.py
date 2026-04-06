import webview

html """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" >
    <title>Browse</title>
</head>
<style>
    body {
        background: ghostwhite;
        color: black;
        font-family: sans-serif;
        font-size: medium;
        font-weight: bolder;
        font-style: initial;
        padding: 0;
        margin: 0;
        max-width: 1920px;
        width: 100%;
        max-height: 1080px;
        height: 100%;
        display: flex;
        border: none;
    }

    .contain {
        background: white;
        color: black;
        padding: 192px;
        margin: 108px;
        border: 1px solid gray;
    }

    .buttons {
        background: aliceblue;
        color: black;
        padding: 96px;
        margin: 54px;
    }

    button {
        background: black;
        color: white;
        padding: 18px;
        margin: 9px;
        border: 1px solid gray;
        opacity: 1;
    }

    button:focus {
        background: white;
        color: black;
        border: 1px solid blue;
    }

    button:hover {
        opacity: 0.7;
        transform: translateY(4px);
    }

    button:active {
        opacity: 0.3;
        transform: translateX(5px);
    }

    input {
        background: black;
        color: white;
        padding: 16px;
        margin: 8px;
        border: 1px solid gray;
    }

    input:focus {
        background: white;
        color: black;
        border: 1px solid gray;
    }
</style>
<body>
<div class="contain">
    <input id="srch_input" type="text" placeholder="Search ...." />
    <button id="srch_butt" type="button">Search</button>
</div>
<div class="buttons" >
    <button id="newwin" type="button">New Window</button>
    <button id="lv" type="button">Leave</button>
</div>
</body>
<script>
    const inp1 = document.geElementById("srch_input");
    const btn1 = document.getElementById("srch_butt");
    const btn2 = document.getElementById("newwin");
    const btn3 = document.getElementById("leave");

    btn1.addEventListener("click", function () {
        const go = inp1.value;

        if (go === "") {
            window.alert("ERROR!: Write domain !");
        } else {
            window.open(go, "_blank");
        }
    });
    
    btn2.addEventListener("click", function () {
        window.open("main.html");
    });

    btn3.addEventListener("click", function () {
        exit(0);
    });
</script>
</html>
"""


def starter_comm():
    webview.create_window("Gui", html=html)
    webview.start()