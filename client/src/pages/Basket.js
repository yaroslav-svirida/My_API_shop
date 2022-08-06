import React, {useContext, useEffect} from 'react';
import {Col, Container, Row} from "react-bootstrap";
import TypeBar from "../components/TypeBar";
import BrandBar from "../components/BrandBar";
import {Context} from "../index";
import {fetchBasket, fetchBrands, fetchDevice, fetchTypes} from "../http/deviceAPI";
import {observer} from "mobx-react-lite";
import BasketShop from "../components/BasketShop";
import {useParams} from "react-router-dom";

const Basket =observer( () => {
    const {device} = useContext(Context)

    const {basket_id} = useParams()

    useEffect(() => {
        fetchTypes().then(data =>device.setTypes(data))
        fetchBrands().then(data =>device.setBrands(data))

        fetchBasket().then(data =>device.setBasket(data))


    }, [])
    return (

        <Container>
            <Row className='mt-2'>
                <Col md={3}>
                    <TypeBar/>
                </Col>

                <Col md={9}>
                    <BrandBar/>
                    <BasketShop/>

                </Col>
            </Row>

        </Container>
    );
});

export default Basket;