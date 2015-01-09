$(document).ready(function() {
	$('button').click(function() {
		console.log($(this).siblings());
		var id = $(this).siblings().attr('id');
		$(this).siblings().remove();
		this.remove();

		$.ajax({
			type: "POST",
			url: "/delete_order/",
			data: {orderId: id},
			dataType: "json"
		})

	});
});