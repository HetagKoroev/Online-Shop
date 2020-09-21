console.log('000')
document.querySelectorAll('.service-item').forEach(service => {
	service.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
			if(category.dataset.myid === service.dataset.myid) {
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
		console.log(product.dataset.category)
		console.log(category.dataset.myid)
			if(product.dataset.category === category.dataset.myid) {
				product.classList.add('show')
			} else {
			        product.classList.remove('show')
			       }
		})
	})
})