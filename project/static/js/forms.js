$('#wine_form').submit(function(event){

	// event.preventDefault(); //to cancel submission
	fk_api = ['country', 'region', 'appelation','producer']
	manyTomany_key_api_list = ['Tag', 'Cepage'] // will need to iterate through structure, because we might have for than 1 item.
	
	self = this;

	for (var i=0; i < fk_api.length;i++){
		var data = {};
		value = $( '#id_' + fk_api[i] ).val();
		data[fk_api[i]] = value
		data['status'] = 'a'
		console.log(data);
		$.ajax({
			async: false,
			dataType:'json',
			type: 'POST',
			url: '/api/' + fk_api[i] + '/', // better if we could have {% url api:fk_api %}
			data: data
		});

	}
});