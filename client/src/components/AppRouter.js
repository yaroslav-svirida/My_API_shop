import React, {useContext} from 'react';
import {BrowserRouter as Routes, Route, Switch} from "react-router-dom";
import {authRoutes, publicRoutes} from "../routes";
import Shop from "../pages/Shop";
import {Context} from "../index";

const AppRouter = () => {
    const {user}  = useContext(Context)
    console.log(user)

    return (

        <Switch>
            {user.isAuth && authRoutes.map(({path, Component}) => {

                    return (
                        <Route key={path} path={path} component={Component} exact/>
                    )
                }
            )}
            {publicRoutes.map(({path, Component}) => {
                console.log(path)
                    return (
                        <Route key={path} path={path} component={Component} exact/>
                    )
                }
            )}
            {/*<Route path="*" component={Shop}/>*/}
        </Switch>
    );
};


export default AppRouter;