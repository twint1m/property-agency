// react/src/components/pages/ClientNeedsPage.tsx
import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosConfig';
import NeedsList from '../Need/NeedsList';

const ClientNeedsPage = () => {
    const [needs, setNeeds] = useState([]);

    useEffect(() => {
        axiosInstance.get('/needs/')
            .then(response => setNeeds(response.data))
            .catch(error => console.error('Error fetching client needs:', error));
    }, []);

    return (
        <div>
            <h1>Client Needs</h1>
            <NeedsList needs={needs} />
        </div>
    );
};

export default ClientNeedsPage;