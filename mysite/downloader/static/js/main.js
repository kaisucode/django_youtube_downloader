
window.onload = function (){

	var shouldPauseEnter;
	shouldPauseEnter = {{ shouldPauseEnter }}
	document.addEventListener("keydown", function onEvent(event) {
		if (shouldPauseEnter)
			return;

		if (event.which === 13){
			shouldPauseEnter = true;
		}

	});

};


