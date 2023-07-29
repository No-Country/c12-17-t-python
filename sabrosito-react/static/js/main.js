const openModalCarrito = document.querySelector(".container-icon")
const modalCarrito = document.querySelector(".modal_carrito")
const closeModalCarrito = document.querySelector(".modal__close__carrito")


openModalCarrito.addEventListener('click', (e)=>{
    console.log("Hola mundo")
    e.preventDefault()
    modalCarrito.classList.add("modal__carrito--show")
})

closeModalCarrito.addEventListener('click', (e)=>{
    e.preventDefault()
    modalCarrito.classList.remove("modal__carrito--show")
})