import React from 'react';
import './Menu.css';
import Header from './ui/Header.js'
import Footer from './ui/Footer.js'
import { Link, NavLink } from "react-router-dom";

const Login = () => {
  return (
  <div className="app">
    <div className="container">
      <Header/>
      <div className="content">
         <NavLink exact='true' to='/' style={({ isActive, isPending }) => {return {
                                                    color: isPending ? "red" : "purple",
                                                    background: isActive ? "#ffbb0e":""};}}
                                className='p-1 text-gray-400 block hover:bg-yellow-500 hover:text-gray-900' >Volver</NavLink>
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
        <Footer/>
    </div>
    </div>
  );
}

export default Login;
