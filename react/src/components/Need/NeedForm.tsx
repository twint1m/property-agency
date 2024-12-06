import React, { useState, useEffect } from 'react';
import axiosInstance from "../../axiosConfig.ts";
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';

const NeedForm = ({ needId, onSuccess }) => {
    const [need, setNeed] = useState({
        client: '',
        realtor: '',
        property_type: '',
        address: '',
        min_price: '',
        max_price: '',
        min_area: '',
        max_area: '',
        min_rooms: '',
        max_rooms: '',
        min_floor: '',
        max_floor: '',
        min_floors: '',
        max_floors: ''
    });
    const [clients, setClients] = useState([]);
    const [realtors, setRealtors] = useState([]);

    const propertyTypes = [
        { value: 'apartment', label: 'Apartment' },
        { value: 'house', label: 'House' },
        { value: 'land', label: 'Land' }
    ];

    useEffect(() => {
        axiosInstance.get('/clients/')
            .then(response => {
                setClients(response.data);
            })
            .catch(error => console.error('Error fetching clients:', error));

        axiosInstance.get('/realtors/')
            .then(response => {
                setRealtors(response.data);
            })
            .catch(error => console.error('Error fetching realtors:', error));

        if (needId) {
            axiosInstance.get(`/needs/${needId}/`)
                .then(response => {
                    setNeed(response.data);
                })
                .catch(error => console.error('Error fetching need:', error));
        }
    }, [needId]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setNeed({ ...need, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const transformedNeed = {
            ...need,
            client: need.client || null,
            realtor: need.realtor || null,
            property_type: need.property_type || null,
            address: need.address || null,
            min_price: need.min_price || null,
            max_price: need.max_price || null,
            min_area: need.min_area || null,
            max_area: need.max_area || null,
            min_rooms: need.min_rooms || null,
            max_rooms: need.max_rooms || null,
            min_floor: need.min_floor || null,
            max_floor: need.max_floor || null,
            min_floors: need.min_floors || null,
            max_floors: need.max_floors || null
        };

        const request = needId
            ? axiosInstance.put(`/needs/${needId}/`, transformedNeed)
            : axiosInstance.post('/needs/', transformedNeed);

        request.then(response => {
            onSuccess(response.data);
        }).catch(error => {
            console.error('Error submitting form:', error);
            alert("An error occurred. Please try again.");
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <select name="client" value={need.client} onChange={handleChange}>
                <option value="">Select Client</option>
                {clients.map(client => (
                    <option key={client.id} value={client.id}>{client.first_name} {client.last_name}</option>
                ))}
            </select>
            <select name="realtor" value={need.realtor} onChange={handleChange}>
                <option value="">Select Realtor</option>
                {realtors.map(realtor => (
                    <option key={realtor.id} value={realtor.id}>{realtor.first_name} {realtor.last_name}</option>
                ))}
            </select>
            <select name="property_type" value={need.property_type} onChange={handleChange}>
                <option value="">Select Property Type</option>
                {propertyTypes.map(type => (
                    <option key={type.value} value={type.value}>{type.label}</option>
                ))}
            </select>
            <Input type="text" name="address" value={need.address} onChange={handleChange} placeholder="Address" />
            <Input type="number" name="min_price" value={need.min_price} onChange={handleChange} placeholder="Min Price" />
            <Input type="number" name="max_price" value={need.max_price} onChange={handleChange} placeholder="Max Price" />
            {need.property_type === 'apartment' && (
                <>
                    <Input type="number" name="min_area" value={need.min_area} onChange={handleChange} placeholder="Min Area" />
                    <Input type="number" name="max_area" value={need.max_area} onChange={handleChange} placeholder="Max Area" />
                    <Input type="number" name="min_rooms" value={need.min_rooms} onChange={handleChange} placeholder="Min Rooms" />
                    <Input type="number" name="max_rooms" value={need.max_rooms} onChange={handleChange} placeholder="Max Rooms" />
                    <Input type="number" name="min_floor" value={need.min_floor} onChange={handleChange} placeholder="Min Floor" />
                    <Input type="number" name="max_floor" value={need.max_floor} onChange={handleChange} placeholder="Max Floor" />
                </>
            )}
            {need.property_type === 'house' && (
                <>
                    <Input type="number" name="min_area" value={need.min_area} onChange={handleChange} placeholder="Min Area" />
                    <Input type="number" name="max_area" value={need.max_area} onChange={handleChange} placeholder="Max Area" />
                    <Input type="number" name="min_rooms" value={need.min_rooms} onChange={handleChange} placeholder="Min Rooms" />
                    <Input type="number" name="max_rooms" value={need.max_rooms} onChange={handleChange} placeholder="Max Rooms" />
                    <Input type="number" name="min_floors" value={need.min_floors} onChange={handleChange} placeholder="Min Floors" />
                    <Input type="number" name="max_floors" value={need.max_floors} onChange={handleChange} placeholder="Max Floors" />
                </>
            )}
            {need.property_type === 'land' && (
                <>
                    <Input type="number" name="min_area" value={need.min_area} onChange={handleChange} placeholder="Min Area" />
                    <Input type="number" name="max_area" value={need.max_area} onChange={handleChange} placeholder="Max Area" />
                </>
            )}
            <Button type="submit">Submit</Button>
        </form>
    );
};

export default NeedForm;