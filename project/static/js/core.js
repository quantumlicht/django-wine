$(document).ready(function(){
	
function capitalize(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
}

//====================================
// ACTIVE NAVBAR SELECTOR
//====================================

arr_path = location.pathname.split('/');
// console.log('arr_path',arr_path);
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
// ADDING BOOTSTRAP CLASSES
//====================================

$('input,select').attr('class','form-control');

//====================================
// DATE PICKER
//====================================


// fetching userLang from hidden injection in base template
userLang = $('#lang_code').text();

// empty string is english locale by default
userLang = userLang=='en'?'':userLang;

$('#id_date').datepicker(
	$.datepicker.regional[ userLang ]
);
$('#id_date').datepicker('option','dateFormat','yy-mm-dd');
//====================================
// WINE EXISTANCE CHECK
//====================================

$('#id_name,#id_code_saq').click(function(){
	$(this).parent().find('.help-block').hide();
	$(this).closest('.form-group').removeClass('has-error');
});

$('#id_name').focusout(function(evt){
	name_to_check = evt.target.value;
	// console.log(name_to_check);
	$.ajax({
		url: '../../api/wine?name='+name_to_check,
		cache: false,
		success: function(data){
			if (data.length){
				// console.log(data);
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
	// console.log(code_to_check);
	$.ajax({
		url: '../../api/wine?code_saq='+code_to_check,
		cache: false,
		success: function(data){
			if (data.length){
				// console.log(data);
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

$('#id_nose_intensity').selectize();
$('#id_persistance').selectize();
$('#id_mouth_intensity').selectize();


$('#id_aroma').selectize();
$('#id_taste').selectize();
$('#id_acidity').selectize();
$('#id_tanin').selectize();
$('#id_rating').selectize();
$('#id_year').selectize();

var xhr;
var $select_teint = $('#id_teint').selectize({
	valueField: 'teint',
	labelField: 'teint',
	searchField: 'teint',
	loadThrottle: 100
});
var select_teint = $select_teint[0].selectize;
var select_country, $select_country;
var select_region, $select_region;
var select_appelation, $select_appelation;
var select_producer, $select_producer;

$select_country = $('#id_country').selectize({
	//value is the region
    onChange: function(value) {
        if (!value.length) return;
        select_appelation.disable();
        select_appelation.clearOptions();
        select_appelation.load(function(callback) {
            xhr && xhr.abort();
            xhr = $.ajax({
            	async: false,
                url: '../../api/appelation/?country=' + value,
                success: function(results) {
                    select_appelation.enable();
                    callback(results);
                },
                error: function() {
                    callback();
                }
            })
        });
        select_region.disable();
        select_region.clearOptions();
        select_region.load(function(callback) {
            xhr && xhr.abort();
            xhr = $.ajax({
            	async: false,
                url: '../../api/region/?country=' + value,
                success: function(results) {
                    select_region.enable();
                    callback(results);
                },
                error: function() {
                    callback();
                }
            })
        });
        select_producer.disable();
        select_producer.clearOptions();
        select_producer.load(function(callback) {
            xhr && xhr.abort();
            xhr = $.ajax({
            	async: false,
                url: '../../api/producer/?country=' + value,
                success: function(results) {
                    select_producer.enable();
                    callback(results);
                },
                error: function() {
                    callback();
                }
            })
        });
    }
});

$select_region = $('#id_region').selectize({
	preload: true,
    valueField: 'region',
    labelField: 'region',
    searchField: ['region']
});

$select_appelation = $('#id_appelation').selectize({
	preload: true,
	create: true,
    valueField: 'appelation',
    labelField: 'appelation',
    searchField: ['appelation']
});

$select_producer = $('#id_producer').selectize({
	preload: true,
	create: true,
    valueField: 'producer',
    labelField: 'producer',
    searchField: ['producer']
});


select_region  = $select_region[0].selectize;
select_appelation  = $select_appelation[0].selectize;
select_country = $select_country[0].selectize;
select_producer = $select_producer[0].selectize;

select_region.disable();
select_appelation.disable();
select_producer.disable();




var $select_cepage = $('#id_cepage').selectize({
	valueField: 'cepage',
	labelField: 'cepage',
	searchField: 'cepage',
	create:true,
	persist: false,
	loadThrottle: 100,
	plugins: ['remove_button','restore_on_backspace'],
	maxItems:5,
	render: {
        option: function(item, escape) {
        	console.log(item);
        	type = item.wineType=='w' ? gettext('White'):gettext('Red');

            return '<div>' +
                '<h5>' +
					'<strong>'+item.cepage+'</strong> <span class="label label-default">'+escape(type)+'</span>'+
                '</h5>' +
            '</div>';
        }
    },
	load: function(query, callback) {
		type = $('#div.id_wineType, input[type=radio]:checked').val() || '';
        if (!query.length) return callback();
        $.ajax({
        	cache: false,
            url: '../../api/cepage/?cepage='+ encodeURIComponent(query)+ '&type='+encodeURIComponent(type),
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

var $select_tag = $('#id_tag').selectize({
	valueField: 'tag',
	labelField: 'tag',
	searchField: 'tag',
	loadThrottle: 100,
	create:true,
	persist: false,
	plugins: ['remove_button','restore_on_backspace'],
	maxItems:5,
	render: {
        option: function(item, escape) {
        	console.log(item);
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
		// $(this).clearOptions();/**/
		type = $('#div.id_wineType, input[type=radio]:checked').val() || '';
        if (!query.length) return callback();
        $.ajax({
        	cache: false,
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
	var winetype = '';
	try{
		winetype = String(evt.target.value);
	}
	catch(e){
		console.log('Exception caught:' + e);
	}

	var select_tag = $select_tag[0].selectize;
	var select_cepage =  $select_tag[0].selectize;
	select_tag.clearOptions();
	select_cepage.clearOptions();
	select_teint.clearOptions();
	select_teint.load(function(callback) {
        xhr && xhr.abort();
        xhr = $.ajax({
        	async: false,
            url: '../../api/teint/?type=' + winetype,
            success: function(results) {
                callback(results);
            },
            error: function() {
                callback();
            }
        });
    });
});

}); //document ready
