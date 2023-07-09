import React from "react";
import "./Menu.css";
import Top from './ui/Top.js'
import Header from './ui/Header.js'
const Menu = () => {
  return (
    <div className="menu-container">

      {/* Top Bar */}
      <Header/>
      <Top/>

      {/* Título */}
      <h1 className="menu-title">Menús</h1>

      {/* Opciones de menú */}
      <div className="image-container">
        {/* Opción 1 */}
        <div className="image-container">
          <img   alt="Desayunos" className='img'/>
          <h2>Desayunos</h2>
        </div>

        {/* Opción 2 */}
        <div className="image-container">
          <img  alt="Comidas" className='img'/>
          <h2>Comidas</h2>
        </div>

        {/* Opción 3 */}
        <div className="image-container">
          <img  alt="Bebidas" className='img'/>
          <h2>Bebidas</h2>
        </div>
      </div>
      <footer className="footer">
        Pie de página
      </footer>
    </div>
  );
};

export default Menu;
