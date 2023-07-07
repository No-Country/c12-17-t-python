import React from 'react';
import './App.css'
import GooglePlacesAutocomplete from 'react-google-autocomplete'
import {useState, useEffect} from 'react'
import Menu from './Components/Paginas/Menu.js'


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

function App() {

  const [logeado, setLogeado] = useState(false)


  return (
    <div className="app">
      <div className="top-bar">
        <div className="contact-info">
          <span>Correo: ejemplo@correo.com</span>
          <span>Teléfono: 123-456-7890</span>
        </div>
        <div className="social-media-icons">
          <a href="#"><i className="fa fa-facebook"></i></a>
          <a href="#"><i className="fa fa-twitter"></i></a>
          <a href="#"><i className="fa fa-instagram"></i></a>
        </div>
      </div>
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
        </nav>
      </header>
      <section className="banner">
        <div className="banner-content">
          <h2>Título del banner</h2>
          <p>Texto del banner</p>
          <div className="banner-buttons">
            <button>Botón 1</button>
            <button>Botón 2</button>
          </div>
        </div>
        <img src="imagen-banner.jpg" alt="Imagen del banner" />
      </section>
      <section className="ofertas">
        <h2>Ofertas</h2>
        <div className="oferta-container">
          <img src="imagen-oferta.jpg" alt="Imagen de la oferta" />
          <div className="oferta-details">
            <h3>Título de la oferta</h3>
            <p>Descripción de la oferta</p>
          </div>
        </div>
      </section>
      <footer className="footer">
        Pie de página
      </footer>
    </div>
  );
}

export default App;
