import React, {useContext} from 'react';
import {Col, Card, Image, Button} from "react-bootstrap";
import star from '../assets/star.png'
import {useHistory, useParams} from "react-router-dom";
import {DEVICE_ROUTE} from "../utils/const";

import {createProd, createType, decreaseProd, deleteProd, increaseProd, updateProd} from "../http/deviceAPI";
import axios from "axios";
import {useState} from "react";
import Form from "react-bootstrap/Form";
import {Context} from "../index";
import {observer} from "mobx-react-lite";


const DeviceBasketItem = ({device}) => {
    const history = useHistory()

    const context = useContext(Context)

    const [value, setValue] = useState('')


    const addType = () => {
        createType(value).then(data => {
            setValue('')

        })
    }


    return (

        <Col md={3} className={'mt-3'}>


            <Card onClick={() => history.push(DEVICE_ROUTE + '/' + device.product_id)}
                  style={{width: 150, cursor: 'pointer'}} border={'light'}>
                <Image width={150} height={150} src={'https://ledpremium.by/upload/iblock/13c/a_897531.jpg'}/>
                <div className='text-black-50 d-flex justify-content-between align-items-center'>
                    <div>Schneider Electric</div>
                    <div className='mt-1 d-flex align-items-center'>
                        <div>{device.product_price}</div>

                        <Image width={18} height={18} src={star}></Image>
                    </div>

                </div>
                <div>{device.product_name}</div>


            </Card>

            <div>
                <div>
                    <input
                        type='number'
                        className='count__input'
                        value={device.product_amount}
                        onChange={e => setValue((e.target.value))}
                        placeholder={'Введите название типа'}
                    />

                </div>
                <div className='count__controls'>
                    <Button onClick={() => increaseProd(device, context.device)}
                            variant={'outline-dark'}>+</Button>
                    <Button onClick={() => decreaseProd(device.product_id, device.product_amount)}
                            variant={'outline-dark'}>-</Button>


                </div>
            </div>

            <button onClick={() => createProd(device.product_id)}>Добавить в корзину</button>
            <button onClick={() => deleteProd(device.product_id)}>Удалить из корзины</button>


        </Col>


    );
};

export default DeviceBasketItem;
