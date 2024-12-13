import React from 'react';
import Tabs from '../ui/Tabs';
import DealForm from './DealForm';

const CreateDeal = ({ onSuccess }) => {
    const handleSuccess = (deal) => {
        console.log('Deal operation successful:', deal);
        onSuccess(deal);
    };

    const tabs = [
        { label: 'Create Deal', content: <DealForm onSubmit={handleSuccess} /> },
        // Add other tabs if necessary
    ];

    return (
        <div>
            <h1>Deal Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default CreateDeal;