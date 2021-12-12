# Clases del Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos

## ¿Qué son y por qué utilizar plantillas de proyectos?

### Personalizacion avanzada

- Crearas plantillas de entornos de trabajo personalizadas para tus analisis

- Aprenderas a desarrollar proyectos autocontenibles y multiplataforma

### ¿Qué son?

Son un medio que posibilita portar o construir un diseño predefinido

### Por qué utilizarlas?

- agiliza tu trabajo
- te agradeceran
- te agradeceras

- la rutina y automatización van a reducir la fatiga por decision
- Personalizar es mas facil que construir de cero
- La repoducibilidad se vuelve mucho mas factible
- Encontrar las cosas se vuelve sencillo

## Instalar Cookiecutter

Es una libreria de python, funciona con Jinja y permite crear plantillas de proyectos.

Es facil instalar cookiecutter con conda

agregar channel para instalar

```sh
conda config --add channels conda-forge
```

crear el entorno virtual

```sh
conda create --name cookie_cutter-personal cookiecutter=1.7.3
```

Exportar las cofniguraciones del entorno virtual

```sh
conda env export --from-history --file environment.yml
```

### Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```

Se usa checkout porque la estructura no esta en la rama principal

## Crear plantillas de proyecto personalizadas

Creando una estructura de archivos con cookiecutter

## Implementar hooks

Puede hacer falta que ciertos nombres cumplan un formato, para lo cual se hace uso de hooks y expresiones regulares para lograr este objetivo.

## Distribuir plantilla de proyecto

para facilitar la distribucion de la plantilla de proyecto, se crea un repositorio publico de github que contenga la carpeta con la plantilla de proyecto.

y para usar la plantilla en local era

```sh
cookiecutter .
```

ahora con el repositorio publico es

```sh
cookiecutter ${url de github}
```

## Manejo de rutas: problemática

una problematica posible es que la definicion de rutas de archivos son diferentes dependiendo del sistema operativo, Siendo estos MacOs, Windows o Linux.

```sh
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
```

## Manejo de rutasdel sistema: OS

Creando la siguiente ruta sin importar el sistema operativo *./data/raw/*

## Manejo de rutas del sistema: Pathlib

Manejando rutas con pathlib

## Manejo de rutas del sistema: PyFilesystem2

## Crear referencias relativas de archivos

## Descarga de plantilla y configuración de ambiente virtual

```sh
cookiecutter git@github.com:jvelezmagic/cookiecutter-conda-data-science.git
```

## Utilizar proyecto como un módulo de Python

Instalar la carpeta actual como un modulo de python, que reaccione a las ediciones.

```sh
pip install --editable .
```

para permitir que el kernel ejecute autoreload de la libreria que estas editando

```python
%load_ext autoreload
%autoreload 2
```

## Flujo de trabajo de los notebooks

Es muy util separar las secciones del notebook que ya estan listas en notebooks diferentes para poder trabajar en ellas de forma mas organizada.

ademas tambien se puede llamar un notebook de la sigueinte manera

```sh
%run "0-0-dbz-download_data.ipynb"
```

## Aplica estas herramientas

Utilizar herramientas de plantillas de entornos de trabajo hara que te agradezca para lograr iniciar proyectos y mantenerlos de forma mas eficaz.

Ajiliza el trabajo

reduce la fatiga por decision
