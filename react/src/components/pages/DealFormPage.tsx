import React from 'react';
import Tabs from '../ui/Tabs';
import DealForm from '../Deal/DealForm';
import UpdateDeal from '../Deal/UpdateDeal';

const DealFormPage = () => {
    const handleSuccess = (deal) => {
        console.log('Deal operation successful:', deal);
    };

    const tabs = [
        { label: 'Create Deal', content: <DealForm onSubmit={handleSuccess} /> },
        { label: 'Update Deal', content: <UpdateDeal onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Deal Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default DealFormPage;