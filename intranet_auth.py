"""
Script en Python para validar usuario y contraseña contra Intranet UNAB
@author Esteban De La Fuente Rubio, DeLaF (esteban.delafuente[at]unab.cl)
@version 2015-07-08
"""

# módulos necesarios
import requests, getpass, json

# dirección del servicio web
uri = "https://campus.ing.unab.cl/api/usuarios/check_password"

# obtener usuario y contraseña
username = input('Usuario ['+getpass.getuser()+']: ')
if username == '' :
    username = getpass.getuser()
password = getpass.getpass('Contraseña: ')
data = json.dumps({'user': username, 'pass': password})

# consumir servicio
r = requests.post(uri, data, verify=False)

# mostrar resultado
print (str(r.status_code)+': '+r.json())
