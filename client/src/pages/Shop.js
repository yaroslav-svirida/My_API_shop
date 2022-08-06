import React, {useContext, useEffect} from 'react';
import {Col, Container, Row} from "react-bootstrap";
import TypeBar from "../components/TypeBar";
import BrandBar from "../components/BrandBar";
import DeviceList from "../components/DeviceList";
import {Context} from "../index";
import {fetchBrands, fetchDevice, fetchTypes} from "../http/deviceAPI";
import {observer} from "mobx-react-lite";

const Shop =observer( () => {
    const {device} = useContext(Context)
    useEffect(() => {
        fetchTypes().then(data =>device.setTypes(data))
        fetchBrands().then(data =>device.setBrands(data))
        fetchDevice().then(data =>device.setDevices(data))

    }, [])
    return (
        <Container>
            <Row className='mt-2'>
                <Col md={3}>
                    <TypeBar/>
                </Col>

                <Col md={9}>
                    <BrandBar/>
                    <DeviceList/>

                </Col>
            </Row>

        </Container>
    );
});

export default Shop;