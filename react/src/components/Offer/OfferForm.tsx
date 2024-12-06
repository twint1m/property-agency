import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig.ts';
import Input from '../ui/Input.tsx';
import Select from '../ui/Select.tsx';
import Button from '../ui/Button.tsx';

const OfferForm = ({ offerId, onSuccess }) => {
    const [offer, setOffer] = useState({
        client: '',
        realtor: '',
        apartment: '',
        house: '',
        land: '',
        description: '',
        price: ''
    });
    const [clients, setClients] = useState([]);
    const [realtors, setRealtors] = useState([]);
    const [apartments, setApartments] = useState([]);
    const [houses, setHouses] = useState([]);
    const [lands, setLands] = useState([]);
    const [selectedPropertyType, setSelectedPropertyType] = useState('');

    useEffect(() => {
        // Fetch clients, realtors, apartments, houses, and lands
        axiosInstance.get('/clients/').then(response => setClients(response.data));
        axiosInstance.get('/realtors/').then(response => setRealtors(response.data));
        axiosInstance.get('/apartments/').then(response => setApartments(response.data));
        axiosInstance.get('/houses/').then(response => setHouses(response.data));
        axiosInstance.get('/lands/').then(response => setLands(response.data));

        if (offerId) {
            // Fetch offer details if offerId is provided
            axiosInstance.get(`/offers/${offerId}/`)
                .then(response => {
                    setOffer(response.data);
                    if (response.data.apartment) setSelectedPropertyType('apartment');
                    if (response.data.house) setSelectedPropertyType('house');
                    if (response.data.land) setSelectedPropertyType('land');
                })
                .catch(error => console.error(error));
        }
    }, [offerId]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setOffer({ ...offer, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const request = offerId
            ? axiosInstance.put(`/offers/${offerId}/`, offer)
            : axiosInstance.post('/offers/', offer);

        request.then(response => {
            onSuccess(response.data);
        }).catch(error => {
            console.error(error);
            alert("An error occurred. Please try again.");
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <Select name="client" value={offer.client} onChange={handleChange} options={clients} placeholder="Select Client" />
            <Select name="realtor" value={offer.realtor} onChange={handleChange} options={realtors} placeholder="Select Realtor" />
            <Select name="apartment" value={offer.apartment} onChange={handleChange} options={apartments} placeholder="Select Apartment" disabled={selectedPropertyType && selectedPropertyType !== 'apartment'} />
            <Select name="house" value={offer.house} onChange={handleChange} options={houses} placeholder="Select House" disabled={selectedPropertyType && selectedPropertyType !== 'house'} />
            <Select name="land" value={offer.land} onChange={handleChange} options={lands} placeholder="Select Land" disabled={selectedPropertyType && selectedPropertyType !== 'land'} />
            <Input type="text" name="description" value={offer.description} onChange={handleChange} placeholder="Description" />
            <Input type="number" name="price" value={offer.price} onChange={handleChange} placeholder="Price" />
            <Button type="submit">Submit</Button>
        </form>
    );
};

export default OfferForm;