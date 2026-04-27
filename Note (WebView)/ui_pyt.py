import webview 

html =''''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" >
    <title>UI</title>
</head>
<style>
    body {
        background: white;
        color: black;
        font-family: sans-serif;
        font-size: medium;
        font-weight: bolder;
        font-style: initial;
        padding: 0;
        margin: 0;
    }
    
    textarea {
        background: gray;
        color: white;
        padding: 50px;
        margin: 25px;
        border: 1px solid dimgray;
        opacity: 1;
    }
    
    textarea:focus {
        background: white;
        color: gray;
        border: 1px solid blue;
        opacity: 0.9;
    }
    
    button {
        background: black;
        color: white;
        padding: 18px;
        margin: 9px;
        border: 1px solid dimgray;
        opacity: 1;
    }
    
    button:focus {
        background: white;
        color: black;
        border: 1px solid blue;
        opacity: 0.9;
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
    <textarea id="text" ></textarea>
    <br><br>
    
    <button id="note">Save</button>
</body>
</html>
'''

def function_ui_pyt():
    webview.create("UI", 640, 480, html=html)
    webview.run()