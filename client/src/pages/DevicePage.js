import React, {useEffect, useState} from 'react';
import {Button, Card, Col, Container, Image, Row} from "react-bootstrap";
import bigStar from '../assets/bigStar.png'
import {useParams} from "react-router-dom";
import {deleteProd, fetchOneDevice} from "../http/deviceAPI";
import {createProd, createType} from "../http/deviceAPI";

const DevicePage = () => {
   const [device, setDevice] = useState({info:[]})
    const {id} = useParams()


    useEffect(() => {
        fetchOneDevice(id).then(data => setDevice(data))
        }, [])


    return (
        <Container className='mt-3'>
            <Row>
                <Col md={4}>
                    <Image width={250} height={250} src={'https://ledpremium.by/upload/iblock/13c/a_897531.jpg'}/>

                </Col>

                <Col md={4}>
                    <Row className='d-flex flex-column align-items-center'>
                        <h2>{device.name}</h2>
                        <div
                            className='d-flex align-items-center justify-content-center'
                            style={{
                                background: `url(${bigStar}) no-repeat center center`,
                                width: 240,
                                height: 240,
                                backgroundSize: 'cover',
                                fontSize: 64
                            }}>
                            {device.rating}
                        </div>
                    </Row>
                </Col>
                <Col md={4}>
                    <Card
                        className='d-flex flex-column align-items-center justify-content-around'
                        style={{width: 300, height: 300, fontSize: 32, border: '5px solid lightgray'}}
                    >
                        <h3>От: {device.price} руб.</h3>
                        <h3>От: {device.amount} руб.</h3>
                        <Button onClick={() =>createProd(device.id)} variant={'outline-dark'}>Добавить в корзину</Button>
                        <Button onClick={() =>deleteProd(device.product_id)} variant={'outline-dark'}>Удалить из корзины</Button>
                    </Card>

                </Col>
            </Row>
            {/*<Row className='d=flex flex-column m-3'>*/}
            {/*    <h1>Характеристики</h1>*/}
            {/*    {device.}*/}
            {/*    {device.info.map((info, index) =>*/}
            {/*        <Row key={info.id} style={{background: index%2 ===0 ? 'lightgray': 'transparent',*/}
            {/*                                    padding:10}}>*/}
            {/*            {info.title} : {info.description}*/}
            {/*        </Row>*/}
            {/*            )}*/}
            {/*</Row>*/}

                    </Container>
                    );
                };

                export default DevicePage;