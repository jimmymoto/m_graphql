# m_graphql

# Carpeta de solución punto 1.1.
[backuml](https://github.com/jimmymoto/m_graphql/tree/feature/backuml)

## Usage

Para realizar el uso solo debe ejecutarse como se muestra a continuación.

```bash
python unmensaje.py
```


# Carpeta de solución punto 1.2.
[backpatern](https://github.com/jimmymoto/m_graphql/tree/feature/backpattern)

## Utilidad

Solución punto 1.2.


# Carpeta de solución punto 2.
[apigql](https://github.com/jimmymoto/m_graphql/tree/feature/apigql)

## Descripción diseño

El diseño se divide en 5 pasos que pasan por 3 instancias, el usuario realiza la solicitud de login por metodo POST enviando el username y password(1.loginUserGraph) a la instancia de Login. 
Luego de esto el sistema envia la petición a la instancia ModelUser(2.getUser) donde a su vez luego de verificar la existencia y exactitud del nombre de usuario con password, envía a la instancia token para la generación de un token.
Vale resaltar que si el usuario o password no es exacto (3.1. userErrorPassword) se genera un response 404 hasta llegar al usuario.
Para generar el token(3.getToken) se envía unicamente el usuario a la instancia de token y este retorna el objeto usuario con el token generado.
Luego este se devuelve a la instancia ModelUser y se genera un mutation donde se adiciona el email del usuario en la respuesta.
Por último se Responde un POST 200 al usuario con el contenido de la mutacion.
En este momento se crea un suscribe(5.userActiveSession) que mantendrá la sesión activa del usuario.

# Carpeta de solución punto 3.
[micro](https://github.com/jimmymoto/m_graphql/tree/feature/micro)

## Descripción diseño

Realice un diseño de un microservicio consultado desde un clienteweb y un clienteMobile.
El cliente web utiliza http para conexión REST a través de su front en ReactJS.
El cliente Mobile utiliza la conexión directa REST
El microservicio cuenta con 3 instancias:
ModelUser -> que maneja los datos del usuario, password y email.
TokenUser -> que maneja la asignación de token y su tiempo de uso en sesión.
ResolvErrors -> que maneja el log de errores y eventos.

Luego de esto y aplicando el patron Event Bridge, en su uso para el login se realiza la abstraccion para que realice la mutación de los datos enviados y quite el dato de password para devolver el token y el email del usuario.

