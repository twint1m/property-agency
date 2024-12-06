import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig.ts';
import NeedsList from '../Need/NeedsList';
import OffersList from "../Offer/OfferList.tsx";

const ClientRealtorManagementPage = () => {
    const [clients, setClients] = useState([]);
    const [realtors, setRealtors] = useState([]);
    const [selectedClient, setSelectedClient] = useState(null);
    const [selectedRealtor, setSelectedRealtor] = useState(null);
    const [needs, setNeeds] = useState([]);
    const [offers, setOffers] = useState([]);

    useEffect(() => {
        axiosInstance.get('/clients/')
            .then(response => setClients(response.data))
            .catch(error => console.error('Error fetching clients:', error));

        axiosInstance.get('/realtors/')
            .then(response => setRealtors(response.data))
            .catch(error => console.error('Error fetching realtors:', error));
    }, []);

    const handleClientSelect = (clientId) => {
        setSelectedClient(clientId);
        setSelectedRealtor(null);
        fetchNeedsAndOffers(clientId, 'client');
    };

    const handleRealtorSelect = (realtorId) => {
        setSelectedRealtor(realtorId);
        setSelectedClient(null);
        fetchNeedsAndOffers(realtorId, 'realtor');
    };

    const fetchNeedsAndOffers = (id, type) => {
        axiosInstance.get(`/needs/?${type}=${id}`)
            .then(response => setNeeds(response.data))
            .catch(error => console.error(`Error fetching needs for ${type}:`, error));

        axiosInstance.get(`/offers/?${type}=${id}`)
            .then(response => setOffers(response.data))
            .catch(error => console.error(`Error fetching offers for ${type}:`, error));
    };

    return (
        <div>
            <h1>Client and Realtor Management</h1>
            <div>
                <h2>Clients</h2>
                <ul>
                    {clients.map(client => (
                        <li key={client.id} onClick={() => handleClientSelect(client.id)}>
                            {client.first_name} {client.last_name}
                        </li>
                    ))}
                </ul>
            </div>
            <div>
                <h2>Realtors</h2>
                <ul>
                    {realtors.map(realtor => (
                        <li key={realtor.id} onClick={() => handleRealtorSelect(realtor.id)}>
                            {realtor.first_name} {realtor.last_name}
                        </li>
                    ))}
                </ul>
            </div>
            <div>
                <h2>Needs</h2>
                <NeedsList needs={needs} />
            </div>
            <div>
                <h2>Offers</h2>
                <OffersList offers={offers} />
            </div>
        </div>
    );
};

export default ClientRealtorManagementPage;