import React from 'react';
import ClientForm from './ClientForm';

const CreateClient = ({ onSuccess }) => {
    return (
        <div>
            <h2>Create Client</h2>
            <ClientForm onSuccess={onSuccess} />
        </div>
    );
};

export default CreateClient;