import React from 'react';
import '.././App.css'
import {useState, useEffect} from 'react'
import Menu from '.././Menu.js'
import Login from '.././Login.js'
import { Routes, Route } from 'react-router';
import { Link, NavLink } from "react-router-dom";


const Top = () => {

    const [logeado, setLogeado] = useState(false)
  return (
    <>
    <header className="header">
        <div className="logo">Logo</div>
        <div className="location">Ubicación</div>
        <nav className="menu">
          <ul>
            <li><a href="#">Menu</a></li>
            <li>
                <a href="#">
                    {/* Aca dependiendo del estado si esta logeado o no carga una opcion */}
                    {logeado ? (<p>User</p>) : (<p>Registrarse</p>)}
                </a>
            </li>

          </ul>
          <div className="cart-icon"><i className="fa fa-shopping-cart"></i></div>

          <NavLink exact='true' to='/menu' style={({ isActive, isPending }) => {return {
                                                    color: isPending ? "red" : "white",
                                                    background: isActive ? "#ffbb0e":""};}}
                                className='p-1 text-gray-400 block hover:bg-yellow-500 hover:text-gray-900' >Menu</NavLink>
                    <NavLink exact='true' to='/login' style={({ isActive, isPending }) => {return {
                                                    color: isPending ? "red" : "white",
                                                    background: isActive ? "#ffbb0e":""};}}
                                className='p-1 text-gray-400 block hover:bg-yellow-500 hover:text-gray-900'>Login</NavLink>
        </nav>
      </header>
    </>
  );
}

export default Top;
