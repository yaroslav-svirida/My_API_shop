import React, {useContext} from 'react';
import DeviceItem from "./DeviceItem";

import {Context} from "../index";
import {Row} from "react-bootstrap";
import {observer} from "mobx-react-lite";
import DeviceBasketItem from "./DeviceBasketItem";
import {deleteProd, fetchExcel} from "../http/deviceAPI";


const BasketShop = observer(() => {
    const {device} = useContext(Context)




    return (

        <Row className='d-flex'>
            <a href = 'http://127.0.0.1:8000/basket_excel/get/' target={'_blank'}>hi</a>
            <button onClick={fetchExcel}>Загрузить файл</button>
                {device.basket(device =>

                    <DeviceBasketItem key={device.product_id} device={device}/>

                )}


        </Row>
    );
});

export default BasketShop;