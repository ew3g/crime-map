import React, { useState, useEffect } from 'react';
import AppNavbar from './Navbar';

function Estatisticas() {
    const [urlBairrosMaisOcorrencias, setUrlBairrosComMaisOcorrencias] = useState('');
    const [urlCrimesMaisFrequentes, setUrlCrimesMaisFrequentes] = useState('');
    const [urlCrimesFlagrantes, setUrlCrimesFlagrantes] = useState('');
    const [urlSolucoesMaisFrequentes, setUrlSolucoesMaisFrequentes] = useState('');
    const [urlDelegaciasComMaisCasos, setUrlDelegaciasComMaisCasos] = useState('');
    const [urlPeriodosComMaisCasos, setUrlPeriodosComMaisCasos] = useState('');

    useEffect(() => {
        fetchImage();
    }, []);

    const fetchImage = async () => {
        setUrlBairrosComMaisOcorrencias("http://localhost:8080/statistics/common-neighborhoods/city/guarulhos?year=2023");
        setUrlCrimesMaisFrequentes('http://localhost:8080/statistics/common-crimes/city/guarulhos?year=2023');
        setUrlCrimesFlagrantes('http://localhost:8080/statistics/hist-flagrant/city/guarulhos?year=2023');
        setUrlSolucoesMaisFrequentes('http://localhost:8080/statistics/common-solutions/city/guarulhos?year=2023');
        setUrlDelegaciasComMaisCasos('http://localhost:8080/statistics/common-police-departments/city/guarulhos?year=2023');
        setUrlPeriodosComMaisCasos('http://localhost:8080/statistics/common-day-period/city/guarulhos?year=2023')
    };

    return (
        <>
            <AppNavbar />
            <div className='statistics-container'>
                <div className='row'>
                    <div className='col-md-6'>
                        <span>Bairros com mais ocorrências</span><br />
                        <img className="image-card" src={urlBairrosMaisOcorrencias} alt="img-common-neighborhoods" />
                    </div>
                    <div className='col-md-6'>
                        <span>Crimes mais frequentes</span><br />
                        <img className="image-card" src={urlCrimesMaisFrequentes} alt="img-common-neighborhoods" />
                    </div>
                </div>
                <div className='row'>
                    <div className='col-md-6'>
                        <span>Soluções mais frequentes</span><br />
                        <img className="image-card" src={urlSolucoesMaisFrequentes} alt="img-common-neighborhoods" />
                    </div>
                    <div className='col-md-6'>
                        <span>Delegacias com mais casos</span><br />
                        <img className="image-card" src={urlDelegaciasComMaisCasos} alt="img-common-neighborhoods" />
                    </div>
                </div>
                <div className='row'>
                    <div className='col-md-6'>
                        <span>Períodos do dia x Crimes</span><br />
                        <img className="image-card" src={urlPeriodosComMaisCasos} alt="img-common-neighborhoods" />
                    </div>
                </div>
            </div>
        </>
    );

}

export default Estatisticas;