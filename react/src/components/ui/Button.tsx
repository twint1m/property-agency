import React from 'react';

const Button = ({ type = 'button', children, onClick }) => {
    return (
        <button type={type} onClick={onClick} style={styles.button}>
            {children}
        </button>
    );
};

const styles = {
    button: {
        padding: '10px 20px',
        backgroundColor: '#007BFF',
        color: '#fff',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
    },
};

export default Button;