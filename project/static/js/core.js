$(document).ready(function(){
	
$('input,select').attr('class','form-control')


$('#id_name').typeahead({
	name: 'cepages',
	// local: ['timtrueman', 'JakeHarding', 'vskarich']
	template: '<p><strong>{{cepage}}</strong></p>',
	engine: Hogan,
		remote: {
			url: '../../api/cepage',
			dataType: 'json'
		}
});
$('#id_wineType').change(function(evt){
	winetype = evt.target.value;


	teint = $('#id_teint option');
	$.ajax({url:'/api/teint',
		cache: false,
		success:function(data){
			arr =[];
			filtered_data = data.filter(function(obj){
				if(obj.wineType == winetype){
					arr.push(obj.teint);
				}
				return obj.wineType==winetype;
			});

			filtered_options = teint.filter(function(index){
				return $.inArray(teint[index].text, arr) > -1;
			})

			$('#id_teint').html(filtered_options);
			// return filtered_data.sort(function(a, b){re	turn  a.order < b.order ? true:false;});
		}
	});
});

}); //document ready
