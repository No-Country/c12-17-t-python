import React from "react";
import "./Menu.css";

const Menu = () => {
  return (
    <div className="menu-container">
      {/* Top Bar */}
      <div className="top-bar">
        {/* Contenido de la barra superior */}
      </div>

      {/* Título */}
      <h1 className="menu-title">Menús</h1>

      {/* Opciones de menú */}
      <div className="menu-options">
        {/* Opción 1 */}
        <div className="menu-option">
          <img src="ruta-de-la-imagen-desayunos" alt="Desayunos" />
          <h2>Desayunos</h2>
        </div>

        {/* Opción 2 */}
        <div className="menu-option">
          <img src="ruta-de-la-imagen-comidas" alt="Comidas" />
          <h2>Comidas</h2>
        </div>

        {/* Opción 3 */}
        <div className="menu-option">
          <img src="ruta-de-la-imagen-bebidas" alt="Bebidas" />
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
