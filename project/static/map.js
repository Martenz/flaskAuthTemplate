// alert("I'm the map JS Duccio.")

var mymap = L.map('mapid').setView([49.06, 76.14], 3);

var CartoDB_Positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
	subdomains: 'abcd',
	maxZoom: 19
});

CartoDB_Positron.addTo(mymap);

$('#addpoint').on('click',function(){
	$('#mapid_container').removeClass('col-sm-12');
	$('#mapid_container').addClass('col-sm-3');
	$('#mappage_container').show();
});

function onClick(e) {
    //alert(this.getLatLng()+' | '+this.key);
	window.open("/map/"+this.key,"_self");
}