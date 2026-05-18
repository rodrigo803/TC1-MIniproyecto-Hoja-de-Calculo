# TC1-MIniproyecto-Hoja-de-Calculo

- INTEGRANTES:
  - Rodrigo Rene Elias Ramirez
  - Sergio Alejandro Monge Moya
  - Dennis Segura Badilla
  
- COMO EJECUTAR:
  - Paso A: Clonar el repositorio
      Primero, descargará el código a su máquina local.
      - `Bash
        git clone https://github.com/rodrigo803/TC1-MIniproyecto-Hoja-de-Calculo.git`

  - Paso B: Entrar a la carpeta del proyecto
      Debe navegar hacia la raíz del proyecto, donde se encuentran el README.md y el main.lucia.
      - `Bash
        cd tu-repositorio-hoja-calculo`

  - Paso C: Compilar y Ejecutar
      Como tu punto de entrada está en la raíz, solo necesita indicarle al compilador (o al CLI) de Lucia que ejecute ese archivo. El compilador se encargará automáticamente de buscar los archivos referenciados en la            carpeta src/ gracias a las importaciones.
      - `Bash
        lucia run main.lucia`


- FUNCIONALIDADES IMPLEMENTADAS:
  - El proyecto cuenta con un núcleo funcional robusto, diseñado bajo principios de programación modular y separación de responsabilidades. Hasta el momento, el sistema incluye:
    - Arquitectura Modular: Separación estricta de la lógica de negocio, la interfaz de usuario y el motor de evaluación mediante módulos (`sistema`, `interfaz`, `evaluador`), manteniendo un punto de entrada limpio en           el archivo principal.
    - Mapeo de Matrices en Memoria Lineal: Implementación de una cuadrícula de 10x10 simulada sobre arreglos unidimensionales de 100 posiciones, utilizando conversión matemática de coordenadas de plano cartesiano a              índices de lista.
    - Interfaz Dinámica CLI (Command Line Interface): Menú interactivo controlado por estados.
    - Renderizado en consola de la matriz con encabezados alfabéticos (A-J) y numéricos (1-10).
    - Alineación y formateo de celdas utilizando métodos nativos de cadenas de texto para simular una tabla visual exacta.
    - Doble Perspectiva de Datos: Mantenimiento de dos estados paralelos en memoria:
    - Matriz de Fórmulas: Almacena el texto bruto o las expresiones ingresadas por el usuario.
    - Matriz Normal: Muestra los valores ya evaluados y calculados.
    - Motor Evaluador de Expresiones: Sistema de intercepción de datos que distingue entre valores estáticos (texto/números) y expresiones matemáticas al detectar el prefijo `=`.
    - Operaciones Soportadas: Asignación de valores estáticos y cadenas de texto.

- DIAGRAMA DE CLASES:

    <img width="587" height="537" alt="image" src="https://github.com/user-attachments/assets/afc3b6aa-32f6-42a1-a8d2-d8666ad24996" />



- DIAGRAMA DE CASOS DE USO:

    <img width="448" height="464" alt="image" src="https://github.com/user-attachments/assets/6dab7b8a-b69b-4cd7-acbe-21791c0fd84a" />


- ¿QUE MEJORAS SE HARIAN EN UNA VERSION 2.0?
  - Persistencia de Datos (Guardado y Carga): Implementar la capacidad de exportar el estado actual de los arreglos a archivos `.csv` o `.json`, permitiendo al usuario cerrar el programa y retomar su trabajo                   posteriormente.
  - Detección de Referencias Circulares: Integrar un algoritmo en el módulo evaluador que prevenga bucles infinitos en caso de que dos celdas se referencien mutuamente (por ejemplo, que `A1` sea `=B1` y `B1` sea `=A1`).
  - Soporte Multilenguaje o Multilibro: Escalar el arreglo para soportar una tercera dimensión que permita navegar entre diferentes "Pestañas" u hojas dentro del mismo libro de trabajo, tal como en el software comercial.
  - Actualización Dinámica en Cascada: Optimizar el evaluador para que, al modificar una celda "origen", todas las celdas que dependan de ella se recalculen automáticamente sin necesidad de reingresar las fórmulas.
  - Interfaz Gráfica de Usuario (GUI): Migrar de la interfaz de línea de comandos a una ventana interactiva gestionada por eventos de ratón, facilitando la selección de celdas y la navegación visual.
