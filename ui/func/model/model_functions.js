function create_products_block(prods){
    prods.forEach(product => {
        let elem = document.createElement("tr");
        elem.classList.add("odd");
        elem.innerHTML = `<td class="dtr-control"><a href="./products_list_page.php?id=${product["id"]}" class="black_link">${product["title"]}</a></td>`;
        document.getElementById("products_table").appendChild(elem);
    });
}

function create_prices_block(prices){
    let tbody = document.getElementById("prices-table-body");
    prices.forEach(price => {
        let date = moment(price["createdAt"])

        let tr = document.createElement("tr");
        let td1 = document.createElement("td");
        let td2 = document.createElement("td");
        let td3 = document.createElement("td");
        td1.innerHTML = price["price"];
        td2.innerHTML = price["storage"];
        td3.innerHTML = date.format('DD.MM.YYYY');
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tbody.appendChild(tr);
    });
}

function set_pagination_info(current, count_entr){
    let info = document.getElementById("example2_info");
    let from = (current - 1) * 10 + 1;
    (from > count_entr) ? from = count_entr: false;
    let to = current * 10;
    (to > count_entr)? to = count_entr: false;
    info.innerHTML = `Showing ${from} to ${to} of ${count_entr} entries`;

}

function create_pages_block(count, current){
    let previous = document.createElement("li");
    previous.classList.add("paginate_button");
    previous.classList.add("page-item");
    previous.classList.add("previous");
    if(current <= 1)
    {
        previous.classList.add("disabled");
    }
    previous.innerHTML = `<a href="?page=${current - 1}" aria-controls="example2" data-dt-idx="0" tabindex="0" class="page-link">Previous</a>`;
    document.getElementById("pages").appendChild(previous);

    for(let i = 0; i < count; i++)
    {
        let elem = document.createElement("li");
        elem.classList.add("paginate_button");
        elem.classList.add("page-item");
        if(i + 1 == current)
        {
            elem.classList.add("active");
        }
        elem.innerHTML = `<a href="?page=${i + 1}" aria-controls="example2" data-dt-idx="${i + 1}" tabindex="0" class="page-link">${i + 1}</a>`;
        document.getElementById("pages").appendChild(elem);
    }

    let next = document.createElement("li");
    next.classList.add("paginate_button");
    next.classList.add("page-item");
    next.classList.add("next");
    if(current == count)
    {
        next.classList.add("disabled");
    }
    next.innerHTML = `<a href="?page=${current + 1}" aria-controls="example2" data-dt-idx="${count + 1}" tabindex="0" class="page-link">Next</a>`;
    document.getElementById("pages").appendChild(next);
}

export {create_pages_block, set_pagination_info, create_products_block, create_prices_block};