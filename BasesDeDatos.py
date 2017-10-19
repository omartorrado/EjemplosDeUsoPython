import sqlite3 as dbapi

#Ver la version de la api
print("Api level: ",dbapi.apilevel)
#Que significa cada nivel de threadsafety
"""threadsafety 	Meaning
0 	Threads may not share the module.
1 	Threads may share the module, but not connections.
2 	Threads may share the module and connections.
3 	Threads may share the module, connections and cursors."""
print("Api Threadsafety: ",dbapi.threadsafety)
#Define como se escriben las consultas sql
print("Api paramStyle: ",dbapi.paramstyle)
#Creamos una variable donde almacenar la conexion con la base de datos
#El try es para manejar posibles errores de la db
try:
    db = dbapi.connect("pythonDB.db")
    print("Conexion: ",db)
    cursor = db.cursor()
    print("Cursor: ",cursor)
#Queda comentado pq tras la primera ejecucion ya queda la db creada
    #cursor.execute("""drop table usuarios""")
    #cursor.execute("""create table usuarios (dni text, nombre text, direccion text)""")

#Comentados para que deje de crear nuevas entradas (Al no tener definida una primaryKey deja duplicarlos)
    #cursor.execute("insert into usuarios VALUES ('7365734h','Paquito','el parque')")
    #cursor.execute("insert into usuarios VALUES ('123456789','Alguien','Somewhere')")

#Realizamos un commit para guardar los datos (aunque juraria que sqlite ya lo hace automaticamente con el execute
# ya que los datos son accesibles sin el commit)
    #db.commit()

#Al ejecutar el select, para acceder a los valores hay que usar el fetchone()/fetchmany(int numeroDeEntradas)/fetchall()
    datosAll =cursor.execute("select * from usuarios").fetchall()

#Podemos acceder directamente como arriba o guardarlo en una variable. Mientras queden entradas podemos seguir pillandolas
#tanto del cursor como de la variable donde guardamos el cursor
    cursorSelect=cursor.execute("select * from usuarios")

    datosOne = cursor.fetchone()
    datosMany = cursorSelect.fetchmany(2)

#Como se ve, al ejecutar el bucle de datosAll nos devuelve una tupla con los valores de cada entrada
    for x in datosAll:
        print("Iterando el resultado de Fetchall()",x)

#Por otra parte si iteramos lo guardado con fetchone() nos devolveria cada campo de esa entrada individualmente
    for x in datosOne:
        print("Iterando el resultado de fetchone()",x)

# Al iterar datosMany se deberia ver como datosAll pero solo tantas entradas como le digamos. Si usamos el mismo cursor
# que utilizamos con fetch one leera a partir de la entrada siguiente a la ultima recuperada con fetchone()
    for x in datosMany:
        print("Iterando el resultado de fetchmany(2)", x)

#En la primera excepcion manejamos un unico tipo de except, mientras que en la segunda 2
except dbapi.OperationalError:
    print("La db no funciona")
except(dbapi.excepcionisima, dbapi.outraExcepcion):
    print("Diferentes excepciones")