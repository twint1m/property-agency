import React from 'react';
import Tabs from '../ui/Tabs';
import CreateOffer from '../Offer/CreateOffer.tsx';
import UpdateOffer from '../Offer/UpdateOffer.tsx';
import DeleteOffer from '../Offer/DeleteOffer.tsx';

const OfferFormPage = () => {
    const handleSuccess = (offer) => {
        console.log('Offer operation successful:', offer);
    };

    const tabs = [
        { label: 'Create Offer', content: <CreateOffer onSuccess={handleSuccess} /> },
        { label: 'Update Offer', content: <UpdateOffer onSuccess={handleSuccess} /> },
        { label: 'Delete Offer', content: <DeleteOffer onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Offer Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default OfferFormPage;