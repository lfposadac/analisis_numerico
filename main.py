#Luis Fernando Posada Cano
try:
   from flask import Flask, render_template, request, url_for
except:
   #Instalar los módulos necesarios
   import os
   try:
      os.system('pip install --upgrade')
      os.system('pip install flask')
      from flask import Flask, render_template, request
   except:
      print('Your OS doesn\'t understand default commands for install dependencies, so try run this file as administrator, or install flask module for yourself')
      import sys
      sys.exit()

try:
   import numpy as np
except:
   #Instalar los módulos necesarios
   import os
   try:
      os.system('pip install --upgrade')
      os.system('pip install numpy==1.19.3')
      import numpy as np
   except:
      print('Your OS doesn\'t understand default commands for install dependencies, so try run this file as administrator, or install numpy module for yourself')
      import sys
      sys.exit()

#IControlador de importación
import os
from numericalMethods import NM
from controllerNM import ControllerNM
from controllerMatrix import ControllerMatrix
from controllerConversor import ControllerConversor
import sys

app = Flask(__name__)
nmc = ControllerNM(NM())
mc = ControllerMatrix()
cc  = ControllerConversor()

@app.route('/', methods=["GET", "POST"])
def index():
   if request.method == "POST":
      cc.setCSS(request.form['css'])
   return render_template('index.jinja',cc=cc)


@app.route('/guie', methods=["GET", "POST"])
def guie():
   if request.method == "POST":
      cc.setCSS(request.form['css'])
   return render_template('guie.jinja',cc=cc)

@app.route('/numericalMethods', methods=["GET", "POST"])
def numericalMethods():
   """
   Si el método numérico necesita el método, entonces el resultado de la vista es falso
   de lo contrario, si necesita variables para generar el resultado del método, entonces
   el resultado es cierto
   luego el resultado puede volver a numericalMethods, por lo que
   el resultado es falso y no existe un método
   """
   if request.method == "POST" and len(request.form) == 1:
      nmc.setMethod(request.form['method'])
      nmc.setResult(False)
   elif request.method == "POST" and len(request.form) > 1:
      nmc.setUp(request.form)
      nmc.setMethod(False)
      nmc.setResult(True)
   else:
      nmc.setMethod(False)
      nmc.setResult(False)
   return render_template('numericalMethods.jinja', nmc=nmc,cc=cc)

@app.route('/makeMatrix', methods=["GET", "POST"])
def makeMatrix():
   data = None
   if request.method == "POST" and len(request.form) == 1 and not mc.getN():
      mc.setN(request.form['n'])
      mc.setResult(False)
   elif request.method == "POST" and '0' in request.form:
      data = request.form
      mc.setN(False)
      mc.setResult(True)
   else:
      mc.setN(False)
      mc.setResult(False)
   return render_template('makeMatrix.jinja', mc=mc,data=data,cc=cc)

@app.route('/conversor', methods=["GET", "POST"])
def conversor():
   data = None
   if request.method == "POST":
      data = request.form
      cc.setResult(True)
   else:
      cc.setResult(False)
   return render_template('conversor.jinja', cc=cc,data=data)

@app.route('/user/<name>')
def user(name):
   return render_template('user.jinja', cc=cc, name=name)

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.jinja', cc=cc,e=e), 404


#fragmento para actualizar archivos estáticos en la depuración web
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
   app.run(debug=False)