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

