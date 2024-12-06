// DeleteNeed.tsx
import React, { useState } from 'react';
import axiosInstance from "../../axiosConfig.ts";
import Input from '../ui/Input.tsx';
import Button from '../ui/Button.tsx';

const DeleteNeed = ({ onSuccess }) => {
    const [needId, setNeedId] = useState('');

    const handleIdChange = (e) => {
        setNeedId(e.target.value);
    };

    const handleDelete = () => {
        axiosInstance.delete(`/needs/${needId}/`)
            .then(response => {
                onSuccess(response.data);
            })
            .catch(error => {
                console.error(error);
                alert("An error occurred. Please try again.");
            });
    };

    return (
        <div>
            <h2>Delete Need</h2>
            <Input type="text" value={needId} onChange={handleIdChange} placeholder="Need ID" />
            <Button onClick={handleDelete}>Delete</Button>
        </div>
    );
};

export default DeleteNeed;