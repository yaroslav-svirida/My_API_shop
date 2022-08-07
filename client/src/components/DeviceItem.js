import React from 'react';
import {Col, Card, Image} from "react-bootstrap";
import star from '../assets/star.png'
import {useHistory, useParams} from "react-router-dom";
import {DEVICE_ROUTE} from "../utils/const";

import {createProd, createType, deleteProd} from "../http/deviceAPI";
import axios from "axios";
import {useState} from "react";


const DeviceItem = ({device}) => {
    const history = useHistory()






    return (

        <Col md={3} className={'mt-3'} >

            <Card onClick={() => history.push(DEVICE_ROUTE + '/' + device.id)}
                  style={{width: 150, cursor: 'pointer'}} border={'light'}>
                <Image width={150} height={150} src={'https://ledpremium.by/upload/iblock/13c/a_897531.jpg'}/>
                <div className='text-black-50 d-flex justify-content-between align-items-center'>
                    <div>Schneider Electric</div>
                    <div className='mt-1 d-flex align-items-center'>
                        <div>{device.price}</div>
                        <Image width={18} height={18} src={star}></Image>
                    </div>

                </div>
                <div>{device.name}</div>
                <div>{device.amount}</div>





            </Card>
           <button onClick={() =>createProd(device.id)}>Добавить в корзину</button>
           <button onClick={() =>deleteProd(device.id)}>Удалить из корзины</button>

        </Col>



    );
};

export default DeviceItem;
