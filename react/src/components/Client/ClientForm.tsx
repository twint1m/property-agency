import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig.ts';
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';

const ClientForm = ({ clientId, onSuccess }) => {
    const [client, setClient] = useState({
        first_name: '',
        last_name: '',
        middle_name: '',
        phone_number: '',
        email: ''
    });

    useEffect(() => {
        if (clientId) {
            axiosInstance.get(`/clients/${clientId}/`)
                .then(response => setClient(response.data))
                .catch(error => console.error(error));
        }
    }, [clientId]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setClient({ ...client, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!client.phone_number && !client.email) {
            alert("Either phone number or email must be provided.");
            return;
        }

        const request = clientId
            ? axiosInstance.put(`/clients/${clientId}/`, client)
            : axiosInstance.post('/clients/', client);

        request.then(response => {
            onSuccess(response.data);
        }).catch(error => {
            console.error(error);
            alert("An error occurred. Please try again.");
        });
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <Input type="text" name="first_name" value={client.first_name} onChange={handleChange} placeholder="First Name" />
                <Input type="text" name="last_name" value={client.last_name} onChange={handleChange} placeholder="Last Name" />
                <Input type="text" name="middle_name" value={client.middle_name} onChange={handleChange} placeholder="Middle Name" />
                <Input type="text" name="phone_number" value={client.phone_number} onChange={handleChange} placeholder="Phone Number" />
                <Input type="email" name="email" value={client.email} onChange={handleChange} placeholder="Email" />
                <Button type="submit">Submit</Button>
            </form>
        </div>
    );
};

export default ClientForm;