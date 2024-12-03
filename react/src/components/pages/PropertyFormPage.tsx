import React from 'react';
import Tabs from '../ui/Tabs';
import CreateProperty from '../Property/CreateProperty';
import UpdateProperty from '../Property/UpdateProperty';

const PropertyFormPage = () => {
    const handleSuccess = (property) => {
        console.log('Property operation successful:', property);
    };

    const tabs = [
        { label: 'Create Apartment', content: <CreateProperty propertyType="apartment" onSuccess={handleSuccess} /> },
        { label: 'Create House', content: <CreateProperty propertyType="house" onSuccess={handleSuccess} /> },
        { label: 'Create Land', content: <CreateProperty propertyType="land" onSuccess={handleSuccess} /> },
        { label: 'Update Apartment', content: <UpdateProperty propertyType="apartment" onSuccess={handleSuccess} /> },
        { label: 'Update House', content: <UpdateProperty propertyType="house" onSuccess={handleSuccess} /> },
        { label: 'Update Land', content: <UpdateProperty propertyType="land" onSuccess={handleSuccess} /> },
    ];

    return (
        <div>
            <h1>Property Management</h1>
            <Tabs tabs={tabs} />
        </div>
    );
};

export default PropertyFormPage;