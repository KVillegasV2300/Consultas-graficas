
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

@app.route('/height')
def height_data():
    height = cs.load_data()[1]
    
    freq_abs = cs.transform_data(cs.freq_abs(height))
    freq_rel = cs.transform_data(cs.freq_rel(height), type='donut')
    freq_acum = cs.transform_data(cs.freq_acum(height))
    mean, median, mode = cs.pack_med(height)
    return render_template('consults/height.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

@app.route('/velocity')
def velocity_data():
    velocity = cs.load_data()[2]
    
    freq_abs = cs.transform_data(cs.freq_abs(velocity))
    freq_rel = cs.transform_data(cs.freq_rel(velocity), type='donut')
    freq_acum = cs.transform_data(cs.freq_acum(velocity))
    mean, median, mode = cs.pack_med(velocity)
    return render_template('consults/velocity.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

@app.route('/color')
def color_data():
    color = cs.load_data()[3]
    
    freq_abs = cs.tranform_data_text(cs.freq_abs(color))
    freq_rel = cs.tranform_data_text(cs.freq_rel(color), type='donut')
    freq_acum = cs.tranform_data_text(cs.freq_acum(color))
    mean, median, mode = cs.pack_med(color, type='str')
    return render_template('consults/color.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

#AQUI ESTBLECEMEOS AHORA SI COMO LA APP PRINCIPAL Y QUE SEA LO PRIMERO EN ARRANCAR
if __name__ == '__main__':
    #SE ACTIVA EL DEBUG PARA QUE LOS CAMBIOS SE HAGAN EN TIEMPO REAL, y no tengasmo que hacer ctr+c una
    #y otra vez..... Es cansado ¿Saben?
    app.run(debug=True)