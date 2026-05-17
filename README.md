# TC1-MIniproyecto-Hoja-de-Calculo

Integrantes:
  -Rodrigo Rene Elias Ramirez
  -Sergio Alejandro Monge Moya
  
Cómo ejecutar:

Paso A: Clonar el repositorio
Primero, descargará el código a su máquina local.
Bash
git clone https://github.com/tu-usuario/tu-repositorio-hoja-calculo.git

Paso B: Entrar a la carpeta del proyecto
Debe navegar hacia la raíz del proyecto, donde se encuentran el README.md y el main.lucia.
Bash
cd tu-repositorio-hoja-calculo

Paso C: Compilar y Ejecutar
Como tu punto de entrada está en la raíz, solo necesita indicarle al compilador (o al CLI) de Lucia que ejecute ese archivo. El compilador se encargará automáticamente de buscar los archivos referenciados en la carpeta src/ gracias a las importaciones.
Bash
lucia run main.lucia


Funcionalidades implementadas:


DIAGRAMA DE CLASES:
+-----------------------------------+          +-----------------------------------+
|               Menu                |          |            HojaCalculo            |
+-----------------------------------+          +-----------------------------------+
| - opcion: int                     |          | - matriz: Celda[10][10]           |
+-----------------------------------+ 1      1 +-----------------------------------+
| + mostrarMenu(): void             |--------->| + inicializar(): void             |
| + procesarOpcion(op: int): void   |          | + obtenerCelda(pos: string): Celda|
+-----------------------------------+          | + actualizarCelda(p: str, v: str) |
                                               | + mostrarFormulas(): void         |
                                               | + mostrarNormal(): void           |
                                               +-----------------------------------+
                                                                 | 1
                                                                 |
                                                                 | 100 (10x10)
                                                                 v
+-----------------------------------+          +-----------------------------------+
|             Evaluador             |          |               Celda               |
+-----------------------------------+          +-----------------------------------+
|                                   |          | - fila: int                       |
+-----------------------------------+          | - columna: string                 |
| + evaluar(texto: str, h: Hoja):str| 1      * | - contenidoOriginal: string       |
| - calcularSuma(f: str): str       |<---------| - valorCalculado: string          |
| - calcularReversa(f: str): str    |          +-----------------------------------+
+-----------------------------------+          | + setContenido(v: string): void   |
                                               | + getContenido(): string          |
                                               +-----------------------------------+


DIAGRAMA DE CASOS DE USO:
       +-------------------------------------------------------+
       |                  Sistema Hoja de Cálculo              |
       |                                                       |
       |   +--------------------------+                        |
       |   | CU1: Asignar Valor/Fórmula|                       |
       |   +--------------------------+                        |
       |                 ^                                     |
       |                 | (Include)                           |
       |                 v                                     |
       |   +--------------------------+                        |
       |   | CU2: Evaluar Operación   |                        |
       |   |      (+, -, *, /, =,     |                        |
       |   |       Reversar, etc.)    |                        |
       |   +--------------------------+                        |
       |                                                       |
((Usuario))---> +--------------------------+                   |
       |        | CU3: Ver Matriz Fórmulas |                   |
       |        +--------------------------+                   |
       |                                                       |
       |   +--------------------------+                        |
       |   | CU4: Ver Matriz Normal   |                        |
       |   +--------------------------+                        |
       +-------------------------------------------------------+

Qué mejoras harían en una versión 2.0?:
