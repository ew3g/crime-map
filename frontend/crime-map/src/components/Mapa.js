//import { React, useState, useEffect, useRef } from "react";
import { React, useState, useEffect } from "react";
import 'leaflet/dist/leaflet.css';

//import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet'

import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import L from 'leaflet';

//import { getBuracos, getCrimes, votoBuraco, createBuraco } from "../api/buraco";
import { getCrimes } from "../api/buraco";

//import { getTamanhosBuraco } from "../api/tamanhoBuraco";


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
    const [buracos, setBuracos] = useState([]);
    //const [tamanhosBuraco, setTamanhosBuraco] = useState([])

    //const [tamanhoBuracoSelecionado, setTamanhoBuracoSelecionado] = useState('')

    //const [markerPosition, setMarkerPosition] = useState(null)

    const [ano, setAno] = useState('')

    const fetchCrimes = async () => {
        const data = await getCrimes(ano);
        //console.log('rodou')
        //console.log(data);
        setBuracos(data)
    };

    const handleAnoSelecionadoChange = (event) => {
        console.log(event.target.value);
        setAno(event.target.value);
        fetchCrimes();
        //window.location.reload(false);
    }

    useEffect(() => {
        const fetchBuracos = async () => {
            const data = await getCrimes(ano);
            //console.log('rodou')
            //console.log(data);
            setBuracos(data)
        };

        // const fetchTamanhosBuraco = async () => {
        //     const data = await getTamanhosBuraco();
        //     console.log(data);
        //     setTamanhosBuraco(data);
        // }

        fetchBuracos();
        //fetchTamanhosBuraco();
    }, [ano]);



    const position = [-23.455, -46.533]

    return (
        <div>
            <div className="selectors-container">
                <div className="row">
                    <div className="col-md-12">
                        <select className="form-select" value={ano} onChange={handleAnoSelecionadoChange} defaultValue={2023}>
                            <option value="2023">2023</option>
                            <option value="2022">2022</option>
                            <option value="2021">2021</option>
                            <option value="2020">2020</option>
                            <option value="2019">2019</option>
                        </select>
                    </div>
                </div>
            </div>
            <MapContainer center={position} zoom={13} scrollWheelZoom={true} style={{ height: "100vh", width: "100%" }}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {/* <MapClickHandler /> */}
                {/* {markerPosition && (
                <PopupMarker position={markerPosition} icon={markerIcon("blue")}>
                    <Popup>
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12">
                                    <span> Deseja cadastrar um buraco aqui?</span>
                                </div>
                                <br /><br />
                                <div className="row">
                                    <div className="col-md-12">
                                        <select className="form-select" value={tamanhoBuracoSelecionado} onChange={handleTamanhoBuracoSelectChange}>
                                            <option value="null">Tamanho do Buraco</option>
                                            {tamanhosBuraco.map(tamanhoBuraco => (
                                                <option key={tamanhoBuraco.id} value={tamanhoBuraco.id}>
                                                    {tamanhoBuraco.nome}
                                                </option>
                                            ))}
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <br />
                            <div className="row">
                                <div className="col-md-12">
                                    <button className="btn btn-primary" onClick={handleMarkerConfirm}>Confirmar</button>
                                </div>
                            </div>
                        </div>
                    </Popup>
                </PopupMarker>
            )} */}
                {buracos.map((crime) => (
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