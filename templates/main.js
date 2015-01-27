$('.modalClick').on('click', function(event){
      	
      	event.preventDefault();
      	/*   Gives overlay effect and the attributes give it the specifics of where and what to do on the fade in   */
      	$('#overlay')
      		.fadeIn()
      		.find('#modal')
      		.fadeIn();
      });
      /*   returns the fadeout specifics for the overlay or modal   */
      $('.close').on('click', function(event){
      	event.preventDefault();
      	$('#overlay')
      		.fadeOut()
      		.find('#modal')
      		.fadeOut();
      });
      /*   End modal jQuery   */
  
  })
  
  