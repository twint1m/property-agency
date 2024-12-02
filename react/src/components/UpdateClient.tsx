import React, { useState } from 'react';
import ClientForm from './ClientForm';
import Input from './ui/Input';
import Button from './ui/Button';

const UpdateClient = ({ onSuccess }) => {
    const [clientId, setClientId] = useState('');

    const handleIdChange = (e) => {
        setClientId(e.target.value);
    };

    return (
        <div>
            <h2>Update Client</h2>
            <Input type="text" value={clientId} onChange={handleIdChange} placeholder="Client ID" />
            {clientId && <ClientForm clientId={clientId} onSuccess={onSuccess} />}
        </div>
    );
};

export default UpdateClient;