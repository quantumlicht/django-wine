$(document).ready(function(){
	
function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
}

//====================================
// ACTIVE NAVBAR SELECTOR
//====================================

arr_path = location.pathname.split('/');
console.log('arr_path',arr_path);
if(arr_path.length < 3){
	//we are at the root, since we usually have a structure like /app_name/
	selector = "href='/'"
}
else{
	selector = "href*='" + arr_path[arr_path.length-2]+ "'"
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
$('#id_name,#id_code_saq').click(function(){
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
						text: gettext('this wine already exists.')
					})
				)

			}
		}
	});
});

$('#id_code_saq').focusout(function(evt){
	code_to_check = evt.target.value;
	console.log(code_to_check);
	$.ajax({
		url: '../../api/wine?code='+code_to_check,
		cache: false,
		success: function(data){
			if (data.length){
				console.log(data);
				$('#id_code_saq').closest('.form-group').addClass('has-error');
				$('#id_code_saq').parent().append(
					$('<span>',{
						class:'help-block',
						text: gettext('This code already exists.')
					})
				)

			}
		}
	});
});



//====================================
// TypeAhead
//====================================

$('#id_producer').selectize({
	create: true,
	persist: false
});

$('#id_nose_intensity').selectize();
$('#id_persistance').selectize();
$('#id_mouth_intensity').selectize();
$('#id_teint').selectize();


$('#id_aroma').selectize();
$('#id_taste').selectize();
$('#id_acidity').selectize();
$('#id_tanin').selectize();
$('#id_rating').selectize();
$('#id_appelation').selectize({
	create: true,
	persist: false
});

$('#id_region').selectize({
	create:true,
	persist: false
});

$('#id_year').selectize();
$('#id_country').selectize();

$('#id_cepage').selectize({
	maxItems:5,
	create:true,
	persist: false,
	load: function(query, callback){
		if (!query.length) return callback();
        $.ajax({
            url: '../../api/cepage/',
            type: 'GET',
            dataType: 'jsonp',
            error: function() {
                callback();
            },
            success: function(res) {
            	console.log('res',res);
                callback(res);
            }
        });

	}
});

$('#id_tag').selectize({
	valueField: 'tag',
	labelField: 'tag',
	searchField: 'tag',
	create:true,
	persist: false,
	plugins: ['remove_button','restore_on_backspace'],
	maxItems:5,
	render: {
        option: function(item, escape) {
        	type = item.wineType=='w' ? gettext('White'):gettext('Red');

            return '<div>' +
                '<h5>' +
					'<strong>'+item.tag+'</strong> <span class="label label-default">'+escape(type)+'</span>'+
                '</h5>' +
                '<h6>' + 
                	escape(item.description || gettext('No description.')) + 
            	'</h6>' +
            '</div>';
        }
    },
	load: function(query, callback) {
		type = $('#div.id_wineType, input[type=radio]:checked').val() || '';
        if (!query.length) return callback();
        $.ajax({
            url: '../../api/tag/?tag='+ encodeURIComponent(query)+ '&type='+encodeURIComponent(type),
            type: 'GET',
            error: function() {
                callback();
            },
            success: function(res) {
                callback(res);
            }
        });
    }

});

//====================================
// AJAX CONTENT POPULATING
//====================================

var teint = $('#div_id_teint > .controls > .selectize-control > .selectize-input');
elements = $('')
$('[id*=id_wineType_]').change(function(evt){
	console.log('test');
	winetype = '';
	try{
		winetype = String(evt.target.value);
		console.log(winetype);
	}
	catch(e){
		console.log('Exception caught:' + e);
	}

	$.ajax({url: '/api/teint?type=' + winetype,
		cache: false,
		success:function(data){

			arr_teint = $.map(data,function(obj){				
				return obj.teint;
			});
			console.log(arr_teint);
			selected_teint = $(teint).text();
			console.log('selected_teint', selected_teint);
			if ( $.inArray(selected_teint,arr_teint ) > -1 ){

				filtered_options = teint.filter(function(index){
					return $.inArray(teint[index].text, arr_teint) > -1;
				})
			// $('#id_teint').html(filtered_options);
				

			}
			else{
				console.log('no');

			}
		}
	});

});

}); //document ready
