
document.querySelectorAll('.service-item').forEach(service => {
	service.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
			if(category.dataset.id === '1' && service.dataset.id === '1') {
				category.classList.add('show')
			}
		})
	})
})


document.querySelectorAll('.category-item').forEach(category => {
	category.addEventListener('click', (e) => {
		document.querySelector('.products').classList.add('show')
		document.querySelectorAll('.product-item').forEach(product => {
			if(product.dataset.id === '1' && category.dataset.id === '1') {
				product.classList.add('show')
			}
		})
	})
})