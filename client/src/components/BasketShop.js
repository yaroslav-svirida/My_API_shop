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

            <button onClick={fetchExcel}>Загрузить файл</button>
                {device.basket.map(device =>

                    <DeviceBasketItem key={device.product_id} device={device}/>

                )}


        </Row>
    );
});

export default BasketShop;