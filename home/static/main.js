document.querySelectorAll('.service-item').forEach(service => {
	service.addEventListener('click', (e) => {
		document.querySelector('.categories').classList.add('show')
		document.querySelectorAll('.category-item').forEach(category => {
		    console.log(category.dataset.service)
		    console.log(service.dataset.myid)
			if(category.dataset.service === service.dataset.myid) {
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
			if(product.dataset.category === category.dataset.myid && category.dataset.service === product.dataset.service) {
				product.classList.add('show')
			} else {
			        product.classList.remove('show')
			       }
		})
	})
})
