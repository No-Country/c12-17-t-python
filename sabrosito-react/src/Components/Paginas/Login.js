import React from 'react';
import './Menu.css';

const Login = () => {
  return (
    <div className="container">
      <div className="top-bar">
        {/* Aquí va el contenido de la barra superior */}
      </div>
      <div className="content">
        <button className="volver-button">Volver</button>
        <div className="image">
          {/* Aquí va la imagen */}
        </div>
        <form className="formulario">
          <h1 className="titulo">Bienvenido</h1>
          <p className="texto">Estamos felices de tenerte aquí</p>
          <h2 className="subtitulo">Iniciar sesión</h2>
          <h3 className="campo-titulo">Correo electrónico</h3>
          <input type="email" className="campo" />
          <h3 className="campo-titulo">Contraseña</h3>
          <input type="password" className="campo" />
          <button className="boton">Iniciar sesión</button>
          <p className="texto-registro">¿Aún no estás registrado? Regístrate</p>
        </form>
      </div>
      <footer className="footer">
        {/* Aquí va el contenido del pie de página */}
      </footer>
    </div>
  );
}

export default Login;
