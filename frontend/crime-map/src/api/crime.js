import api from './axiosConfig';


export const getCrimes = async (ano) => {
    var url = '/crime/city/guarulhos';
    if (ano && ano !== '') {
        url += '?year=' + ano
    }
    const response = await api.get(url)
        .catch(function (error) {
            console.log(error)
        });
    return response.data;
};