import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div>
            <h1>Real Estate Agency</h1>
            <ul>
                <li><Link to="/client-form">Client Form</Link></li>
                <li><Link to="/realtor-form">Realtor Form</Link></li>
            </ul>
        </div>
    );
};

export default Home;