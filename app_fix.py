import flask
from flask import render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if flask.request.method == 'POST':
        with open('model_matrix3_1.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        pl= float(flask.request.form['Плотность, кг/м3']) 
        my = float(flask.request.form['Модуль упругости, ГПа'])
        ko = float(flask.request.form['Количество отвердителя, м.%'])
        seg = float(flask.request.form['Содержание эпоксидных групп,%_2'])
        tv = float(flask.request.form['Температура вспышки, С_2'])
        pp = float(flask.request.form['Поверхностная плотность, г/м2'])
        myp = float(flask.request.form['Модуль упругости при растяжении, ГПа'])
        pr = float(flask.request.form['Прочность при растяжении, МПа'])
        ps = float(flask.request.form['Потребление смолы, г/м2'])
        yn = float(flask.request.form['Угол нашивки, град']) 
        sn = float(flask.request.form['Шаг нашивки']) 
        pn = float(flask.request.form['Плотность нашивки'])    

        X = np.array([pl,my,ko,seg,tv,pp,myp,pr,ps,yn,sn,pn]).reshape(1,-1)
        y_matrix_pred2= loaded_model.predict(X)
        # y_matrix_pred2= loaded_model.predict([[pl], [my], [ko], [seg], [tv], [pp], [my], [pr], [ps], [yn], [sn], [pn]])

        return render_template('main.html', result = y_matrix_pred2) 

if __name__ == '__main__':
    app.run()      