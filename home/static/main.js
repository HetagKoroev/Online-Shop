document.querySelectorAll('.service-item').forEach(service => {
	service.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
		    try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
			if(category.dataset.service === service.dataset.myid) {
				category.classList.add('show')
				try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
			} else {
			        try{document.getElementById(category.id).checked = false} catch (e) {console.log(e)}
                     category.classList.remove('show')
                     document.querySelectorAll('.product-item').forEach(product => {
                     product.classList.remove('show')
                     })
			       }
		})
	})
})


document.querySelectorAll('.category-item').forEach(category => {
	category.addEventListener('click', (e) => {
		document.querySelector('.products').classList.add('show')
		document.querySelectorAll('.product-item').forEach(product => {
			if(product.dataset.category === category.dataset.myid && category.dataset.service === product.dataset.service) {

				product.classList.add('show')
			} else {
			        product.classList.remove('show')
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