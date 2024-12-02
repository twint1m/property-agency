import React, { useState } from 'react';
import axiosInstance from '../axiosConfig';
import Input from './ui/Input';
import Button from './ui/Button';

const DeleteRealtor = ({ onSuccess }) => {
    const [realtorId, setRealtorId] = useState('');
    const [error, setError] = useState('');

    const handleIdChange = (e) => {
        setRealtorId(e.target.value);
    };

    const handleDelete = () => {
        axiosInstance.delete(`/realtors/${realtorId}/`)
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
            <h2>Delete Realtor</h2>
            <Input type="text" value={realtorId} onChange={handleIdChange} placeholder="Realtor ID" />
            <Button onClick={handleDelete}>Delete</Button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default DeleteRealtor;