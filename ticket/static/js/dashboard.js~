function draw_type_chart(data) {
    ctx = document.getElementById("type_chart").getContext('2d');
   
    var itm_count = 0;
    labels = []
    values = []
    colours = []
    for (dt in data) {
        labels.push(data[dt].fields.label);
        values.push(data[dt].fields.tickets);
        r = Math.floor(Math.random() * 200);
        g = Math.floor(Math.random() * 200);
        b = Math.floor(Math.random() * 200);
        colours.push('rgb(' + r + ', ' + g + ', ' + b + ')');
    }
    window.type_chart = new Chart(ctx, {
    type: 'pie',
    
    options: {
        plugins: {
            title: {
                display: false,
                text: 'Ticket Types'
            }
        }
    },
    data: {
        labels: labels,
        datasets: [
            {
                label: "Types",
                data: values,
                backgroundColor: colours
            }
            
        ]
    }
})
};

function draw_time_chart(data) {
    ctx = document.getElementById("time_chart").getContext('2d');
   
    var itm_count = 0;
    labels = []
    values = []
    colours = []
    for (dt in data) {
        console.log(data[dt].fields);
        labels.push(data[dt].fields.mean_response);
        values.push(data[dt].fields.ticket_count);
        r = Math.floor(Math.random() * 200);
        g = Math.floor(Math.random() * 200);
        b = Math.floor(Math.random() * 200);
        colours.push('rgb(' + r + ', ' + g + ', ' + b + ')');
    }
    window.type_chart = new Chart(ctx, {
    type: 'bar',
    
    options: {
        plugins: {
            title: {
                display: false,
                text: 'Ticket Types'
            }
        }
    },
    data: {
        labels: labels,
        datasets: [
            {
                label: "Ticket count per mean response",
                data: values,
                backgroundColor: colours
            }
            
        ]
    }
})
};
$.getJSON("/chart/type/top",draw_type_chart);
$.getJSON("/chart/ticket/times",draw_time_chart);
