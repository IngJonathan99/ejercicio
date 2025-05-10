## Requisitos: 
**Python 3.x** instalado

## Instrucciones para ejecutar:
  - Clona el repositorio o descarga el archivo .py .
  - Abre una terminal en el directorio donde se encuentra el archivo.
  - Ejecuta el programa con el siguiente comando:
      `python nombre_del_archivo.py`
  - Ingresa una cadena de texto que contenga paréntesis (), corchetes [] o llaves {} cuando se te pida.
  
### Ejemplo:
  - "()}]" --> "No balanceado"
  - "{[]}" --> "Balanceado"

## Explicacion:
  Este programa evalúa si una cadena de caracteres contiene símbolos balanceados. Se consideran balanceados cuando:
  - Cada símbolo de apertura tiene un símbolo de cierre correspondiente.
  - El orden de apertura y cierre es correcto.

### ¿Cómo funciona?
  - El programa utiliza una estructura de datos tipo pila

Símbolos de apertura se agregan a la pila, cuando se encuentra un símbolo de cierre, se verifica:
  - Que la pila no esté vacía.
  - Que el último símbolo de apertura coincida con el tipo correcto de cierre.
  - Si alguna comprobación falla, se retorna False.
  - Al final, si la pila está vacía, los símbolos están correctamente balanceados → se retorna True.	

Finalmente, en base al resultado (True o False), se entrega si esta "Balanceado" o "No balanceado"
