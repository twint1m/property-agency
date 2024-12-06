import React from 'react';

const Select = ({ name, value, onChange, options, placeholder }) => {
    return (
        <select name={name} value={value} onChange={onChange}>
            <option value="" disabled>{placeholder}</option>
            {options.map((option, index) => (
                <option key={option.id || index} value={option.id}>
                    {option.first_name ? `${option.first_name} ${option.last_name}` : option.name || option.city || option.street}
                </option>
            ))}
        </select>
    );
};

export default Select;