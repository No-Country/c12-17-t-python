import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css'

function Inicio() {

  return (
  <React.Fragment>
    <p style="text-color:black">Hola que pasa chavales</p>
    <h1>HOLA MUNDO desde react</h1>
    
   </React.Fragment>
  );
}

Inicio()

const domcCon = document.querySelector('#react_container')

ReactDOM.render(<Inicio/>, domcCon)
//export default Inicio;
