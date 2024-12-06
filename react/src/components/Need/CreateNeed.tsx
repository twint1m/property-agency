import React from 'react';
import NeedForm from './NeedForm.tsx';

const CreateNeed = ({ onSuccess }) => {
    return (
        <div>
            <h2>Create Need</h2>
            <NeedForm onSuccess={onSuccess} />
        </div>
    );
};

export default CreateNeed;