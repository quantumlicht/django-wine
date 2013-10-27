$(document).ready(function(){
	


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
// TypeAhead
//====================================

$('#id_name').typeahead({
	name: 'cepages',
	template: '<p><strong>{{cepage}}</strong></p>',
	engine: Hogan,
		prefetch: {
			url: '../../api/cepage',
			dataType: 'json'
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
