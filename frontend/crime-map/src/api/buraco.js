import api from './axiosConfig';
import axios from 'axios';


export const getCrimes = async (ano) => {
    var url = '/crime/city/guarulhos';
    if (ano && ano != '') {
        url += '?year=' + ano
    }
    console.log(url);
    const response = await api.get(url)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};

export const getCrimesComuns = async () => {
    var url = "/statistics/common-crimes/city/guarulhos";
    //const res = await api.get(url);

    var resp = "";
    var res = axios.get("http://localhost:8080" + url, { responseType: 'blob' }).then(axios.spread((...responses) => {
        responses.map((res) => (
            //console.log(URL.createObjectURL(res.data))
            resp = URL.createObjectURL(res.data)
        ))
    }));

    return resp;
}

export const getBuracos = async () => {
    const response = await api.get('/buraco')
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};

export const getBuracoById = async (id) => {
    const response = await api.put(`/buracos/${id}`);
    return response.data;
};

export const createBuraco = async (data) => {
    const response = await api.post('/buraco', data)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};

export const updateBuraco = async (id, data) => {
    const response = await api.put(`/buracos/${id}`, data);
    return response.data;
};

export const deleteBuraco = async (id) => {
    const response = await api.delete(`/buracos/${id}`);
    return response.data;
};

export const votoBuraco = async (id) => {
    const response = await api.post(`/buraco/${id}`)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};