import {$authHost, $authHostth, $host} from "./index";
import jwt_decode from "jwt-decode";

export const registration = async (email, password) => {
    const {data} = await $host.post('http://127.0.0.1:8000/api/users/', {email, password, role: 'ADMIN'})
    localStorage.setItem('token', data.access)
    return jwt_decode(data.access)

}

export const login = async (email, password) => {
    const {data} = await $host.post('http://127.0.0.1:8000/api/jwt/create/', {email, password})
    localStorage.setItem('token', data.access)
    return jwt_decode(data.access, { header: true })

}

// export const registration = async () => {
//     const response = await $authHost.post('http://127.0.0.1:8000/api/users/', )
//     return response
//
// }