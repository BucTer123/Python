import webview 

html='''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" >
	<title>Main Site</title>
	<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
</head>
<style>
	#map {
		width: 100%;
		height: 100vh;
	}
</style>
<body>
	<div id="map"></div>
</body>
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
	var map = L.map('map').setView([48.29569960648587, 25.933912477867402], 13);
	
	L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
		attribution: '&copy; OpenStreetMap & CartoDB'
	}).addTo(map);
</script>
</html>
'''

webview.create("UI", html=html)
webview.run()