import React from 'react';
import '../App.css'

const Header = () => {
  return (
    <>
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
    </>
  );
}

export default Header;
