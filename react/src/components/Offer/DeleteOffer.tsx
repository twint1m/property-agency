import React, { useState } from 'react';
import axiosInstance from '../../axiosConfig.ts';
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';

const DeleteOffer = ({ onSuccess }) => {
    const [offerId, setOfferId] = useState('');
    const [error, setError] = useState('');

    const handleIdChange = (e) => {
        setOfferId(e.target.value);
    };

    const handleDelete = () => {
        axiosInstance.delete(`/offers/${offerId}/`)
            .then(response => {
                onSuccess(response.data);
                setError('');
            })
            .catch(error => {
                console.error(error);
                setError("An error occurred. Please try again.");
            });
    };

    return (
        <div>
            <h2>Delete Offer</h2>
            <Input type="text" value={offerId} onChange={handleIdChange} placeholder="Offer ID" />
            <Button onClick={handleDelete}>Delete</Button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default DeleteOffer;