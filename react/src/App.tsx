import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home';
import ClientFormPage from './components/pages/ClientFormPage';
import RealtorFormPage from './components/pages/RealtorFormPage';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/client-form" element={<ClientFormPage />} />
                <Route path="/realtor-form" element={<RealtorFormPage />} />
            </Routes>
        </Router>
    );
};

export default App;