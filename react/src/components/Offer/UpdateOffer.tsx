import React, { useState, useEffect } from 'react';
import OfferForm from './OfferForm.tsx';
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';
import axiosInstance from '../../axiosConfig.ts';

const UpdateOffer = ({ onSuccess }) => {
    const [offerId, setOfferId] = useState('');
    const [offer, setOffer] = useState(null);
    const [error, setError] = useState('');

    const handleIdChange = (e) => {
        setOfferId(e.target.value);
    };

    useEffect(() => {
        if (offerId) {
            axiosInstance.get(`/offers/${offerId}/`)
                .then(response => {
                    setOffer(response.data);
                    setError('');
                })
                .catch(error => {
                    console.error(error);
                    setError('Offer not found. Please check the ID.');
                    setOffer(null);
                });
        }
    }, [offerId]);

    return (
        <div>
            <h2>Update Offer</h2>
            <Input type="text" value={offerId} onChange={handleIdChange} placeholder="Offer ID" />
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {offer && <OfferForm offerId={offerId} onSuccess={onSuccess} />}
        </div>
    );
};

export default UpdateOffer;