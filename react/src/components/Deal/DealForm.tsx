import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig';

const DealForm = ({ dealId, onSubmit }) => {
    const [needs, setNeeds] = useState([]);
    const [offers, setOffers] = useState([]);
    const [selectedNeed, setSelectedNeed] = useState('');
    const [selectedOffer, setSelectedOffer] = useState('');

    useEffect(() => {
        axiosInstance.get('/needs/')
            .then(response => setNeeds(response.data))
            .catch(error => console.error('Error fetching needs:', error));

        axiosInstance.get('/offers/')
            .then(response => setOffers(response.data))
            .catch(error => console.error('Error fetching offers:', error));

        if (dealId) {
            axiosInstance.get(`/deals/${dealId}/`)
                .then(response => {
                    setSelectedNeed(response.data.need);
                    setSelectedOffer(response.data.offer);
                })
                .catch(error => console.error('Error fetching deal:', error));
        }
    }, [dealId]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = { need: selectedNeed, offer: selectedOffer };
        axiosInstance.post('/deals/', data)
            .then(response => {
                onSubmit(response.data);
            })
            .catch(error => {
                console.error('Error creating deal:', error);
                alert('An error occurred. Please try again.');
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Need:</label>
                <select value={selectedNeed} onChange={(e) => setSelectedNeed(e.target.value)}>
                    <option value="">Select Need</option>
                    {needs.map(need => (
                        <option key={need.id} value={need.id}>{need.address}</option>
                    ))}
                </select>
            </div>
            <div>
                <label>Offer:</label>
                <select value={selectedOffer} onChange={(e) => setSelectedOffer(e.target.value)}>
                    <option value="">Select Offer</option>
                    {offers.map(offer => (
                        <option key={offer.id} value={offer.id}>{offer.description}</option>
                    ))}
                </select>
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default DealForm;