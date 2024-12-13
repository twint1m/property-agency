import React, { useState } from 'react';
import DealForm from './DealForm';
import Input from '../ui/Input';

const UpdateDeal = ({ onSuccess }) => {
    const [dealId, setDealId] = useState('');

    const handleIdChange = (e) => {
        setDealId(e.target.value);
    };

    return (
        <div>
            <h2>Update Deal</h2>
            <Input type="text" value={dealId} onChange={handleIdChange} placeholder="Deal ID" />
            {dealId && <DealForm dealId={dealId} onSubmit={onSuccess} />}
        </div>
    );
};

export default UpdateDeal;