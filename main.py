from flask import Flask, render_template, url_for, request, make_response, session, redirect, jsonify
from Datos.usuario import Usuario
from Datos.receta import Receta
from os import environ
import json
import base64
import csv

app = Flask(__name__)
usuario1 = Usuario("Usuario","Maestro","admin","admin")
usuarios = [usuario1]
user=None
app.secret_key = b'pythonipc'

receta1=Receta("Administrador","Fiambre","Plato tradicional de Guatemala que se come el 1 de noviembre, día en que, como en muchos países católicos, se celebra el Día de Todos los Santos."
,"2 libras ejote \n 6 zanahoria grandes\n 0.5 libra jamón \n 6 unidades Embutidos varios \n 0.5 libra queso craft, mozzarella, seco, fresco Vinagre de manzana, tomillo, laurel al gusto Pimienta blanca, sal \n 2 latas Cebollas encurtidas \n 1 lata Chile pimiento, elotitos y pepinillos encurtidos \n Lechuga lisa \n rábanos y chile morrón  \n 4 huevos cocidos" +
    "Perejil Pacayas Bruselas 1 libra Cebollas en agajos","1. Cocer ejote y zanahoria bruselas y pacayas con laurel y sal\n"
    +"2. Cocer embutidos uno por uno en la misma agua y reservar el agua\n"+"3. Dejar enfriar verduras, agua de embutidos y embutidos por separado\n"
    +"4. Licuar agua de embutidos con 1/2 taza de vinagre, perejil, mostaza y sal. Colar en un recipiente plástico y reservar\n"
    +"5. Picar en rodajas y tiras los embutidos y quesos\n"+"6. Unir en un recipiente plástico todos los ingredientes y reservar\n"+"7. Mezclar caldillo con verdura, agregar tomillo, laurel, vinagre y sal al gusto\n"
    +"8. Dejar una parte de embutidos y quesos por aparte para adornar\n"+"9. Dejar reposar 24 horas en el refrigerador y servir","162","https://www.guatemala.com/fotos/201710/Tipos-de-fiambre-que-se-hacen-en-Guatemala-para-el-Dia-de-Todos-los-Santos-885x500.jpg",0)

receta2=Receta("Administrador","Ponche de Frutas", "El ponche de frutas navideño es una infusión que se consume en Guatemala tradicionalmente durante las posadas y en la Nochebuena."
,"1 piña \n1 papaya\n4 onzas de pasas\n1 taza de uvas\n1 plátano\n4 manzanas rojas\n1 taza de coco fresco en cuadritos\n2 rajas de canela\n4 onzas de ciruelas\nPimienta gorda al gusto\nClavos de olor\n12 tazas de agua\nAzúcar al gusto",
"1. Lavar y después cortar las frutas en pequeños cuadros.\n2. Agregar 12 tazas de agua en una olla grande y hervirla.\n3. Después agregar las frutas, canela, pimienta gorda, clavos de olor, uvas, pasas, ciruelas y el azúcar.\n4. Cocinar aproximadamente por media hora a fuego medio.\n5. De preferencia servirlo bien caliente.",
"30","https://www.mexicodesconocido.com.mx/wp-content/uploads/2019/11/ponche-festival-tepoztlan.jpg",1)


receta3=Receta("Administrador","Tamalitos de Elote","Tipo de tamal de temporada de Guatemala que se hace con maíz fresco tienen la característica de ser dulces son fáciles de preparar y quedan deliciosos.",
"1 libra y media de tomate ciruelo maduro.\n2 chiles pimientos.\n3 chiles guaques.\n2 onzas de ajonjolí.\n2 onzas de pepitoria.\n1 raja pequeña de canela.\n1 onza de manteca de cerdo.\nAchiote.\nSal.\n"
+"1 libra y media de masa de maíz.\n8 onzas de manteca de marrano.\n1 maleta de hojas de plátano.\n2 maletas de hojas de maxán.\n3 chiles pimientos para ser asados.\n4 onzas de aceitunas.\n4 onzas de alcaparras.\n2 libras de carne de cerdo.",
"1. Primero, comenzar por cortar las hojas de maxán en cuadros, lavar y poner a secar al sol.\n2. Cortar las hojas de plátano en cuadros de 25 centímetros aproximadamente y poner a cocer en agua por 10 minutos.\n"
+"3. Poner las tiras de cibaque en remojo para que se ablanden.\nRECADO:\n1. Entonces, proceder a picar los tomates.\n2. Lavar y quitar las semillas del chile guaque.\n3. Agregar un poco de mantequilla al sartén y cocinar los ingredientes anteriores.\n"
+"4. Luego, triturar la mezcla y sazonar con un poco de sal el ajonjolí, la pepitoria, canela, achiote y sal.\n5. Si se desea agregar tocino, cortarlo en pedacitos y agregarlo al recado.\n6. Cortar la carne de cerdo en cuadritos de tamaño regular y agregar al recado.\n"
+"7. En un sartén derretir un poco de manteca y freír la carne con el recado\n8. Por separado asar los chiles pimientos, pelar, partir, desvenar y quitar las semillas.\n9. Cortar los chiles en tiras y reservar.\nMASA\n"
+"1. Deshacer y mezclar la masa de maíz en medio litro de agua y licuar.\n2. Poner a hervir 4 tazas de agua y agregar la masa, revolviendo constantemente.\n3. Cuando la masa esté espesa, batir y añadir bastante sal. Recordar que tiende a perderse el sabor de la sal durante la cocción.\n"
+"4. Si la masa está demasiado espesa, se le puede agregar agua caliente poco a poco.\n5. Cuando esté lista la masa, retirar del fuego y agregar la manteca.\n6. Batir hasta que la manteca se mezcle bien y la masa se ponga un poco brillante.\nTAMALES:\n"
+"1. Colocar una hoja de plátano sobre una de maxán en diagonal.\n2. En el centro agregar una porción de masa y recado abundante, al igual que la carne.\n3. También añadir aceitunas, alcaparras, pasas y tiras de chile pimiento.\n4. Doblar las hojas para formar un paquete.\n"
+"5. Amarrar con tiras de cibaque.\n6. En el fondo de una olla poner las hojas que sobren, 4 tazas de agua y hervir.\n7. Cuando comience a hervir, colocar los tamales.\n8. Cubrir la olla con más hojas y una manta.\n9.Finalmente, hervir por aproximadamente 1 hora y media.",
"120","https://i2.wp.com/www.revistalatinanc.com/wp-content/uploads/2019/10/TamalesEloteMilRecetas-1.jpeg",2)

receta4=Receta("Administrador","Ceviche de Camarón","El ceviche de camarón en Guatemala es un plato que ha ganado gran popularidad por su delicioso sabor que combina en la época de calor.",
"5 limones.\n1 ramo de apio.\n2 cebollas.\n5 tomates.\n3 ramas de hierbabuena.\n1 manojo de cilantro.\nSalsa inglesa.\n1 libra de camarón.\nSal.","1. Limpiar los camarones, pelarlos y quitarles la cabeza.\n"
+"2. Colocar los camarones en una olla con agua y hervirlos por 2 minutos.\n3. Retirar el agua y colocar los camarones en un recipiente hondo.\n4. Cubrir los camarones con el jugo de los limones y un chorro de salsa inglesa.\n"
+"5. Dejar reposando por una noche en el refrigerador.\n6. Picar las hierbas, cebolla, apio y el tomate y agregarlo al tomate.\n7. Agregar una pizca de sal y chile cobanero al gusto.\n8. Dejar reposar en el refrigerador de nuevo. Esta vez por media hora.\n"
+"9. Servir con galletas saladas y disfrutar.","60","https://images-gmi-pmc.edge-generalmills.com/c3039468-71fb-49bc-b886-822c67cf7c51.jpg",3)

receta5=Receta("Administrador","Rellenitos","Es un plato de puré de plátanos dulces rellenos con una mezcla de frijoles refritos, chocolate y canela.","6 plátanos maduros.\n1.5 tazas agua.\n1 raja de canela.\n½ taza miga pan.\n1 taza frijol negro.\n½ taza azúcar o al gusto.\n½ cucharadita canela.\n2 onzas chocolate.\n½ taza harina.\nAceite para freír.",
"1. Primero, cortar el plátano en trozos y cocinar en el agua, con canela en raja y azúcar.\n2. Luego retirar la cáscara, hacerlos puré y agregar la miga de pan.\n3. Freír el frijol previamente cocinado y licuado espeso con el azúcar, la canela en polvo y el chocolate.\n4. Darle al plátano forma de tortita, rellenar con una cucharada de frijol y cerrar en forma de rellenito.\n"
+"5. Pasar por harina y freír en aceite.\n6. Espolvorear con azúcar.\n7. Si se desea se puede sustituir el frijol por manjar.","90","https://img-global.cpcdn.com/recipes/5b9111851382617a/1200x630cq70/photo.jpg",4)

receta6=Receta("Administrador","Chuchitos","Es un plato nacional, tradicional y emblemático de la gastronomía Guatemalteca, elaborado a base de masa de maíz, y generalmente va mezclado de un recado o salsa de tomate y con un relleno que puede ser de carne de pollo o de cerdo.",
"2 manojos de hojas de mazorcas de maíz secas.\n1 kilo de harina de maíz.\n1/4 de kilo de manteca vegetal derretida.\n1/4 de taza de aceite vegetal.\n2 cucharaditas de sal.\n1 cucharadita de consomé de pollo.\nRECADO\n1 chile guaque.\n1/4 cucharadita de comino en polvo.\n1 cucharadita de sal.\n1/8 de cucharadita de pimienta.\n1 kilo de carne de cerdo en trozos.\n12 tomates",
"1. Lavar bien las hojas de mazorca y dejarlas en remojo para que se ablanden.\n2. Mezclar el harina con la manteca, sal y el consomé.\n3. Agregar un poco de agua tibia para suavizarla, no debe quedar muy aguada.\n4. Para hacer el recado, picar los tomates.\n5. Lavar y quitar las semillas del chile.\n6. Agregar una cucharadita del aceite vegetal en un sartén y freír el chile con el comino.\n7. Luego, moler el tomate y chile junto. Puede hacerse en una trituradora.\n"
+"8. Sazonar con la sal y pimienta\n9. Cuando ya esté frío, agregar la carne.\n10. Colocar en las hojas de mazorca un poco de masa.\n11. En el centro agregar una cucharada de recado y trozos de la carne.\n12. Envolver las hojas y atar en un extremo una tira de hoja o hilo de cocinar.\n13. Cocinar al vapor los chuchitos por aproximadamente una hora y media a fuego lento.",
"90","https://parrillas.top/wp-content/uploads/2020/07/chuchitos-guatemaltecos.jpg",5)

rec=[receta1,receta2,receta3]
recetas = [receta1,receta2,receta3,receta4,receta5,receta6]
val=None
contador=5
def validar_login(user, contrasena):
    for usuario in usuarios:
        if usuario.usuario == user and usuario.contrasena == contrasena:
            return usuario
    return None

def validar_usuario(uss):
    v=False
    for usuario in usuarios: 
        if str(uss)!=str(usuario.usuario):
            v=False
        else:
            v=True
            return v
    return v

def recuperacion_contrasena(user):
    v=False
    for usuario in usuarios: 
        if str(user)!=str(usuario.usuario):
            v=False
        else:
            v=usuario.contrasena
            return v
    return v

def creacion_usuario(nom, ape, user, contra):
    us=Usuario(nom,ape,user,contra)
    usuarios.append(us)

def buscar_receta(num):
    for x in recetas:
        if int(num)== int(x.indice):
            return x
        
@app.route('/')
def init():
    return redirect('inicio')


@app.route('/inicio')
def home():
    global validacion
    validacion=0
    if 'usuario_logeado' in session:
        return render_template('inicio.html', usuario=session['usuario_logeado'], rec=rec)
    return render_template('inicio.html', usuario=None, rec=rec)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        usuario = validar_login(
            request.form['usuario'], request.form['contrasena'])
        if usuario != None:
            global val
            val=1
            session['usuario_logeado'] = usuario.usuario  
            global user
            user=usuario.usuario  
            return redirect('inicio')
        else:
            error = 'Contrasena invalida'
            return render_template('login.html', error=error)
    if 'usuario_logeado' in session:
        return redirect('inicio')
    return render_template('login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('usuario_logeado', None)
    global val
    val= None
    global user
    user=None
    return redirect('login')

@app.route('/postReceta', methods=['POST'])
def agregarReceta():
    datos = request.get_json()
    print(datos)
    if datos['autor'] == '' or datos['titulo'] == '' or datos['resumen'] == '' or datos['ingredientes'] == '' or datos['procedimiento'] == '' or datos['tiempo'] == '' or datos['imagen'] == '':
        return {"msg": 'Error en contenido'}
    global contador
    contador=contador+1
    receta = Receta(datos['autor'], datos['titulo'], datos['resumen'], datos['ingredientes'], datos['procedimiento'], datos['tiempo'], datos['imagen'], contador)
    recetas.append(receta)
    return {"msg": 'Receta agregada'}

@app.route('/perfil')
def perfil():
    return render_template('perfil.html',user=user)

@app.route('/receta/<ide>')
def receta(ide):
    receta=buscar_receta(ide)     
    return render_template('receta.html',val=val,receta=receta,user=user)

@app.route('/registro', methods=['POST', 'GET'])
def registro():
    error = None
    if request.method == 'POST':
        cuenta=validar_usuario(request.form['usuario'])
        contraseña=request.form['contrasena']
        confi= request.form['contrasena1']
        if cuenta == True:
            error='El usuario ya existe'
            return render_template('registro.html', error=error)
        elif contraseña != confi:
            error='La contraseña no coincide'
            return render_template('registro.html', error=error)
        else:
            creacion_usuario(request.form['nombre'],request.form['apellido'],request.form['usuario'],request.form['contrasena'])
            error='Usuario creado con exito'
            return render_template('registro.html', error=error)
    return render_template('registro.html', error=error)

@app.route('/recuperar', methods=['POST', 'GET'])
def recuperar():
    error = ""
    if request.method == 'POST':
        error=recuperacion_contrasena(request.form['usuario'])
        print(error)
        if error == False:
            error='El usuario no existe'
            return render_template('recuperar.html', error=error)
        else:
            return render_template('recuperar.html', error=error)
    return render_template('recuperar.html', error=error)

@app.route('/CrearReceta')
def CrearReceta():
    return render_template('CrearReceta.html')

@app.route('/masrecetas')
def masrecetas(): 
    return render_template('masrecetas.html',val=val,recetas=recetas)

@app.route('/cargarArchivo', methods=['POST'])
def agregarRecetas():
    datos = request.get_json()
    print(datos)
    if datos['data'] == '':
        return {"msg": 'Error en contenido'}
    contenido = base64.b64decode(datos['data']).decode('utf-8')
    filas = contenido.splitlines()
    reader = csv.reader(filas, delimiter=',')
    for row in reader:
        global contador
        contador=contador+1
        receta = Receta(row[0], row[1], row[2],row[3],row[4],row[5],row[6],contador)
        recetas.append(receta)
    return {"msg": 'Receta agregada'}



if __name__ == '__main__':
    app.run(threaded=True,port=5000)
#app.run(debug=True)