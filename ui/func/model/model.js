class Users{
    xhr;
    #method;

    #set_method(meth){
        this.#method = meth;
    }

    constructor(method){
        this.#set_method(method);
        this.xhr = new XMLHttpRequest();
        this.xhr.open('POST', "../func/querries/users_queries.php");
        this.xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let xhr = this.xhr;
        this.xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                console.log(xhr.responseText);
            }
        };
    }

    create_user(data) {
        let xhr = this.xhr;
        this.xhr.onload = function () {
            let status = xhr.status;
            let response = xhr.response;
            console.log(`Загружено: ${status} ${response}`);
            window.location.href = '../pages/login.php';
        }

        this.xhr.send(`data=${JSON.stringify(data)}&method=${this.#method}`);
    }

    get_user(data){
        let xhr = this.xhr;
        let answer;
        this.xhr.onload = function () {
            console.log(`Загружено: ${xhr.status} ${xhr.response}`);
            answer = JSON.parse(xhr.response);
            if(answer["results"] == 1)
            {
                let user = answer["users"][0];
                if(user["password"] == data["password"])
                {
                    window.location.href = `../func/session/set_session.php?login=${data["login"]}`;
                }else
                {
                    console.log("FALSE");
                }
            }
        }

        this.xhr.send(`login=${data["login"]}&method=${this.#method}`);
    }
}

class Products{
    #method;
    xhr;
    #set_method($meth){
        this.#method = $meth;
    }

    constructor(method){
        this.#set_method(method);
        this.xhr = new XMLHttpRequest();
        this.xhr.open('POST', "../func/querries/products_queries.php");
        this.xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let xhr = this.xhr;
        this.xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                console.log(xhr.responseText);
            }
        };
    }

    get_products(page, search){
        let xhr = this.xhr;
        let answer;
        let start = new Date().getTime();
        this.xhr.onload = function (){
            let end1 = new Date().getTime();
            console.log(`Get answer in ${end1 - start} ms`);
            answer = JSON.parse(xhr.response);
            let products = answer["products"];
            create_products_block(products);
            let pages_count = Math.ceil(answer.count / 10);
            set_pagination_info(page, answer["count"]);
            create_pages_block(pages_count, page);
            let end2 = new Date().getTime();
            console.log(`Script ended in ${end2 - end1} ms`);
        }

        this.xhr.send(`method=${this.#method}&page=${page}&search=${search}`);
    }

    create_product(data){
        let xhr = this.xhr;
        this.xhr.onload = function (){
            console.log(`Загружено: ${xhr.status} ${xhr.response}`);
            window.location.reload();
        }

        this.xhr.send(`method=${this.#method}&data=${JSON.stringify(data)}`);

    }
}

class Prices{
    #method;
    xhr;
    #set_method($meth){
        this.#method = $meth;
    }

    constructor(method){
        this.#set_method(method);
        this.xhr = new XMLHttpRequest();
        this.xhr.open('POST', "../func/querries/prices_queries.php");
        this.xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        let xhr = this.xhr;
        this.xhr.onreadystatechange = function () {
            if (xhr.readyState == 4) {
                console.log(xhr.responseText);
            }
        };
    }


    get_prices(id){
        let xhr = this.xhr;
        let answer;
        this.xhr.onload = function (){
            console.log(`Загружено: ${xhr.status} ${xhr.response}`);
            answer = JSON.parse(xhr.response);
            let prices = answer["products"];
            create_prices_block(prices);
        }

        this.xhr.send(`method=${this.#method}&id=${id}`);
    }
}

import {create_pages_block, set_pagination_info, create_products_block, create_prices_block} from "./model_functions.js";
export {Users, Products, Prices};
