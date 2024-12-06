import React from 'react';

const OffersList = ({ offers }) => {
    return (
        <ul>
            {offers.map(offer => (
                <li key={offer.id}>
                    {offer.description} - {offer.price}
                </li>
            ))}
        </ul>
    );
};

export default OffersList;