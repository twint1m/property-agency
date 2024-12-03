import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div>
            <h1>Home</h1>
            <nav>
                <ul>
                    <li><Link to="/client-form">Client Form</Link></li>
                    <li><Link to="/realtor-form">Realtor Form</Link></li>
                    <li><Link to="/fuzzy-search">Fuzzy Search</Link></li>
                    <li><Link to="/property-form">Property Form</Link></li>
                </ul>
            </nav>
        </div>
    );
};

export default Home;