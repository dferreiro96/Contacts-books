# Contact Book / Agenda de Contactos v.2

A Python CLI program to manage a contact book: add, search, delete, and list contacts.

Un programa de línea de comandos en Python para gestionar una agenda de contactos: añadir, buscar, eliminar y listar contactos.

## Features / Funcionalidades

- Add contacts with name and phone number / Añadir contactos con nombre y número de teléfono
- Store contacts in a list of dictionaries / Guardar contactos en una lista de diccionarios
- Prevent duplicate contacts / Evitar contactos duplicados
- Search for a contact by name / Buscar un contacto por nombre
- Delete a contact by name / Eliminar un contacto por nombre
- Delete all contacts at once / Eliminar todos los contactos de una vez
- List all contacts sorted alphabetically / Listar todos los contactos ordenados alfabéticamente
- Menu-driven interface / Interfaz con menú
- Input validation for phone numbers / Validación de entrada para números de teléfono

## What Changed / Qué Cambió

This version was refactored into a  program with functions.

Esta versión fue refactorizada de un script de un solo archivo a un programa con funciones.

### Before / Antes

- All logic was written directly in the main loop / Toda la lógica estaba escrita directamente en el bucle principal
- No functions, just inline code / Sin funciones, solo código en línea
- Harder to read and maintain / Más difícil de leer y mantener

### After / Después

- Code split into reusable functions / Código dividido en funciones reutilizables
- Each function has a single responsibility / Cada función tiene una sola responsabilidad
- `main()` function controls the program flow / La función `main()` controla el flujo del programa
- Uses `match case` for menu options / Usa `match case` para las opciones del menú
- Easier to read, test, and maintain / Más fácil de leer, probar y mantener

### Function List / Lista de Funciones

- `pedir_nombre()` — Ask for and validate a contact name / Pedir y validar un nombre de contacto
- `pedir_telefono()` — Ask for and validate a phone number / Pedir y validar un número de teléfono
- `agregar_contacto(agenda)` — Add a new contact / Añadir un nuevo contacto
- `buscar_contacto(agenda)` — Search for a contact by name / Buscar un contacto por nombre
- `eliminar_contacto(agenda)` — Delete a contact by name / Eliminar un contacto por nombre
- `mostrar_agenda(agenda)` — Display all contacts sorted / Mostrar todos los contactos ordenados
- `eliminar_todos_los_contactos(agenda)` — Delete all contacts / Eliminar todos los contactos
- `menu()` — Display the menu / Mostrar el menú
- `pedir_opcion(opciones)` — Ask for and validate a menu option / Pedir y validar una opción del menú
- `jugar()` — Main loop of the program / Bucle principal del programa
- `main()` — Entry point / Punto de entrada


## Requirements / Requisitos

Python 3

## What I Learned / Lo que Aprendí

- Using dictionaries to store key-value data / Usar diccionarios para guardar datos clave-valor

- Asking the user for a specific number of items / Preguntar al usuario por un número específico de elementos

- Using enumerate() with dicc.items() to number the output / Usar enumerate() con dicc.items() para numerar la salida

- Validating input with try/except / Validar entradas con try/except

- Exiting a loop early with a keyword like "fin" / Salir de un bucle antes de tiempo con una palabra clave como "fin"

- Using a flag (jugar) to control the main loop / Usar una bandera (jugar) para controlar el bucle principal

## Author / Autor
[dferreiro96]

## How to Run / Cómo Ejecutar

```bash
python Agenda_de_contactos.py