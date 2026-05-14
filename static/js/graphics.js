
function clean_graph(id){

    document.getElementById(id).innerHTML = '';
}

function freq_abs_graph(data, id){
    clean_graph(id);

    new_data = eval('[' + data + ']');

    new Morris.Bar({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Frecuencia'],
        resize: true
    });

}

function freq_rel_graph(data, id){
    clean_graph(id);

    new_data = eval('[' + data + ']');

    new Morris.Donut({
        element: id,
        data: new_data,
        resize: true
    });
}

function freq_acum_graph(data, id){
    clean_graph(id);

    new_data = eval('[' + data + ']');
    new Morris.Line({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Frecuencia Acumulada'],
        resize: true
        
    });
}

function pol_frec_graph(data, id){
    clean_graph(id);

    new_data = eval('[' + data + ']');

    new Morris.Line({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Poligono de Frecuencia'],
        resize: true
    });
}