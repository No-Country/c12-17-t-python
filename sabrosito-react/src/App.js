import React from 'react';
import './App.css'
import GooglePlacesAutocomplete from 'react-google-autocomplete'
import {useState, useEffect} from 'react'
import { Routes, Route } from 'react-router';
import Menu from './Components/Paginas/Menu.js'
import Login from './Components/Paginas/Login.js'
import Inicio from './Components/Paginas/Inicio.js'


const App = ()=>{
  return (
    <>
         <Routes>
            <Route path='/' element={<Inicio />} />
            <Route path='/menu' element={<Menu />} />
            <Route path='/login' element={<Login />} />
          </Routes>
    </>
  );
}

export default App;
