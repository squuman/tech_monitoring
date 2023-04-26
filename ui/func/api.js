var baseUrl = '127.0.0.1:8000/'

function create_user(data) {
    var xhr = new XMLHttpRequest();
    xhr.open(baseUrl + 'users', 'POST');

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            console.log(xhr.responseText);
        }
    }

    xhr.send(data);
}

function create_product(data) {
    var xhr = new XMLHttpRequest();
    xhr.open(baseUrl + 'products', 'POST');

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            console.log(xhr.responseText);
        }
    }

    xhr.send(data)
}

function get_products(data) {
    var xhr = new XMLHttpRequest();
    xhr.open(baseUrl + 'products', 'GET');

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            console.log(xhr.responseText);
        }
    }

    xhr.send(data)

}
