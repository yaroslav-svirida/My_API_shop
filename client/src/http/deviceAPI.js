import {$authHost, $host} from "./index";
import axios from "axios";


export const createType = async (type) => {
    const {data} = await $host.post('http://127.0.0.1:8000/collection/create/', type)
    return data

}

export const increaseProd =(device, store) => {
    $authHost.put('http://127.0.0.1:8000/product_in_basket/put/'+ device.product_id +'/',
        {product_amount: device.product_amount+1})
        .then(function (response) {
           device.setAmount(device.product_amount+1)
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
}

export const decreaseProd =(id, value) => {
    $authHost.put('http://127.0.0.1:8000/product_in_basket/put/'+ id +'/',
        {product_amount: value-1})
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
}



// await request.delete('<your route>, { data: { <your data> }});

export const createProd =(pk) => {
    $authHost.post('http://127.0.0.1:8000/product_in_basket/post/' ,
        {id: pk})
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
}

export const deleteProd =(pk) => {
    $authHost.delete('http://127.0.0.1:8000/product_in_basket/delete/'+ pk +'/',
        )
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        })
}

export const fetchTypes = async (email, password) => {
    const {data} = await $authHost.get('http://127.0.0.1:8000/collection/get/')

    return data

}
// export const fetchExcel = async () => {
//     const {data} = await $authHost.get('http://127.0.0.1:8000/basket_excel/get/')
//
//     return data
// }

export const fetchExcel = () => {
    $authHost({
        url: 'http://127.0.0.1:8000/basket_excel/get/', //your url
        method: 'GET',
        responseType: 'blob', // important
    }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'file.xlsx'); //or any other extension
        document.body.appendChild(link);
        link.click();
    });
}




export const createBrand = async (brand) => {
    const {data} = await $host.post('http://127.0.0.1:8000/brend/create/', brand)
    return data

}

export const fetchBrands = async (email, password) => {
    const {data} = await $authHost.get('http://127.0.0.1:8000/brend/get/')
    return data
}

export const fetchDevice = async (email, password) => {
    const {data} = await $authHost.get('http://127.0.0.1:8000/product/get/')
    return data
}
export const fetchOneDevice = async (id) => {
    const {data} = await $authHost.get('http://127.0.0.1:8000/product/get/' + id)
    return data
}

export const fetchBasket = async () => {

    const {data} = await $authHost.get('http://127.0.0.1:8000/product_in_basket/get/')

    return data
}
