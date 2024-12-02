import React from 'react';
import Tabs from '../ui/Tabs';
import CreateClient from '../CreateClient';
import UpdateClient from '../UpdateClient';
import DeleteClient from '../DeleteClient';

const ClientFormPage = () => {
    const handleSuccess = (client) => {
        console.log('Client operation successful:', client);
    };

    const tabs = [
        { label: 'Create Client', content: <CreateClient onSuccess={handleSuccess} /> },
        { label: 'Update Client', content: <UpdateClient onSuccess={handleSuccess} /> },
        { label: 'Delete Client', content: <DeleteClient onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Client Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default ClientFormPage;