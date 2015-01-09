$(document).ready(function() {
	$('.kitchen').click(function() {
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

	$('.menu').click(function() {
		var menu = $(this).attr('id');
		$(this).addClass('active');
		$(this).siblings().removeClass('active');

		$.ajax({
			type: "POST",
			url: "/change_menu/",
			data: {menu_type: menu},
			dataType: "json",
			success: function(data){
				//change menu items
			}
		})

	});
});