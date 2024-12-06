import React from 'react';
import Tabs from '../ui/Tabs';
import CreateNeed from '../Need/CreateNeed';
import UpdateNeed from '../Need/UpdateNeed';
import DeleteNeed from '../Need/DeleteNeed';

const NeedFormPage = () => {
    const handleSuccess = (need) => {
        console.log('Need operation successful:', need);
    };

    const tabs = [
        { label: 'Create Need', content: <CreateNeed onSuccess={handleSuccess} /> },
        { label: 'Update Need', content: <UpdateNeed onSuccess={handleSuccess} /> },
        { label: 'Delete Need', content: <DeleteNeed onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Need Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default NeedFormPage;