import React, { StrictMode } from 'react';
import ReactDOM from 'react-dom/client';
import { createRoot } from 'react-dom/client'
import './App.css'
import Inicio from './Inicio';

const rootElement = document.getElementById("#react_container");
const root = createRoot(rootElement);

root.render(
  <React.StrictMode>
    <Inicio/>
  </React.StrictMode>
)


/*
function Inicio() {

  return (
  <React.Fragment>
    <p style="text-color:black">Hola que pasa chavales</p>
    <h1>HOLA MUNDO desde react</h1>
    
   </React.Fragment>
  );
}

Inicio()
*/


//createRoot(document.getElementById('react_container')).render(<Inicio/>)

const domcCon = document.querySelector('#react_container')
//ReactDOM.render(<Inicio/>, domcCon)
//export default Inicio;
