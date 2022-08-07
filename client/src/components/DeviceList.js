import React, {useContext, useEffect, useState} from 'react';
import DeviceItem from "./DeviceItem";

import {Context} from "../index";
import {Row, Table} from "react-bootstrap";
import {observer} from "mobx-react-lite";
import axios from "axios";





const DeviceList = observer(() => {
    const {device} = useContext(Context)



    const [value , setValue] = useState('')
    const filteredCountries = device.device.filter(product =>{

            return product.name.toLowerCase().includes(value.toLowerCase())

    })


    return (

    <Row className='d-flex'>

        <div >
                    <input
                        value={value}

                        type = "text"
                        className="search__input"
                        placeholder="Search..."
                        onChange={(event) =>setValue(event.target.value)}
                    />

                </div>

        {filteredCountries.map(device =>
            <DeviceItem key={device.id} device={device}/>
        )}


    </Row>
)
    ;
});

export default DeviceList;
