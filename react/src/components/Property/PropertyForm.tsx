import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig.ts';
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';

const PropertyForm = ({ propertyType, propertyId, onSuccess }) => {
    const [property, setProperty] = useState({
        city: '',
        street: '',
        house_number: '',
        apartment_number: '',
        latitude: '',
        longitude: '',
        floor: '',
        rooms: '',
        area: ''
    });

    useEffect(() => {
        if (propertyId) {
            axiosInstance.get(`/${propertyType}s/${propertyId}/`)
                .then(response => setProperty(response.data))
                .catch(error => console.error(error));
        }
    }, [propertyId, propertyType]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProperty({ ...property, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const request = propertyId
            ? axiosInstance.put(`/${propertyType}s/${propertyId}/`, property)
            : axiosInstance.post(`/${propertyType}s/`, property);

        request.then(response => {
            onSuccess(response.data);
        }).catch(error => {
            console.error(error);
            alert("An error occurred. Please try again.");
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <Input type="text" name="city" value={property.city} onChange={handleChange} placeholder="City" />
            <Input type="text" name="street" value={property.street} onChange={handleChange} placeholder="Street" />
            <Input type="text" name="house_number" value={property.house_number} onChange={handleChange} placeholder="House Number" />
            <Input type="text" name="apartment_number" value={property.apartment_number} onChange={handleChange} placeholder="Apartment Number" />
            <Input type="number" name="latitude" value={property.latitude} onChange={handleChange} placeholder="Latitude" />
            <Input type="number" name="longitude" value={property.longitude} onChange={handleChange} placeholder="Longitude" />
            <Input type="number" name="floor" value={property.floor} onChange={handleChange} placeholder="Floor" />
            <Input type="number" name="rooms" value={property.rooms} onChange={handleChange} placeholder="Rooms" />
            <Input type="number" name="area" value={property.area} onChange={handleChange} placeholder="Area" />
            <Button type="submit">Submit</Button>
        </form>
    );
};

export default PropertyForm;