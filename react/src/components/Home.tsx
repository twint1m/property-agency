import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div>
            <h1>Real Estate Agency</h1>
            <ul>
                <li><Link to="/client-form">Client Form</Link></li>
                {/* Добавьте здесь ссылки на другие формы */}
            </ul>
        </div>
    );
};

export default Home;