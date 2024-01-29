import React from 'react';
import './styles.css'; // Import the CSS file

const Welcomepage = () => {
    return (
        <div style={{ display:"flex", alignItems:"center", justifyContent:"center"}}>
            <p className="welcome-message">
                <h1 style={{fontFamily:"sans-serif"}}>Welcome to the Food Suggestion ChatBot.</h1> 
                <p style={{fontSize:"24px", fontFamily:"sans-serif"}}>The menu button displays dishes. The chatbot will aid you in choosing your dish.</p>
            </p>

        </div>
    );
};

export default Welcomepage;
