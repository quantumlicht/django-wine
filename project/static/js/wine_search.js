// this is the id of the submit button
search_fields = $("#wine_search > .input-group > .input-group-btn > ul >li> a");

search_fields.click(function(evt){
   query_field = $(this).attr('id');
   query = $('#query').val();
   var url = "../../api/wine/?"+query_field+'='+encodeURIComponent(query); // the script where you handle the form input.
   var jsonData ;
   $.ajax({
      type: "GET",
      url: url,
      dataType: 'json',
      complete: function(data){
         console.log(data.responseJSON);
      }
   });

});
