# Budda Mission

Iniciando transmisión...

El desafío es crear un algoritmo que calcule la ruta con menos estaciones en una red de metro desde un punto A a un punto B, teniendo en cuenta que hay trenes en ruta, propiedad que indica en que estaciones va a parar o no.

El programa debe recibir ciertos parametros para emitir una respuesta:

    - Un archivo que describa la red de metro
    - Una estación inicial
    - Una estación final
    - Tipo de ruta del tren

Si se trata de los materiales...
Los tres últimos parámetros los podemos representar con Strings asi que no presentan un problema...
Pero ese archivo que describe la red de metro no suena fácil, suena a grafo.

Por ahi vamos a partir, vamos a averiguar como se describe un grafo en Python...
Googleando...

Ya encontré algunas referencias asi que vamos a trastear un poco. Vamos a levantar el ambiente...
Listo, el ambiente responde adecuadamente y ya logramos describir las rutas desde la Cisterna hasta Los Leones a travez de la L2, L1, L3 Y L4

Ahora vamos a trabajar en las clases que representan el gráfo y los vertices, para luego calcular la ruta mas corta entre dos estaciones
Después le agregaremos los colores, eso suena mas complicado. En mi investigacion escuche acerca de un algoritmo que calcula las rutas mas cortas en grafos con pesos, se llamaba Algoritmo de Dijkstra, creo que es por ahí es, pero vamos a partir por algo sensillo.

Zen mode activated.

Fin de la transmisión.
