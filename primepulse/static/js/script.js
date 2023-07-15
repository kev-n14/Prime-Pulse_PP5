$(document).ready(function() {
	
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if

    
}); 

setTimeout(function () {
    $('#message').fadeOut('slow')
}, 4000)