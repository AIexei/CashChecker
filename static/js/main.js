$(document).ready(function() {
	$('.have-account a').click(function(){
		if ($('div#logindiv').hasClass('hidden')) {
			$('div#logindiv').removeClass('hidden');
			$('div#registerdiv').addClass('hidden');
		} else {
			$('div#registerdiv').removeClass('hidden');
			$('div#logindiv').addClass('hidden');
		}
	});
});