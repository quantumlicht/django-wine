$('input,select').attr('class','form-control')
// console.log(JSON.parse($('#id_hidden_field').attr('data')));
$('#id_wineType').change(function(evt){console.log(evt.target.value);});