const miFormulario = document.getElementById('miFormulario');
const miEnlace = document.getElementById('btnE');

function enviarFormulario(event) {
  if (!miFormulario.checkValidity()) {
    event.preventDefault(); // Evitar que el enlace funcione si el formulario no está completo
  }
}

miFormulario.addEventListener('input', function() {
  if (miFormulario.checkValidity()) {
    miEnlace.removeAttribute('btnEnviar');
  } else {
    miEnlace.setAttribute('btnEnviar', 'btnEnviar');
  }
});
