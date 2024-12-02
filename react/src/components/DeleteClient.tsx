import React, { useState } from 'react';
import axiosInstance from '../axiosConfig';
import Input from './ui/Input';
import Button from './ui/Button';

const DeleteClient = ({ onSuccess }) => {
    const [clientId, setClientId] = useState('');
    const [error, setError] = useState('');

    const handleIdChange = (e) => {
        setClientId(e.target.value);
    };

    const handleDelete = () => {
        axiosInstance.delete(`/clients/${clientId}/`)
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
            <h2>Delete Client</h2>
            <Input type="text" value={clientId} onChange={handleIdChange} placeholder="Client ID" />
            <Button onClick={handleDelete}>Delete</Button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default DeleteClient;