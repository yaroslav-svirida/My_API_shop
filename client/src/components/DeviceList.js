import React, {useContext, useEffect, useState} from 'react';
import DeviceItem from "./DeviceItem";

import {Context} from "../index";
import {Carousel, Row, Table} from "react-bootstrap";
import {observer} from "mobx-react-lite";
import axios from "axios";


const DeviceList = observer(() => {
    const {device} = useContext(Context)


    const [value, setValue] = useState('')
    const filteredCountries = device.device.filter(product => {

        return product.name.toLowerCase().includes(value.toLowerCase())

    })


    return (
        <>
            <Carousel>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src="https://www.meme-arsenal.com/memes/eeebc46e4a8a59a7317c4ef10fb75a2e.jpg"
                        alt="First slide"
                    />
                    <Carousel.Caption>

                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src = 'https://skillbox.ru/upload/setka_images/14055326052022_0ed1686442ac630326a48ddcef43684fa02b904b.jpg'
                        alt="Second slide"
                    />

                    <Carousel.Caption>

                    </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src="data:image/jpeg;base64,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"
                        alt="Third slide"
                    />

                    <Carousel.Caption>

                    </Carousel.Caption>
                </Carousel.Item>
            </Carousel>

            <Row className='d-flex'>

                <div>
                    <input
                        value={value}

                        type="text"
                        className="search__input"
                        placeholder="Search..."
                        onChange={(event) => setValue(event.target.value)}
                    />

                </div>

                {filteredCountries.map(device =>
                    <DeviceItem key={device.id} device={device}/>
                )}


            </Row>
        </>
    )
        ;
});

export default DeviceList;
