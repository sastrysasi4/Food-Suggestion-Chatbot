import React, { useState, useEffect } from 'react';
import menuData from "../food_items.json";

const Menu = () => {
    const [menuItems, setMenuItems] = useState({});

    useEffect(() => {
        // Load the menu data from the JSON file
        setMenuItems(menuData.menu);
    }, []);

    return (
        <div>
            <h1>Menu</h1>
            {Object.keys(menuItems).map((category) => (
                <div key={category}>
                    <h2>{category}</h2>
                    <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                        {menuItems[category].map((item, index) => (
                            <div key={index} style={cardStyle}>
                                <h3>{item.name}</h3>
                                <p>{item.description}</p>
                            </div>
                        ))}
                    </div>
                </div>
            ))}
        </div>
    );
};

// Simple card style
const cardStyle = {
    border: '1px solid #ddd',
    borderRadius: '4px',
    padding: '10px',
    margin: '10px',
    width: '200px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)'
};

export default Menu;
