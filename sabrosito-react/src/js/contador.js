const contador = document.getElementById("contar")
const sumar = document.getElementById("incre")
const restar = document.getElementById("decre")


let numero = 0

sumar.addEventListener("click", ()=>{
    numero++
    contador.innerHTML = numero
})

restar.addEventListener("click", ()=>{
    
    if(numero == 0)
    {

    }
    else{
        numero--
        contador.innerHTML = numero
    }
    
    
})
