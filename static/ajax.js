
$(function(){
	$('#search').keyup(function() {
		$.ajax({
			type: "POST",
			url: "/posts/search/",
			data: {
				'search_text': $('#search').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
			},
			success: searchSuccess,
			dataType: 'html',
		});
	});
})

function searchSuccess(data, textStatus, jqXHR){
	console.log(data)
	$('#search-results').html(data);
}