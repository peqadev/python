# Python by PEQA

## Introducción

Python es un lenguaje de programación interpretado potente y fácil de aprender. Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos. La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.

El intérprete de Python y la extensiva librería estándar se encuentran disponibles libremente en código fuente y forma binaria para la mayoría de plataformas desde la Web de Python, https://www.python.org/, y se pueden distribuir libremente. El mismo sitio contiene distribuciones y direcciones a muchos módulos de Python de terceras partes, programas, herramientas y adicionalmente documentación.

El intérprete de Python es fácilmente extensible con funciones y tipos de datos implementados en C o C++ (o otros lenguajes que permitan ser llamados desde C). Python también es apropiado como un lenguaje para extender aplicaciones modificables.

## ¿Por qué aprender Python?

> Python, el segundo mejor lenguaje de programación para la mayoría de las áreas.

Hoy día, hay muchísimos lenguajes de programación y elegir entre ellos resulta una tarea difícil. Dependiendo del escenario, puedes decantarte por uno u otro y hay algunos que brillan muy bien en ciertos ambientes, pero no tanto, paro otros. Allí es donde entra Python, es un lenguaje que puede ser uno de los mejores para categorías de la programación como "las ciencias de datos", pero también puede ser bueno en "computación distribuida" y hasta en IoT. Es por esto, que muchos desarrolladores están tomando la iniciativa de emprender la tarea de aprender el lenguaje de programación "Python".

A continuación, listo una serie de puntos a favor de aprender python:
1. **Fácil de aprender:** Su sintaxis, hace que la barrera de entrada sea baja para desarrolladores que comienzan a programar, pero también funciona perfectamente cuando lo desees usar para implementar soluciones consideradas "complejas".
1. **Crea aplicaciones al instante (Scripting):** Python es un lenguaje de programación interpretado, pero también permite crear "scripts" que permite que crees aplicaciones en forma de scripts muy rápido. Y su versatilidad para funcionar en muchos ambientes diferentes, permite que puedas usar este lenguaje para sustituir algunos lenguajes tradiciones para crear scripts como Bash, Powershell, u otros.
1. **Python crece constantemente:** Éste posee una gran comunidad, muy bien estructurada que crece constantemente y que lo hace de una manera organizada. Además, apoya a muchos proyectos que se desarrollen sobre el lenguaje, a partir de sus relativamente grandes fondos (https://www.python.org/psf/annual-report/2020/) para un proyecto completamente open source. Apréndelo hoy y seguro vas a poder aplicarlo en algún proyecto hoy y hasta en los próximos años.
1. **Permite crear aplicaciones en muchas áreas distintas:** Como lo mencioné en el mensaje que envié arriba, Python es excelente lenguaje a para muchas áreas, y en las que no, sigue siendo un lenguaje que puede adaptarse. A continuación menciono algunas de las áreas más conocidas en las que este lenguaje funciona perfectamente:

    1. *Desarrollo web:* Con plataformas como flask y django.
    1. *Desarrollo de videojuegos:* Existen librerías como PySoy y Pygame.
    1. *Aprendizaje de máquina e inteligencia artifical:* Para estas áreas, python es el lenguaje que más se utiliza es Python. ¿Por qué?, por librerías como Pandas, Scitik-learn, Numpy y muchísimas más.
    1. *Ciencias de los datos:* Los datos, hoy día, representan dinero. El estudio de los datos que posees y extraer información/conocimiento es común realizarlo a través de herramientas como Python. Librerías como Pandas, Numpy ayudan a procesar los datos y librerías como Matplotlib y Seaborn para la construcción de gráficos.
    1. *Aplicaciones de escritorio:* Python se puede user para programar aplicaciones de escritorio. La librería Tkinter se puede utilizar para desarrollar interfaces de usuario. Hay otros conjuntos de herramientas útiles como wxWidgets, Kivy, PYQT que se pueden utilizar para crear aplicaciones en varias plataformas.
    1. *Aplicaciones de Web Scrapping:* Python es un excelente cuando se trata de extraer una gran cantidad de datos de sitios web que luego pueden ser útiles en varios procesos del mundo real, como la comparación de precios, las listas de trabajo, la investigación y el desarrollo y mucho más.
    1. *Aplicaciones empresariales:* Las aplicaciones empresariales son diferentes a otras aplicaciones del mercado y abarcan dominios como el comercio electrónico, el ERP y muchos más. Requieren aplicaciones que sean escalables, extensibles y fácilmente legibles y Python nos proporciona todas estas características. Plataformas como Tryton están disponibles para desarrollar este tipo de aplicaciones empresariales.
    1. *Aplicaciones de video/audio:* Usamos Python para desarrollar aplicaciones que puedan realizar varias tareas y también emitir medios. Aplicaciones de vídeo y audio como TimPlayer, Cplay han sido desarrolladas utilizando bibliotecas de Python. Proporcionan una mayor estabilidad y rendimiento en comparación con otros reproductores multimedia.
    1. *Aplicaciones CAD:* El diseño asistido por ordenador es todo un reto, ya que hay que tener en cuenta muchas cosas. Los objetos y su representación, las funciones son sólo la punta del iceberg cuando se trata de escenarios de ese tipo. Python también lo hace sencillo y la aplicación más conocida para el CAD es Fandango.
    1. *Aplicaciones integradas (Embebbed applications):* Python está basado en C, lo que significa que puede utilizarse para crear software C embebido para aplicaciones embebidas. Esto nos ayuda a realizar aplicaciones de alto nivel en dispositivos más pequeños que pueden computar Python.

## Instalación de python

Existen diferentes formas de instalar python en tu computador, pero este tutorial se enfoca en las opcione oficiales, porque resultan las mejores opciones para alguien que está comenzando con este lenguaje.

### Como instalar python en Windows

Existen tres opciones para instalar python en windows:
1. El "Microsoft Store"
1. El instalador completo.
1. Windows Sybsystem for Linux

Pero antes de instalar, vamos a verificar si el python está o no instalado en nuestra máquina.

#### ¿Cómo verificar la versión de python instalada en Windows?

En esta primera sección, revisaremos si existe previamente instalada una versión de python en la computadora.

Para esto, podemos hacer esto:
1. Abrir powershell / cmd.exe.
1. Escribir en el terminal: 
    ```powershell
    C:C:\> python --version
    ```
1. **Si** ya tienes python insalado, verás:
   ```powershell
   Python 3.8.4
   ```
1. En caso de **no** tenerlo instalado te aparecerá un error o se abrirá una vista del microsoft store para que lo descargues.

Si estás interesado en saber cómo verificar "Dónde" se encuentra almacenado tu intérprete de python, debes ejecutar: `C:\> where.exe python` en la misma terminal, cmd o powershell.

#### ¿Qué opciones tiene para instalar python en windows?

Como se ha mencionado anteriormente, hay tres formas de instalar la distribución oficial de Python en Windows:

- **Paquete de la Tienda Microsoft:** El método de instalación más sencillo en Windows implica la instalación desde la aplicación Microsoft Store. Se recomienda para los usuarios principiantes de Python que buscan una experiencia interactiva fácil de configurar.

- **Instalador completo:** Este método implica la descarga de Python directamente desde el sitio web Python.org. Se recomienda para desarrolladores intermedios y avanzados que necesitan más control durante el proceso de instalación.

- **Subsistema de Windows para Linux (WSL):** El WSL permite ejecutar un entorno Linux directamente en Windows. Puede aprender a habilitar el WSL leyendo la Guía de instalación del subsistema de Windows para Linux para Windows 10. *Esta es la opción favorita de muchos desarrolladores que trabajan con python con buen background de linux en un entorno de windows a día de hoy (2021).*

En esta sección, nos centraremos sólo en las dos primeras opciones, que son los métodos de instalación más populares en un entorno Windows.

```
Nota: También puedes completar la instalación en Windows utilizando distribuciones alternativas, como Anaconda, pero este tutorial sólo cubre las distribuciones oficiales.

Anaconda es una plataforma popular para hacer computación científica y ciencia de datos con Python.
```

Los dos instaladores oficiales de Python para Windows no son idénticos. El paquete de Microsoft Store tiene algunas limitaciones importantes.

##### Limitaciones del paquete de Microsoft Store

La documentación oficial de Python dice lo siguiente sobre el paquete Microsoft Store:

> El paquete Microsoft Store es un intérprete de Python de fácil instalación que está pensado principalmente para un uso interactivo, por ejemplo, por parte de los estudiantes.
*Fuente:* https://docs.python.org/3/using/windows.html#the-microsoft-store-package

La importante es que el paquete Microsoft Store está "pensado principalmente para un uso interactivo". Es decir, el paquete Microsoft Store está diseñado para ser utilizado por estudiantes y personas que aprenden a usar Python por primera vez.

Además de estar dirigido a los principiantes de Python, el paquete Microsoft Store tiene limitaciones que lo hacen poco adecuado para un entorno de desarrollo profesional. En particular, no tiene acceso total de escritura a ubicaciones compartidas como TEMP o el registro.

##### Recomendaciones del instalador de Windows

Si eres nuevo en Python y te centras principalmente en el aprendizaje del lenguaje más que en la creación de software profesional, entonces deberías instalar desde el paquete de Microsoft Store. Esto ofrece el camino más corto y más fácil para empezar con un mínimo de molestias.

Por otro lado, si eres un desarrollador experimentado que busca desarrollar software profesional en un entorno Windows, entonces el instalador oficial de Python.org es la elección correcta. Tu instalación no estará limitada por las políticas de la tienda de Microsoft, y puedes controlar dónde se instala el ejecutable e incluso añadir Python al PATH si es necesario.

##### Cómo instalar desde la Microsoft Store

Si eres nuevo en Python y quieres empezar rápidamente, el paquete de la Microsoft Store es la mejor manera de empezar a trabajar sin complicaciones. Puedes instalar desde la Microsoft Store en dos pasos.

**Paso #1:** Abrir la página de la aplicación Python en la Microsoft Store

Abre la aplicación Microsoft Store y busca Python.

Probablemente verás varias versiones que puedes elegir para instalar:

![Data Science](images/python_install_microsoft_store.png)

Selecciona Python 3.8, o el número de versión más alto que veas disponible en la aplicación, para abrir la página de instalación.

```
Advertencia: Asegúrate de que la aplicación de Python que has seleccionado ha sido creada por la Python Software Foundation.

El paquete oficial de Microsoft Store siempre será gratuito, así que si la aplicación cuesta dinero, entonces es la aplicación equivocada.
```

Como alternativa, puede abrir PowerShell y escribir el siguiente comando:

```Powershell
C:\> python
```

Si aún no tienes una versión de Python en tu sistema, cuando pulses Enter, la Microsoft Store se iniciará automáticamente y te llevará a la última versión de Python en la tienda.

**Paso #2:** Instalar la aplicación Python

Una vez seleccionada la versión a instalar, sigue estos pasos para completar la instalación:

1. Haga clic en Obtener.

1. Espera a que la aplicación se descargue. Cuando termine de descargarse, el botón Obtener será reemplazado por un botón que dice Instalar en mis dispositivos.

1. Haz clic en Instalar en mis dispositivos y selecciona los dispositivos en los que deseas completar la instalación.

1. Haz clic en Instalar ahora y luego en Aceptar para iniciar la instalación.

1. Si la instalación se ha realizado correctamente, verás el mensaje "Este producto está instalado" en la parte superior de la página de Microsoft Store.

¡Felicidades! Ahora tienes acceso a Python, incluyendo pip e IDLE.