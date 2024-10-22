# Django news app
- App de noticias para el informatorio

# Como ejecutar la app
- realizar un `git clone https://github.com/M0narc/django_news_app.git`

- crear en tu carpeta de trabajo un virtualenvironment(venv)
  `python -m venv venv` o `python3 -m venv venv`

  lo activas por la linea de comandos ya sea por cmd o vcs

  en tu carpeta donde tienes creado el `venv` -> cd venv/Scripts,
  y escribes activate -> luego escribes el comando `cd ..` dos veces
  para volver a la carpeta base
  
  ya en la carpeta base, en la linea de comandos escribes

  `pip install -r requirements`

  para instalar los requerimientos necesarios

  `cd src`
  para pararnos en la carpeta src donde se encuentra `manage.py`

  para ver las imagenes que tenemos de forma local usar el comando:
  `python manage.py collectstatic`

  y para correr la pagina

  `python manage.py runserver`

# jira board
  `https://informatorio2024comision3grupo3.atlassian.net/jira/software/projects/PF/boards/1`

  Por favor, atenerce a hacer lo que dice su ticket, no tocar de mas.

# Como trabajar en el proyecto
  en la linea de comandos:
    hacer un `git status` para confirmar que esats parado en la rama main y en la BASE del proyecto
    hacer un `git pull`para tener los datos actualizados
    hacer un `git switch -c {tu-nombre}/{nombre-de-tu-ticket}`
    y ya puedes comenzar tu trabajo!
    despues de probar tus cambios y funcionalidad corriendo el programa
    tienes que pushear tu codigo al repositorio remoto usando los siguientes comandos
    Asegurate de estar en LA BASE del proyecto
    `git status` para ver los cambios realizados en rojo, significa que no estan commiteados
    `git add .` para seleccionar TODOS los cambios que hiciste, puedes hacer otro `git status` para ver que los cambios que quieres realizar estan ahora de color verde, significa que estan listos para un commit
    `git commit -m "tu mensaje especifico"` para commitear los cambios en tu rama local
    `git push -u origin {aqui-el-nombre-de-tu-rama}` para empujar los cambios por primera vez al repositorio remoto primero tienes que apuntarlo ahi, despues ya no es necesario.
    si realizas el proceso nuevamente porque tenias mas cambios que hacer, ahora puedes simplemente hacer un: 
    `git push`

# Como hacer un PR
  una vez terminado tu codigo, hay que verificar que tenemos todo el mismo codigo que hay en la rama `main`, para hacer eso tenemos que hacer un `git branch` en la consola y verificar que estamos en `main`, de no estarlo hacemos un `git checkout main` para pararnos en la rama main, usar nuevamente `git branch` para estar seguros, deberia aparecer una * al lado de main, se veria asi `*main`, ahi, realizar un git pull para traer todos los cambios, luego, volvemos a nuestra rama de trabajo, haciendo un `git checkout nombre-de-tu-rama` y realizamos un `git rebase main`, si no hay conflictos, hacemos otro `git push` a tu rama remota y creamos el pull request desde la pagina lleanando los campos que se encuentran ahi.
  en el caso de encontrar conflictos, resolverlos, verificar que la app funcione y ahi recien, hacer el `git push` a tu rama.
  Si tienen dudas, escribanme en discord.

# TODO
 - Despues podemos pasar todo el texto plano a .json para mejor legibilidad
 - dejamos a drede fuera del .gitignore some media files para que los devs tengan imagenes con que testear