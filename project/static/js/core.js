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
	plugins: ['remove_button','restore_on_backspace']
});

$('#id_tag').selectize({
	maxItems:5,
	create:true,
	persist: false,
	// plugins: ['remove_button','restore_on_backspace'],
	// render: {
 //        option: function(item, escape) {
 //            var actors = [];
 //            for (var i = 0, n = item.abridged_cast.length; i < n; i++) {
 //                actors.push('<span>' + escape(item.abridged_cast[i].name) + '</span>');
 //            }

 //            return '<div>' +
 //                '<img src="' + escape(item.posters.thumbnail) + '" alt="">' +
 //                '<span class="title">' +
 //                    '<span class="name">' + escape(item.title) + '</span>' +
 //                '</span>' +
 //                '<span class="description">' + escape(item.synopsis || 'No synopsis available at this time.') + '</span>' +
 //                '<span class="actors">' + (actors.length ? 'Starring ' + actors.join(', ') : 'Actors unavailable') + '</span>' +
 //            '</div>';
 //        }
 //    },
	load: function(query, callback){
		if (!query.length) return callback();
        $.ajax({
            url: '../../api/tag',
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

//====================================
// AJAX CONTENT POPULATING
//====================================

var teint = $('#id_teint option');
$('#id_wineType').change(function(evt){
	winetype = '';
	try{
		winetype = String(evt.target.value);
	}
	catch(e){
		console.log('Exception caught:' + e);
	}

	$.ajax({url: '/api/teint?type=' + winetype,
		cache: false,
		success:function(data){
			arr =[];

			filtered_data = data.filter(function(obj){				
				arr.push(obj.teint);
			});
			
			filtered_options = teint.filter(function(index){
				return $.inArray(teint[index].text, arr) > -1;
			})
			$('#id_teint').html(filtered_options);
		}
	});
});

}); //document ready
