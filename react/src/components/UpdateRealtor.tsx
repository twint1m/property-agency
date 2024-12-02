import React, { useState, useEffect } from 'react';
import axiosInstance from '../axiosConfig';
import Input from './ui/Input';
import Button from './ui/Button';

const UpdateRealtor = ({ onSuccess }) => {
    const [realtorId, setRealtorId] = useState('');
    const [realtor, setRealtor] = useState({
        first_name: '',
        last_name: '',
        middle_name: '',
        commission_share: ''
    });
    const [error, setError] = useState('');

    useEffect(() => {
        if (realtorId) {
            axiosInstance.get(`/realtors/${realtorId}/`)
                .then(response => setRealtor(response.data))
                .catch(error => console.error(error));
        }
    }, [realtorId]);

    const handleIdChange = (e) => {
        setRealtorId(e.target.value);
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setRealtor({ ...realtor, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!realtor.first_name || !realtor.last_name || !realtor.middle_name) {
            setError("First name, last name, and middle name are required.");
            return;
        }

        axiosInstance.put(`/realtors/${realtorId}/`, realtor)
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
            <h2>Update Realtor</h2>
            <Input type="text" value={realtorId} onChange={handleIdChange} placeholder="Realtor ID" />
            <form onSubmit={handleSubmit}>
                <Input type="text" name="first_name" value={realtor.first_name} onChange={handleChange} placeholder="First Name" />
                <Input type="text" name="last_name" value={realtor.last_name} onChange={handleChange} placeholder="Last Name" />
                <Input type="text" name="middle_name" value={realtor.middle_name} onChange={handleChange} placeholder="Middle Name" />
                <Input type="number" name="commission_share" value={realtor.commission_share} onChange={handleChange} placeholder="Commission Share" />
                <Button type="submit">Submit</Button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default UpdateRealtor;