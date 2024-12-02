import React from 'react';

const Input = ({ type = 'text', name, value, onChange, placeholder }) => {
    return (
        <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
            placeholder={placeholder}
            style={styles.input}
        />
    );
};

const styles = {
    input: {
        padding: '10px',
        margin: '5px 0',
        border: '1px solid #ccc',
        borderRadius: '4px',
        width: '100%',
    },
};

export default Input;