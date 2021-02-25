alert("I'm the map JS Duccio.")

var mymap = L.map('mapid').setView([45.91115427928255, 8.642077649021676], 13);

var CartoDB_Positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
});

CartoDB_Positron.addTo(mymap);