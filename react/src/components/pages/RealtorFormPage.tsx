import React from 'react';
import Tabs from '../ui/Tabs';
import CreateRealtor from '../CreateRealtor';
import UpdateRealtor from '../UpdateRealtor';
import DeleteRealtor from '../DeleteRealtor';

const RealtorFormPage = () => {
    const handleSuccess = (realtor) => {
        console.log('Realtor operation successful:', realtor);
    };

    const tabs = [
        { label: 'Create Realtor', content: <CreateRealtor onSuccess={handleSuccess} /> },
        { label: 'Update Realtor', content: <UpdateRealtor onSuccess={handleSuccess} /> },
        { label: 'Delete Realtor', content: <DeleteRealtor onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Realtor Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default RealtorFormPage;