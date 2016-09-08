$(function(){
	//23.534253, -46.921777
/*	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	}else{
		
	}
	function getCoords(position){
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;
		initialize(lat, lng);
	}	*/
	var lat = -23.534253;
	var lng = -46.921777;
	initialize(lat, lng);
	function getError(err){
		//alert(err.message);
		initialize(13.302272, -87.194107);
	}
	function initialize(lat, lng){
		var latlng = new google.maps.LatLng(lat, lng);
		var mapSettings = {
			center: latlng,
			zoom:15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		map = new google.maps.Map($('#mapa').get(0), mapSettings);

		var marker = new google.maps.Marker({
			position: latlng,
			map: map,
			draggable: true,
			title: 'Arrastrame'
		});

		google.maps.event.addListener(marker, 'position_changed', function(){
				getMarkerCoords(marker);
		});
	}
	function getMarkerCoords(marker){
		var markerCoords = marker.getPosition();
		// console.log(markerCoords.lat() + ' ' + markerCoords.lng());
		$('#id_latI').val(markerCoords.lat());
		$('#id_lngI').val(markerCoords.lng());
	}
	$('#form_coords').submit(function(e){
		// e.eventDefault();//nao enviar para a url default
		e.preventDefault();
		$.post('/coords/save', $(this).serialize(), function(data){			
			console.log('inicio2');
			console.log(data);
			if(data.ok)
			{
				$('#data').html(data.msg);
				$('#form_coords').each(function(){ this.reset(); });
			}else{
				alert(data.msg);
			}
		}, 'json');
	});

});