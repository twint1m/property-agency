import { useState } from 'react';
import axiosInstance from '../axiosConfig';
import Input from './ui/Input';
import Button from './ui/Button';

const FuzzySearch = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState({ clients: [], realtors: [] });
    const [error, setError] = useState('');

    const handleChange = (e) => {
        setQuery(e.target.value);
    };

    const handleSearch = () => {
        if (!query) {
            setError('Search query cannot be empty.');
            return;
        }

        axiosInstance.get(`/fuzzy_search/?query=${query}`, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                setResults(response.data);
                setError('');
                console.log('Search Results:', response.data);
            })
            .catch(error => {
                console.error(error);
                setError('An error occurred. Please try again.');
            });
    };

    return (
        <div>
            <h2>Fuzzy Search</h2>
            <Input type="text" value={query} onChange={handleChange} placeholder="Enter name" />
            <Button onClick={handleSearch}>Search</Button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <div>
                <h3>Clients</h3>
                <ul>
                    {results.clients.map(client => (
                        <li key={client.id}>{client.first_name} {client.last_name} {client.middle_name}</li>
                    ))}
                </ul>
                <h3>Realtors</h3>
                <ul>
                    {results.realtors.map(realtor => (
                        <li key={realtor.id}>{realtor.first_name} {realtor.last_name} {realtor.middle_name}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default FuzzySearch;