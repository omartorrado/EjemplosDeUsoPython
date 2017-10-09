import sqlite3 as dbapi

#Ver la version de la api
print(dbapi.apilevel)
#Que significa cada nivel de threadsafety
"""threadsafety 	Meaning
0 	Threads may not share the module.
1 	Threads may share the module, but not connections.
2 	Threads may share the module and connections.
3 	Threads may share the module, connections and cursors."""
print(dbapi.threadsafety)
#Define como se escriben las consultas sql
print(dbapi.paramstyle)
#Creamos una variable donde almacenar la conexion con la base de datos
#El try es para manejar posibles errores de la db
try:
    db = dbapi.connect("pythonDB.db")
    print(db)
    cursor = db.cursor()
    print(cursor)
    #cursor.execute("""drop table usuarios""")
    cursor.execute("""create table usuarios (dni text, nombre text, direccion text)""")
#En la primera excepcion manejamos un unico tipo de except, mientras que en la segunda 2
except dbapi.OperationalError:
    print("La db no funciona")
except(dbapi.excepcionisima, dbapi.outraExcepcion):
    print("Diferentes excepciones")