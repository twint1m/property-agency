import React from 'react';

const NeedsList = ({ needs }) => {
    return (
        <ul>
            {needs.map(need => (
                <li key={need.id}>
                    {need.property_type} - {need.address}
                </li>
            ))}
        </ul>
    );
};

export default NeedsList;