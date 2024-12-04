import React, { useState } from 'react';
import axiosInstance from '../axiosConfig';
import Input from './ui/Input';
import Button from './ui/Button';

const PropertySearch = () => {
    const [city, setCity] = useState('');
    const [street, setStreet] = useState('');
    const [houseNumber, setHouseNumber] = useState('');
    const [apartmentNumber, setApartmentNumber] = useState('');
    const [polygon, setPolygon] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');

    const handleFuzzySearch = () => {
        console.log(`Search query: city=${city}, street=${street}, house_number=${houseNumber}, apartment_number=${apartmentNumber}`);
        axiosInstance.get(`/search/fuzzy_properties/`, {
            params: { city, street, house_number: houseNumber, apartment_number: apartmentNumber }
        })
            .then(response => {
                console.log('Search Results:', response.data);
                const { apartments, houses, lands } = response.data.results;
                setResults([...apartments, ...houses, ...lands]);
                setError('');
            })
            .catch(error => {
                console.error(error);
                setError('An error occurred. Please try again.');
            });
    };

    const handlePolygonSearch = () => {
        try {
            const parsedPolygon = JSON.parse(polygon);
            axiosInstance.post(`/search/within_polygon_properties/`, { polygon: parsedPolygon })
                .then(response => {
                    setResults(response.data.results || []);
                    setError('');
                })
                .catch(error => {
                    console.error(error);
                    setError('An error occurred. Please try again.');
                });
        } catch (e) {
            console.error('Invalid JSON:', e);
            setError('Invalid JSON format. Please enter valid JSON.');
        }
    };

    return (
        <div>
            <h2>Property Search</h2>
            <div>
                <h3>Fuzzy Search</h3>
                <Input type="text" value={city} onChange={(e) => setCity(e.target.value)} placeholder="City" />
                <Input type="text" value={street} onChange={(e) => setStreet(e.target.value)} placeholder="Street" />
                <Input type="text" value={houseNumber} onChange={(e) => setHouseNumber(e.target.value)} placeholder="House Number" />
                <Input type="text" value={apartmentNumber} onChange={(e) => setApartmentNumber(e.target.value)} placeholder="Apartment Number" />
                <Button onClick={handleFuzzySearch}>Search</Button>
            </div>
            <div>
                <h3>Polygon Search</h3>
                <Input type="text" value={polygon} onChange={(e) => setPolygon(e.target.value)} placeholder='Enter polygon coordinates as JSON, e.g. [[30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]]' />
                <Button onClick={handlePolygonSearch}>Search</Button>
            </div>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <div>
                <h3>Results</h3>
                <ul>
                    {Array.isArray(results) && results.map((property, index) => (
                        <li key={index}>{JSON.stringify(property)}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default PropertySearch;