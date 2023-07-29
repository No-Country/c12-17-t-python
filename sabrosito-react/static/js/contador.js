const contador = document.getElementById("contar");
const sumar = document.getElementById("incre");
const restar = document.getElementById("decre");
const inputHidden = document.getElementById("inputHidden");

let numero = 0;

sumar.addEventListener("click", () => {
  numero++;
  contador.innerHTML = numero;
});

restar.addEventListener("click", () => {
  if (numero === 0) {
    // No se permite decrementar más allá de cero
  } else {
    numero--;
    contador.innerHTML = numero;
  }
});

function convertirSpanAInput(event) {
  event.preventDefault(); // Evitar el envío del formulario por defecto

  // Obtener el valor actual del span
  var valorSpan = parseInt(contador.innerHTML);

  // Crear un nuevo elemento input de tipo "number"
  var miInput = document.createElement("input");
  miInput.type = "number";
  miInput.name = "cantidad";
  miInput.value = valorSpan;

  // Reemplazar el span con el input
  contador.parentNode.replaceChild(miInput, contador);

  // Establecer el valor del campo oculto antes de enviar el formulario
  inputHidden.value = valorSpan;

  // Enviar el formulario automáticamente
  event.target.submit();
}
