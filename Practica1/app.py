from flask import Flask, render_template, request, redirect
app = Flask (__name__)
#----------------------rutas
@app.route("/") 
def index():
       
    return render_template ("index.html")

@app.route("/contacto", methods=['GET','POST']) 
def contacto():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        ap= request.form.get("apellidos")
        tel=request.form.get("telefono")
        correo=request.form.get("correo")
        lugar=request.form.get("poblacion")
        mensaje=request.form.get("descripcion")
        return render_template("salida.html",nombre=nombre, ap=ap, tel=tel, correo= correo, lugar=lugar, mensaje=mensaje)
    return render_template ("contacto.html")

@app.route("/noticias") 
def noticias():
    return render_template ("noticias.html")

@app.route("/quienessomos") 
def quienessomos():
       
    return render_template ("quienessomos.html")

@app.route("/servicios") 
def servicios():
       
    return render_template ("servicios.html")
@app.route("/nota") 
def nota():
    return ("<h1> Página en desarrollo</h1>" )
#-------------fin rutas
if __name__ == "__main__":
    app.run(debug=True)