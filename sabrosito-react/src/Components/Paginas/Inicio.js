import React from 'react';
import './App.css'
import GooglePlacesAutocomplete from 'react-google-autocomplete'
import {useState, useEffect} from 'react'
import { Routes, Route } from 'react-router';
import Menu from './Menu.js'
import Login from './Login.js'
import Header from './ui/Header.js'
import Footer from './ui/Footer.js'
import Top from './ui/Top.js'

// Componente de autocompletado de ubicación
const LocationInput = () => {
  const handlePlaceSelect = (place) => {
    // Obtén la ubicación seleccionada
    const { geometry, formatted_address } = place;
    const { lat, lng } = geometry.location;

    // Haz algo con la ubicación seleccionada
    console.log('Ubicación seleccionada:', lat(), lng(), formatted_address);
  };

  return (
    <input type="text" placeholder="Selecciona tu ubicación" onChange={handlePlaceSelect} />
  );
};

function Inicio() {




  return (
  <>

    <div className="app">
    <Header/>
    <Top/>
      <section className="banner">
        <div className="banner-content">
          <h2>Título del banner</h2>
          <p>Texto del banner</p>
          <div className="banner-buttons">
            <button>Botón 1</button>
            <button>Botón 2</button>
          </div>
        </div>
        <img className='imagen' alt="Imagen del banner" />
      </section>
      <section className="ofertas">
        <h2>Ofertas</h2>
        <div className="oferta-container">
          <img src="" alt="Imagen de la oferta" />
          <div className="oferta-details">
            <h3>Título de la oferta</h3>
            <p>Descripción de la oferta</p>
          </div>
        </div>
        </section>
        <Footer/>
    </div>

   </>
  );
}

export default Inicio;
