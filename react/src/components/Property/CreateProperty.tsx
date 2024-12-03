import React from 'react';
import PropertyForm from './PropertyForm';

const CreateProperty = ({ propertyType, onSuccess }) => {
    return (
        <div>
            <h2>Create Property</h2>
            <PropertyForm propertyType={propertyType} onSuccess={onSuccess} />
        </div>
    );
};

export default CreateProperty;