function convertirSpanAInput(event) {
  event.preventDefault(); // Evitar el envío del formulario por defecto

  // Obtener el elemento span
  var miSpan = document.getElementById("miSpan");

  // Crear un nuevo elemento input de tipo "number"
  var miInput = document.createElement("input");
  miInput.type = "number";

  // Obtener el texto del span y convertirlo a un número
  var numeroSpan = parseInt(miSpan.innerText);

  // Establecer el valor y el nombre del input
  miInput.value = numeroSpan;
  miInput.name = "cantidad"; // Agregamos el atributo name al input

  // Reemplazar el span con el input
  miSpan.parentNode.replaceChild(miInput, miSpan);

  // Enviar el formulario después de la conversión
  event.target.submit();
}
