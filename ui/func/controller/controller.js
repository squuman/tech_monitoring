function get_inputs_data(){
    let values = document.getElementsByClassName("form-control");
    return values;
}

function CreateUser(){
    let users = new Users('POST');
    let inputs = get_inputs_data();
    let now = new Date();
    now = now.toISOString();
    let data = 
    {
        "login": inputs[0].value,
        "name": inputs[1].value,
        "password": inputs[2].value,
        "createdAt": now,
        "updatedAt": now
    }
    users.create_user(data);
}

function CreateProduct(){
    let products = new Products('POST');
    let input = document.getElementById("new-product-name").value;
    let now = new Date();
    now = now.toISOString();
    let data=
    {
        "title": input,
        "createdAt": now,
        "updatedAt": now
    }
    products.create_product(data);
}

function GetUser(){
    let users = new Users('GET');
    let inputs = get_inputs_data();
    let data = 
    {
        "login": inputs[0].value,
        "password": inputs[1].value
    }
    users.get_user(data);
}

function GetProducts(page, search){
    let products = new Products('GET');
    products.get_products(page, search);
}

function GetPrices(id){
    let prices = new Prices('GET');
    prices.get_prices(id);
}

function FillChart(product, data){
    fill_chart(product, data);
}

export {CreateUser, GetUser, GetProducts, CreateProduct, GetPrices, FillChart};

import {Users, Products, Prices} from "../model/model.js";
import {fill_chart} from "../model/chart.js";