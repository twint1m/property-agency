import React, { useState } from 'react';
import PropertyForm from './PropertyForm';
import Input from '../ui/Input.tsx';

const UpdateProperty = ({ propertyType, onSuccess }) => {
    const [propertyId, setPropertyId] = useState('');

    const handleIdChange = (e) => {
        setPropertyId(e.target.value);
    };

    return (
        <div>
            <h2>Update Property</h2>
            <Input type="text" value={propertyId} onChange={handleIdChange} placeholder="Property ID" />
            {propertyId && <PropertyForm propertyType={propertyType} propertyId={propertyId} onSuccess={onSuccess} />}
        </div>
    );
};

export default UpdateProperty;