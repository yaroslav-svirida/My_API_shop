import {makeAutoObservable, observable} from "mobx";

export default class DeviceStore {
    constructor() {
        this._types = [
            {id: 1, name: 'Холодильники'},
            {id: 2, name: 'Смартфоны'},
            {id: 3, name: 'Ноутбуки'},
            {id: 4, name: 'Телевизоры'}

        ]
        this._brands = []
        this._orders = []
        this._basket = []
        this._devices = []
        this._selectedType = {}
        this._selectedBrand = {}
        makeAutoObservable(this)
    }

    setTypes(types) {
        this._types = types
    }

    setBrands(brands) {
        this._brands = brands
    }

    setDevices(devices) {
        this._devices = devices
    }

    setDevicesAmount(devices, amount) {
        devices.product_amount = amount
    }

    setSelectedType(type) {
        this._selectedType = type
    }

    setSelectedBrand(brand) {
        this._selectedBrand = brand
    }

    setBasket(basket) {

        this._basket = observable(basket.map(b => ({...b,setAmount: (amount) => this.product_amount = amount})))
    }

    get basket() {
        return this._basket
    }

    get types() {
        return this._types
    }

    get brands() {
        return this._brands
    }

    get device() {
        return this._devices
    }

    get selectedType() {
        return this._selectedType
    }

    get selectedBrand() {
        return this._selectedBrand
    }

}