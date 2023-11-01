import React, { useState, useEffect } from 'react';

function Estatisticas() {
    const [breed, setBreed] = useState('');
    const [url, setUrl] = useState('');

    useEffect(() => {
        fetchImage();
    }, [breed]);

    const fetchImage = async () => {
        const res = await fetch(`http://localhost:8080/statistics/hist-flagrant/city/guarulhos?year=2023`)
        setUrl("http://localhost:8080/statistics/common-neighborhoods/city/guarulhos?year=2023");
    };

    return (
        <>
            <div className="image-container">
                <img className="image-card" src={url} />
            </div>
        </>
    );

}

export default Estatisticas;