$(document).ready(function(){
	
function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
}

//====================================
// ACTIVE NAVBAR SELECTOR
//====================================

arr_path = location.pathname.split('/');
if(arr_path.length < 3){
	//we are at the root, since we usually have a structure like /app_name/
	selector = "href='/'"
}
else{
	selector = "href*='" + arr_path[1]+ "'"
}
// add deactivate class to element if we want to prevent an element from being set as active
// See for more info on selectors: http://www.w3schools.com/jquery/jquery_ref_selectors.asp
$('.navbar-nav>li a[' + selector + '][class!="deactivate"]').parent().addClass('active');


//====================================
// adding bootstrap classes
//====================================

$('input,select').attr('class','form-control');


//====================================
// WINE EXISTANCE CHECK
//====================================
$('#id_name').click(function(){
	$(this).parent().find('.help-block').hide();
	$(this).closest('.form-group').removeClass('has-error');
});
$('#id_name').focusout(function(evt){
	name_to_check = evt.target.value;
	console.log(name_to_check);
	$.ajax({
		url: '../../api/wine?name='+name_to_check,
		cache: false,
		success: function(data){
			if (data.length){
				console.log(data);
				$('#id_name').closest('.form-group').addClass('has-error');
				$('#id_name').parent().append(
					$('<span>',{
						class:'help-block',
						text: 'The wine already exists.'
					})
				)

			}
		}
	})
});



//====================================
// TypeAhead
//====================================
arr_typeaheads = ['country','cepage','tag','region','producer'];

$('#id_country').typeahead({
	name: 'Countries',
	template: '<p><strong>{{name}}</strong></p>',
	engine: Hogan,
	prefetch: {
		url: '../../api/country',
		filter: function(parsedResponse){
			arr_datums = [];
			for (var idx=0; idx<parsedResponse.length;idx++){
				data = parsedResponse[idx]['country'];
				
				elem = {
					value: data,
					tokens: [data,capitalize(data)],
					name: data
				} 
				arr_datums.push(elem);
			} 
			return arr_datums;
		}
	}
});


$('#id_cepage').typeahead({
	name: 'Cepages',
	template: '<p><strong>{{name}}</strong></p>',
	engine: Hogan,
	prefetch: {
		url: '../../api/cepage',
		filter: function(parsedResponse){
			arr_datums = [];
			for (var idx=0; idx<parsedResponse.length;idx++){
				data = parsedResponse[idx]['cepage'];
				
				elem = {
					value: data,
					tokens: [data,capitalize(data)],
					name: data
				} 
				arr_datums.push(elem);
			} 
			return arr_datums;
		}
	}
});


$('#id_tag').typeahead({
	name: 'Tags',
	template: '<p><strong>{{name}}</strong></p>',
	engine: Hogan,
	prefetch: {
		url: '../../api/tag',
		filter: function(parsedResponse){
			arr_datums = [];
			for (var idx=0; idx<parsedResponse.length;idx++){
				data = parsedResponse[idx]['tag'];
				
				elem = {
					value: data,
					tokens: [data,capitalize(data)],
					name: data
				} 
				arr_datums.push(elem);
			} 
			return arr_datums;
		}
	}
});


$('#id_region').typeahead({
	name: 'Regions',
	template: '<p><strong>{{name}}</strong></p>',
	engine: Hogan,
	prefetch: {
		url: '../../api/region',
		filter: function(parsedResponse){
			arr_datums = [];
			for (var idx=0; idx<parsedResponse.length;idx++){
				data = parsedResponse[idx]['region'];
				
				elem = {
					value: data,
					tokens: [data,capitalize(data)],
					name: data
				} 
				arr_datums.push(elem);
			} 
			return arr_datums;
		}
	}
});


$('#id_producer').typeahead({
	name: 'Producers',
	template: '<p><strong>{{name}}</strong></p>',
	engine: Hogan,
	prefetch: {
		url: '../../api/producer',
		filter: function(parsedResponse){
			arr_datums = [];
			for (var idx=0; idx<parsedResponse.length;idx++){
				data = parsedResponse[idx]['producer'];
				
				elem = {
					value: data,
					tokens: [data,capitalize(data)],
					name: data
				} 
				arr_datums.push(elem);
			} 
			return arr_datums;
		}
	}
});

//====================================
// AJAX CONTENT POPULATING
//====================================

var teint = $('#id_teint option');
$('input[name="wineType"]').change(function(evt){
	winetype = evt.target.value;
	$.ajax({url: '/api/teint/',
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
