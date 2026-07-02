import webview 


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" >
    <title>UI</title>
</head>
<style>
    body {
        background: whitesmoke;
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
    }
</style>
<body>
    <input id="fl" type="file" />
    <br><br>

    <audio id="pl" width="800" height="600" ></audio>
</body>
<script>
    const f = document.getElementById("fl");
    const p = document.getElementById("pl");

    const file = this.file[0];
    f.addEventListener("change", function () {
        if (file) {
            const url = URL.createObjectURL(file);
            p.src = url;
            p.play();
        }
    });
</script>
</html>
"""

def second_script():
    webview.create("UI", html=html)
    webview.run()
