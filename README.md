# Contact Book / Agenda de Contactos v.3

A Python CLI program to manage a contact book using Object-Oriented Programming: add, search, delete, and edit contacts, with JSON persistence and CSV export.

Un programa de línea de comandos en Python para gestionar una agenda de contactos usando Programación Orientada a Objetos: añadir, buscar, eliminar y editar contactos, con persistencia en JSON y exportación a CSV.

## Features / Funcionalidades

- Object-Oriented Design: Uses inheritance (Contacto, ContactoPersonal, ContactoLaboral) and an Agenda class to manage logic. / Diseño Orientado a Objetos: Usa herencia (Contacto, ContactoPersonal, ContactoLaboral) y una clase Agenda para gestionar la lógica.

- Add contacts with name, phone number, email, and custom tags / Añadir contactos con nombre, teléfono, correo y etiquetas personalizadas.

- Prevent duplicate names, phone numbers, and emails / Evitar nombres, teléfonos y correos duplicados.

- Automatic JSON Persistence: Automatically saves changes to Datos.json. / Persistencia Automática en JSON: Guarda los cambios automáticamente en Datos.json.

- Crash Protection & Backups: Creates a backup (Datos.back) if the JSON is corrupted, and saves data if the user presses Ctrl+C. / Protección contra Cierres y Copias: Crea un respaldo (Datos.back) si el JSON está corrupto, y guarda los datos si el usuario presiona Ctrl+C.

- Birthday Reminder: Checks and displays a reminder at startup if any personal contact has a birthday today. / Recordatorio de Cumpleaños: Verifica y muestra un aviso al iniciar si algún contacto personal está de cumpleaños hoy.

- CSV Export: Export the contact list to Excel. / Exportación a CSV: Exporta la lista de contactos a Excel.

- Menu-driven interface with input validation / Interfaz con menú y validación de entradas.

## What Changed / Qué Cambió

- This version was refactored into an Object-Oriented architecture with data persistence / Esta versión fue refactorizada a una arquitectura Orientada a Objetos con persistencia de datos.

### Before / Antes

- Used a single Contacto list of dictionaries / Usaba una sola lista de diccionarios para los contactos.

- No file persistence (data lost on exit) / Sin persistencia de archivos (se perdían los datos al salir).

- Monolithic menu logic / Lógica del menú monolítica.

### After / Después

- Inheritance & super(): ContactoPersonal and ContactoLaboral inherit from Contacto. / Herencia y super(): ContactoPersonal y ContactoLaboral heredan de Contacto.

- File Handling: JSON for reading/writing state, CSV for exporting. / Manejo de Archivos: JSON para leer/escribir el estado, CSV para exportar.

- Modular UI: The programa() function acts as a router, calling smaller action functions (gestionar_agregar_contactos, gestionar_edicion_de_contactos, etc.). / UI Modular: La función programa() actúa como enrutador, llamando a funciones de acción más pequeñas.

## Function List / Lista de Funciones principales

- class Contacto (Base class: name, phone, email, tags) / (Clase base: nombre, teléfono, correo, etiquetas)

- class ContactoPersonal(Contacto) (Adds birthday and relationship) / (Añade cumpleaños y parentesco)

- class ContactoLaboral(Contacto) (Adds company and position) / (Añade empresa y cargo)

- class Agenda (Manages the contact list, persistence, and searches) / (Gestiona la lista de contactos, persistencia y búsquedas)

- programa() — Main loop and exception handling / Bucle principal y manejo de excepciones

- gestionar_agregar_contactos(), gestionar_busqueda_de_contactos(), gestionar_edicion_de_contactos() — UI routers / Enrutadores de la interfaz

## Requirements / Requisitos

- Python 3.10 or higher (uses match statements) / Python 3.10 o superior (usa match).

- Standard library only (json, csv, datetime, shutil) / Solo librería estándar.

## What I Learned / Lo que Aprendí

- Object-Oriented Programming: Classes, Inheritance (super()), and Polymorphism (isinstance). / Programación Orientada a Objetos: Clases, Herencia (super()) y Polimorfismo (isinstance).

- Data Persistence: Using __dict__ to serialize objects to JSON and reconstructing them. / Persistencia de Datos: Usar __dict__ para serializar objetos a JSON y reconstruirlos.

- File Export: Using csv.DictWriter for Excel reports and string formatting (.strftime). / Exportación de Archivos: Usar csv.DictWriter para reportes en Excel y formateo de strings.

- Exception Handling: Catching specific errors (FileNotFoundError, KeyError) and managing KeyboardInterrupt to save data safely. / Manejo de Excepciones: Capturar errores específicos y gestionar KeyboardInterrupt para guardar datos de forma segura.

- Refactoring: Splitting a large codebase into small, testable functions and separating UI from business logic. / Refactorización: Dividir un código grande en funciones pequeñas y separar la interfaz de la lógica de negocio.

## Author / Autor

[dferreiro96]

## How to Run / Cómo Ejecutar

python Agenda_de_contactos.py