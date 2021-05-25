# m_graphql

Carpeta de solución punto 3.

## Descripción diseño

Realice un diseño de un microservicio consultado desde un clienteweb y un clienteMobile.
El cliente web utiliza http para conexión REST a través de su front en ReactJS.
El cliente Mobile utiliza la conexión directa REST
El microservicio cuenta con 3 instancias:
ModelUser -> que maneja los datos del usuario, password y email.
TokenUser -> que maneja la asignación de token y su tiempo de uso en sesión.
ResolvErrors -> que maneja el log de errores y eventos.

Luego de esto y aplicando el patron Event Bridge, en su uso para el login se realiza la abstraccion para que realice la mutación de los datos enviados y quite el dato de password para devolver el token y el email del usuario.

