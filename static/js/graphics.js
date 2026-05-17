//Aqui es donde van las poderosas graficas gracias a morris

//Teniendo primeramente esta funcion para limpiar y no se dupliquen las grficas como en el ejemplo de la profa juasjausj
function clean_graph(id){
    document.getElementById(id).innerHTML = '';
}

//Aqui empezamos con funciones genericas, para mantener esto mas limpio....
function freq_abs_graph(data, id, type="num"){
    //Limpiamos la grafica actual.
    clean_graph(id);

    //No le hagan mucho caso a este sistema, salio improvisado cuando me di cuenta del erro que cometi en colores (ultima consulta que hice)
    if (type == "num") {
        new_data = eval('[' + data + ']');
    } else if (type == "char") {
        new_data = data
    }

    //Ahora si lasgraficas
    new Morris.Bar({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Frecuencia'],
        resize: true
    });

}

//---------------------------------------------------------------------------------------\\
//APARTIR DE AQUI REPLICO LA MISMA LOGICA PERO CON DIFERENTES TIPOS DE GRAFICAS :DDDD\\
//---------------------------------------------------------------------------------------\\
function freq_rel_graph(data, id, type="num"){
    clean_graph(id);

    if (type == "num") {
        new_data = eval('[' + data + ']');
    } else if (type == "char") {
        new_data = data
    }

    new Morris.Donut({
        element: id,
        data: new_data,
        resize: true
    });
}

function freq_acum_graph(data, id, type="num"){
    clean_graph(id);

    if (type == "num") {
        new_data = eval('[' + data + ']');
    } else if (type == "char") {
        new_data = data
    }

    new Morris.Line({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Frecuencia Acumulada'],
        resize: true,
        parseTime: false //ESTO, DE MANERA NORMAL SALE COMO CIN DATOS DEL CLIMA, ESTO LO QUITA JAJAJAJA
    });
}

function pol_frec_graph(data, id, type="num"){
    clean_graph(id);

    if (type == "num") {
        new_data = eval('[' + data + ']');
    } else if (type == "char") {
        new_data = data
    }

    new Morris.Line({
        element: id,
        data: new_data,
        xkey: 'x',
        ykeys: ['y'],
        labels: ['Poligono de Frecuencia'],
        resize: true,
        parseTime: false
    });
}