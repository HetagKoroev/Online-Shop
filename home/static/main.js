
document.querySelectorAll('.service-item').forEach(service => {
	service.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
			if(category.dataset.id === service.dataset.id) {
				category.classList.add('show')
			} else {
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
			if(product.dataset.id === category.dataset.id) {
				product.classList.add('show')
			} else {
			        product.classList.remove('show')
			       }
		})
	})
})