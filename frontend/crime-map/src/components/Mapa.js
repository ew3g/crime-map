import { React, useState, useEffect } from "react";
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import L from 'leaflet';
import { getCrimes } from "../api/crime";


const markerIcon = () => {

    var iconUrl = `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png`
    return L.icon({
        iconUrl: iconUrl,
        iconSize: [32, 48],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32],
    });
}

const Mapa = () => {
    const [crimes, setCrimes] = useState([]);
    useEffect(() => {
        const fetchCrimes = async () => {
            const data = await getCrimes(2023);
            setCrimes(data)
        };
        fetchCrimes();
    }, []);

    const centerPosition = [-23.455, -46.533]

    return (
        <div>
            <div className="header-container">
                <div className="row">
                    <div className="col-md-12">
                        <span>Dados referentes ao ano de 2023</span>
                    </div>
                </div>
            </div>
            <br />
            <MapContainer center={centerPosition} zoom={13} scrollWheelZoom={true} style={{ height: "100vh", width: "100%" }}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {crimes.map((crime) => (
                    <Marker key={crime.id} position={[Number(crime.latitude), Number(crime.longitude)]} icon={markerIcon()}>
                        <Popup>
                            <div className="container">
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Número BO: {crime.numeroBO}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Data Ocorrência: {crime.dataOcorrencia}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        {crime.horaOcorrencia && <span>Hora Ocorrência: {crime.horaOcorrencia}</span>}
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Período Ocorrência: {crime.periodoOcorrencia}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Data Registro BO: {crime.registroBO}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        {crime.flagrante && <span>Flagrante: Sim</span>}
                                        {!crime.flagrante && <span>Flagrante: Não</span>}
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Endereço: {crime.endLogradouro}, {crime.endNumero}, {crime.endBairro}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Descrição Endereço: {crime.endDescricao}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Solução: {crime.solucao}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Delegacia Responsável: {crime.delegaciaCircunscricao}</span>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-12">
                                        <span>Delito: {crime.rubrica}</span>
                                    </div>
                                </div>
                                {(crime.veiculo.cor || crime.celular.quantidade > 0) && <div className="row">
                                    {crime.celular.quantidade > 0 && <div className="col-md-12">
                                        <span>Tipo Objeto: Celular</span><br />
                                        <span>Quantidade: {crime.celular.quantidade}</span><br />
                                        <span>Marca: {crime.celular.marca}</span><br />
                                    </div>}
                                    {crime.veiculo.cor && <div className="col-md-12">
                                        <span>Tipo Objeto: Veículo</span><br />
                                        <span>Placa: {crime.veiculo.placa}</span><br />
                                        <span>Cor: {crime.veiculo.cor}</span><br />
                                        <span>Marca: {crime.veiculo.marca}</span><br />
                                        <span>Ano Fabricação: {crime.veiculo.anoFabricacao}</span><br />
                                        <span>Ano Modelo: {crime.veiculo.anoModelo}</span><br />
                                        <span>Tipo: {crime.veiculo.tipo}</span><br />
                                    </div>}

                                </div>}

                            </div>
                        </Popup>
                    </Marker>
                ))}
            </MapContainer>
        </div>

    );
};

export default Mapa;