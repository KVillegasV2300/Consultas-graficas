import pandas as pd

#Primero cargamos los datos directamente del csv 
def load_data():
    #primero leemos los datos dados
    df = pd.read_csv('datos.csv')

    #aqui limpiados los datos y extraemos cada columna
    weight = df['peso'].dropna()  #eliminamos los valores nulos
    height = df['altura'].dropna()
    velocity = df['velocidad'].dropna()
    color = df['color'].dropna()

    return weight, height, velocity, color

#una vez cargados nos piden primerooo:

#frecuencia absolutas
def freq_abs(data):
    #contamos la frecuencia de cada valor unico en la columna
    freq = data.value_counts().sort_index()
    return freq

#Frecuencias relativas
def freq_rel(data):
    #calculamos la frecuencia relativa de cada valor unico en la columna
    freq = data.value_counts(normalize=True).sort_index()

    #redondeamos a 2 decimales por que si son muchisimos decimales se ve feo en la grafica xD
    freq = round(freq, 2)
    return freq

#Frecuencias acumuladas
def freq_acum(data):
    #calculamos la frecuencia acumulada de cada valor unico en la columna :b
    freq = data.value_counts().sort_index().cumsum()
    return freq

#Media. mediana y moda

def pack_med(data, type='num'):

    if type == 'str':
        #si es categorica, la media y mediana no tienen sentido, asi que la ponemos como N/A
        mean = 'N/A'
        median = "N/A"
        mode = data.mode()[0]  #la moda puede tener varios valores, pero nos quedamos con el primero
    elif type == 'num':
        #calculamos la media, mediana y moda de la columna si son datos numerics
        mean = round(data.mean(), 2)  #redondeamos a 2 decimales
        median = round(data.median(), 2)  #redondeamos a 2 decimales
        mode = data.mode()[0]  #la moda puede tener varios valores, pero nos quedamos con el primero
    
    return mean, median, mode


#Para seguyir un formato similar a la de la profa se convierte el resultado en un formato legible para Morris
def transform_data(data, type='bar'):
    script = ""

    if type == 'bar':
        for v, c in data.items():
            script += "{x: " + str(v) + ", y: " + str(c) + "},"
    elif type == 'donut':
        for v, c in data.items():
            script += "{label: " + str(v) + ", value: " + str(c) + "},"
    
    script = script[:-1]  #eliminar la ultima coma
    
    return script

#OKAY AQUI SI ME PASE DE ESTUDPIDO, Y CON ELSISTEMA QUE MONTE NO CONSIDERE LAS "" Y '' DENTRO DEL ARGUMENTO DE ONCLIC
#POR LO QUE HICE OTRA FUNCION PARA TRANSFORMAR LOS DATOS DE LAS CATEGORICAS, PARA QUE EN VEZ DE PONER {x: rojo, y: 5} PONGA {x: 'rojo', y: 5} Y ASI SI FUNCIONE CON LOS STRING
#ADEMAS DE AGREGAR UN ARGUMENTO NUEVO EN LOS Js
def tranform_data_text(data, type='bar'):
    script = ""

    if type == 'bar':
        for v, c in data.items():
            script += """{x: """ + f"'{str(v)}'" + """, y: """ + f"{str(c)}" + """},"""
    elif type == 'donut':
        for v, c in data.items():
            script += """{label: """ + f"'{str(v)}'" + """, value: """ + f"{str(c)}" + """},"""
    
    script = script[:-1]  #eliminar la ultima coma
    script = "[" + script + "]"  #agregar corchetes para que sea un array de objetos
    return script