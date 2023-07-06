import React from 'react';
import './App.css'
import GooglePlacesAutocomplete from 'react-google-autocomplete'

// Componente de la barra superior
const TopBar = () => {
  return (
    <div className="top-bar">
      <div className="icon">Icono</div>
      <div className="location-bar">
        {/* Componente de selección de ubicación */}
        <LocationInput />
      </div>
      <div className="buttons">
        <button>Menu</button>
        <button>Ingresar</button>
        <button><i className="fas fa-shopping-cart"></i></button>
      </div>
    </div>
  );
};

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

// Componente del banner
const Banner = () => {
  return (
    <div className="banner">

      <h2>Texto del banner</h2>
      <button>Botón</button>
    </div>
  );
};

// Componente de la sección de ofertas
const OffersSection = () => {
  return (
  <>
    <h1>Ofertas</h1>
    <div className="offers-section">

      {/* Contenido de la sección de ofertas */}
    </div>
    </>
  );
};

// Componente del pie de página
const Footer = () => {
  return (
    <footer>
      <p>Todos los derechos reservados &copy; 2023</p>
    </footer>
  );
};

// Componente principal de la página
const App = () => {
  return (
    <div>
      <TopBar />
      <Banner />
      <OffersSection />
      <Footer />
    </div>
  );
};

export default App;
