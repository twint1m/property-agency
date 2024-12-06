// UpdateNeed.tsx
import React, { useState } from 'react';
import NeedForm from './NeedForm.tsx';
import Input from '../ui/Input.tsx';

const UpdateNeed = ({ onSuccess }) => {
    const [needId, setNeedId] = useState('');

    const handleIdChange = (e) => {
        setNeedId(e.target.value);
    };

    return (
        <div>
            <h2>Update Need</h2>
            <Input type="text" value={needId} onChange={handleIdChange} placeholder="Need ID" />
            {needId && <NeedForm needId={needId} onSuccess={onSuccess} />}
        </div>
    );
};

export default UpdateNeed;