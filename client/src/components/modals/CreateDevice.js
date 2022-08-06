import React, {useContext, useState} from 'react';
import {Button, Col, Dropdown, Form, Row} from "react-bootstrap";
import Modal from "react-bootstrap/Modal";
import {Context} from "../../index";

const CreateDevice = ({show, onHide}) => {
    const {device} = useContext(Context)
    const [info, setInfo] = useState([])
    const addInfo = () => {
        setInfo([...info, {title: '', description: '', number: Date.now()}])
    }
    const removeInfo = (number) => {
        setInfo(info.filter(i => i.number !== number))
    }

    return (
        <Modal
            show={show}
            onHide={onHide}

            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    Добавить устройство
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Dropdown className={'mt-2 mb-2'}>
                        <Dropdown.Toggle>Выберите тип</Dropdown.Toggle>
                        <Dropdown.Menu>
                            {device.types.map(type =>
                                <Dropdown.Item key={type.id}>{type.name}</Dropdown.Item>
                            )}
                        </Dropdown.Menu>
                    </Dropdown>

                    <Dropdown className={'mt-2 mb-2'}>
                        <Dropdown.Toggle>Выберите тип</Dropdown.Toggle>
                        <Dropdown.Menu>
                            {device.types.map(type =>
                                <Dropdown.Item key={type.id}>{type.name}</Dropdown.Item>
                            )}
                        </Dropdown.Menu>
                    </Dropdown>

                    <Form.Control
                        className='mt-3'
                        placeholder='Введите название устройства'
                    />

                    <Form.Control
                        className='mt-3'

                        type='number'
                    />

                    <Form.Control
                        className='mt-3'
                        placeholder='Введите название устройства'
                        type='file'
                    />
                    <hr/>
                    <Button
                        variant='outline-dark'
                        onClick={addInfo}
                    >
                        Добавить новое свойство</Button>
                    {
                        info.map(i =>
                            <Row className='mt-4' key ={i.number}>
                                <Col md={4}>
                                    <Form.Control
                                        placehilder='Введите название свойства'
                                    />
                                </Col>
                                <Col md={4}>
                                    <Form.Control
                                        placehilder='Введите описание свойства'
                                    />
                                </Col>
                                <Col md={4}>
                                    <Button
                                        onClick = {()=>removeInfo(i.number)}
                                        variant={"outline-danger"}>Удалить</Button>
                                </Col>

                            </Row>)


                    }

                </Form>

            </Modal.Body>
            <Modal.Footer>
                <Button variant='outline-danger' onClick={onHide}>Закрыть</Button>
                <Button variant='outline-success' onClick={onHide}>Добавить</Button>
            </Modal.Footer>
        </Modal>
    );
};

export default CreateDevice;