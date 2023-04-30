function fill_chart(product, data){
    var json = JSON.parse(data);
    console.log(json);
    let chart_data = create_chart_data(json);
    var canvas = document.getElementById("prices-chart").getContext("2d");
    var main_chart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: chart_data[0],
            datasets: [{
                fill: false,
                data: chart_data[1],
                label: `Цена на ${product}`,
                backgroundColor: 'rgba(0, 0, 255)',
                borderColor: "rgba(0,0,255,0.3)",
            }]
        }
    })
}

function create_chart_data(data){
    let chart_data = [];
    let colors = [];
    let labels = [];
    for(const key in data){
        labels.push(key);
        chart_data.push(data[key]["average"]);
        colors.push('rgba(0, 0, 0)');
    }
    let newArray = [labels, chart_data, colors];
    return newArray;
}

export {fill_chart};