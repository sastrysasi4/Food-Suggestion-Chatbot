import React from 'react';
import './styles.css'; // Import the CSS file
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="headerStyle">
      <div className="logoStyle">Food Suggestion Chatbot</div>
      <nav className="navStyle">
        <li className="navItemStyle"><Link to="/Home">HOME</Link></li>
        <li className="navItemStyle"><Link to="/Menu">MENU</Link></li>
        <li className="navItemStyle"><Link to="/Chatbot">CHATBOT</Link></li>
        {/* Repeat for other nav items */}
      </nav>
    </header>
  );
};

export default Header;
