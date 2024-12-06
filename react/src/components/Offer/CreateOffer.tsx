import React from 'react';
import OfferForm from './OfferForm.tsx';

const CreateOffer = ({ onSuccess }) => {
    return (
        <div>
            <h2>Create Offer</h2>
            <OfferForm onSuccess={onSuccess} />
        </div>
    );
};

export default CreateOffer;