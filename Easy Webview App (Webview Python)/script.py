import webview

html = """
<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Easy Gui</title>
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
    }
    
    button {
        background: blue;
        color: white;
        padding: 14px;
        margin: 7px;
        border: 1px solid black;
        opacity: 1;
    }
    
    button:focus {
        background: white;
        color: blue;
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
</style>
<body>
    <button id="lv" type="button">Leave</button>
    <button id="gt" type="button">Next</button>
</body>
<script>
    const btn1 = document.getElementById("lv");
    const btn2 = document.getElementById("gt");
    
    btn1.addEventListener("click", function() {
        exit(0);
    }
    
    btn2.addEventListener("click", function() {
        window.open("main.html");
    }
</script>
"""

webview.create_window("EASY GUI", html=html)
webview.start()