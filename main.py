
#Aqui como reocmendacion que se dio es utilizar FLASK para crear una app web sencilla
from flask import Flask, render_template

#AQUI SIMPLEMENTE IMPORTAMOS LAS CONSULTAS
import consults as cs

#Aqui se crea la aplicacion, ademas de indicar que esta es la aplicacion principal al servdior
app = Flask(__name__)

#Aqui se define la ruta principal de esta aplicacion que sera referenciada mas adelante
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weight')
def weight_data():

    weight = cs.load_data()[0]
    
    freq_abs = cs.transform_data(cs.freq_abs(weight))
    freq_rel = cs.transform_data(cs.freq_rel(weight), type='donut')
    freq_acum = cs.transform_data(cs.freq_acum(weight))
    mean, median, mode = cs.pack_med(weight)
    return render_template('consults/weight.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

#AQUI ESTBLECEMEOS AHORA SI COMO LA APP PRINCIPAL Y QUE SEA LO PRIMERO EN ARRANCAR
if __name__ == '__main__':
    #SE ACTIVA EL DEBUG PARA QUE LOS CAMBIOS SE HAGAN EN TIEMPO REAL, y no tengasmo que hacer ctr+c una
    #y otra vez..... Es cansado ¿Saben?
    app.run(debug=True)