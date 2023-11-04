import React, { useState, useEffect } from 'react';
import AppNavbar from './Navbar';

function Estatisticas() {
    const [urlBarrasCrimesMaisComuns, setUrlBarrasCrimesMaisComuns] = useState('');
    const [urlPizzaCrimesMaisComuns, setUrlPizzaCrimesMaisComuns] = useState('');

    const [urlBarrasBairrosMaisCrimes, setUrlBarrasBairrosMaisCrimes] = useState('');
    const [urlPizzaBairrosMaisCrimes, setUrlPizzaBairrosMaisCrimes] = useState('');

    const [urlBarrasSolucoesMaisComuns, setUrlBarrasSolucoesMaisComuns] = useState('');
    const [urlPizzaSolucoesMaisComuns, setUrlPizzaSolucoesMaisComuns] = useState('');

    const [urlBarrasDelegaciasComMaisCrimes, setUrlBarrasDelegaciasComMaisCrimes] = useState('');
    const [urlPizzaDelegaciasComMaisCrimes, setUrlPizzaDelegaciasComMaisCrimes] = useState('');

    const [urlBarrasPeriodosComMaisCrimes, setUrlBarrasPeriodosComMaisCrimes] = useState('');
    const [urlPizzaPeriodosComMaisCrimes, setUrlPizzaPeriodosComMaisCrimes] = useState('');
    useEffect(() => {
        fetchImage();
    }, []);

    const fetchImage = async () => {
        setUrlBarrasCrimesMaisComuns("http://localhost:8080/statistics/bar/common-crimes/city/guarulhos?year=2023");
        setUrlPizzaCrimesMaisComuns("http://localhost:8080/statistics/pie/common-crimes/city/guarulhos?year=2023");
        setUrlBarrasBairrosMaisCrimes("http://localhost:8080/statistics/bar/common-neighborhoods/city/guarulhos?year=2023");
        setUrlPizzaBairrosMaisCrimes("http://localhost:8080/statistics/pie/common-neighborhoods/city/guarulhos?year=2023");
        setUrlBarrasSolucoesMaisComuns("http://localhost:8080/statistics/bar/common-solutions/city/guarulhos?year=2023");
        setUrlPizzaSolucoesMaisComuns("http://localhost:8080/statistics/pie/common-solutions/city/guarulhos?year=2023");
        setUrlBarrasDelegaciasComMaisCrimes("http://localhost:8080/statistics/bar/common-police-departments/city/guarulhos?year=2023");
        setUrlPizzaDelegaciasComMaisCrimes("http://localhost:8080/statistics/pie/common-police-departments/city/guarulhos?year=2023");
        setUrlBarrasPeriodosComMaisCrimes("http://localhost:8080/statistics/bar/common-day-period/city/guarulhos?year=2023");
        setUrlPizzaPeriodosComMaisCrimes("http://localhost:8080/statistics/pie/common-day-period/city/guarulhos?year=2023");
    };

    return (
        <>
            <AppNavbar />
            <div className="header-container">
                <div className="row">
                    <div className="col-md-12">
                        <span>Dados referentes ao ano de 2023</span>
                    </div>
                </div>
            </div>
            <br />
            <div className='crimes-statistics-container'>
                <div className='row'>
                    <div className='col-md-12'>Crimes mais comuns</div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlBarrasCrimesMaisComuns} alt="img-bar-common-crimes" />
                    </div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlPizzaCrimesMaisComuns} alt="img-pie-common-crimes" />
                    </div>
                </div>
            </div>
            <div className='neighborhoods-statistics-container'>
                <div className='row'>
                    <div className='col-md-12'>Bairros com mais ocorrências</div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlBarrasBairrosMaisCrimes} alt="img-bar-common-neighborhoods" />
                    </div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlPizzaBairrosMaisCrimes} alt="img-pie-common-neighborhoods" />
                    </div>
                </div>
            </div>
            <div className='solutions-statistics-container'>
                <div className='row'>
                    <div className='col-md-12'>Soluções mais comuns</div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlBarrasSolucoesMaisComuns} alt="img-bar-common-solutions" />
                    </div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlPizzaSolucoesMaisComuns} alt="img-pie-common-solutions" />
                    </div>
                </div>
            </div>
            <div className='police-departments-statistics-container'>
                <div className='row'>
                    <div className='col-md-12'>Delegacias com mais crimes registrados</div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlBarrasDelegaciasComMaisCrimes} alt="img-bar-police-departments" />
                    </div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlPizzaDelegaciasComMaisCrimes} alt="img-pie-police-departments" />
                    </div>
                </div>
            </div>
            <div className='periods-statistics-container'>
                <div className='row'>
                    <div className='col-md-12'>Total crimes por períodos do dia</div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlBarrasPeriodosComMaisCrimes} alt="img-bar-common-periods" />
                    </div>
                    <div className='col-md-6'>
                        <img className="image-card" src={urlPizzaPeriodosComMaisCrimes} alt="img-pie-common-periodos" />
                    </div>
                </div>
            </div>
        </>
    );

}

export default Estatisticas;