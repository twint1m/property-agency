import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import ClientFormPage from './components/pages/ClientFormPage';
import RealtorFormPage from './components/pages/RealtorFormPage';
import FuzzySearch from './components/FuzzySearch';
import PropertyFormPage from './components/pages/PropertyFormPage';
import PropertySearchPage from './components/pages/PropertySearchPage';
import OfferFormPage from './components/pages/OfferFormPage';
import NeedFormPage from './components/pages/NeedFormPage';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/client-form" element={<ClientFormPage />} />
                <Route path="/realtor-form" element={<RealtorFormPage />} />
                <Route path="/fuzzy-search" element={<FuzzySearch />} />
                <Route path="/property-form" element={<PropertyFormPage />} />
                <Route path="/property-search" element={<PropertySearchPage />} />
                <Route path="/offer-form" element={<OfferFormPage />} />
                <Route path="/need-form" element={<NeedFormPage />} />
            </Routes>
        </Router>
    );
};

export default App;