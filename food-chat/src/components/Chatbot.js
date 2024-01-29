import React from 'react';
import './ChatInterface.css'; // Import the CSS file for styling

function ChatInterface() {
  return (
    <div className="streamlit-iframe-container">
      <iframe
        src="http://localhost:8501/"
        title="Streamlit App"
        className="fullscreen-iframe"
      ></iframe>
    </div>
  );
}

export default ChatInterface;
