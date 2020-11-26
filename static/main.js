document.querySelectorAll('.platform-item').forEach(platform => {
	platform.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
		    try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
			if(category.dataset.platform === platform.dataset.myid) {
				category.classList.add('show')
				try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
			} else {
			        try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
                     category.classList.remove('show')
                     document.querySelectorAll('.service-item').forEach(service => {
                     service.classList.remove('show')
                     })
			       }
		})
	})
})


document.querySelectorAll('.category-item').forEach(category => {
	category.addEventListener('click', (e) => {
		document.querySelector('.services').classList.add('show')
		document.querySelectorAll('.service-item').forEach(service => {
			if(service.dataset.category === category.dataset.myid && category.dataset.platform === service.dataset.platform) {

				service.classList.add('show')
			} else {
			        service.classList.remove('show')
			       }
		})
	})
})

if (document.querySelector('.change-theme').checked === true) {
	document.body.classList.add('light');
} else {
	document.body.classList.add('dark');
}

document.querySelector('.change-theme').addEventListener('click' , (e) => {
	if(e.target.checked === true) {
		document.body.classList.add('light');
		document.body.classList.remove('dark');
		return;
	}
	document.body.classList.add('dark');
	document.body.classList.remove('light');
})