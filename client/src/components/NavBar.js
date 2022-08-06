import React, {useContext} from 'react';
import {Context} from "../index";
import {Button, Container, Nav, Navbar} from "react-bootstrap";
import {ADMIN_ROUTE, BASKET_ROUTE, LOGIN_ROUTE, SHOP_ROUTE} from "../utils/const";
import {observer} from "mobx-react-lite";
import {Link, NavLink} from "react-router-dom";
import {useHistory} from 'react-router-dom';

const NavBar = observer(() => {
    const {user} = useContext(Context)
    const history = useHistory()

    const logOut = () => {
        user.setUser({})
        user.setIsAuth(false)
        localStorage.removeItem('token')
    }

    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <NavLink style={{color: 'white'}} to={SHOP_ROUTE}>Atlas</NavLink>
                {user.isAuth ?

                    <Nav className="ml-auto" style={{color: 'white'}}>
                        <Link to={BASKET_ROUTE}>
                        <Button
                            variant={"outline-light"}
                            // onClick={() => history.push(BASKET_ROUTE)}
                            className='mt-2'
                        >
                            Корзина
                        </Button>
                            </Link>

                        <Button
                            variant={"outline-light"}
                            onClick={() => history.push(ADMIN_ROUTE)}
                            className='mt-2'
                        >
                            Админ панель
                        </Button>
                        <Button
                            variant={"outline-light"}
                            onClick={() => logOut()}
                            className='mt-2'
                        >
                            Выйти
                        </Button>
                    </Nav>
                    :
                    <Nav className="ml-auto" style={{color: 'white'}}>
                        <Button variant={"outline-light"} onClick={() => history.push(LOGIN_ROUTE)}>Авторизация</Button>

                    </Nav>
                }
            </Container>
        </Navbar>


    );
});

export default NavBar;