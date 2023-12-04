


la interfaz es Una especificacion de que queremos que hagan los objetos.

Concepto de semantica sintaxis y sincronizacion.

En la especificacion de la interfaz tenemos la sintaxis ya hecha, tenemos cierta semantica con el printer y con el metodo write. Y por supuesto tenemos sincronizacion por que tenemos como es el mensaje de retorno. estamos viendo el ejemplo printer.ice

Modulo, lo utilizamos para agrupar interfaces. Las interfaces agrupan objetos, una clase printer que implementa los metodos. los servicios que vamos a utilizar son los diferentes metodos presentados en la interfaz.

Hay que hacer un manual de usuario con como hay que ejecutar el programa.


todo esto es de la carpeta basic.

Ice.loadSlice('Printer.ice')

 con esto hacemos una carga dinamica de la interfaz para poder utilizar las cosas 

    import Example
        con esto hacemos el import del modulo creado en el .ice


class PrinterI(Example.Printer):
    n = 0
    def write(self, message, current=None):
        print("{0}: {1}".format(self.n, message))
        sys.stdout.flush()
        self.n += 1

Lo implementamos asi para ejecutarlo de manera remota con la especificación de la interfaf, tenemos que poner un current para que pille la información sobre la llamada que se esta haciendo ademas del resto de parametros.

current=none se pone para que el metodo write se ejecute de manera local

el servidor hereda de ice.aplicattion para poder configurar el servidor.


con self.comunicator creamos un broker y el brojer lo utilizamos para crear un objeto adapter para controlar el servidor. con este ultimo creamos el proxy.

con el proxy lo que hacemos es decirle que este servicio lo asocie con el adaptador

        adapter.activate()
         
         Tras crear el adaptador lo activamos 


todo lo demas se entiende.




Ha dicho que el icestrom hay que replicarlo tal cual lo tiene ella en el ejemplo.

El icestorm es lo que tenemos que utilizar para los canales de eventos para comunicar los cambios del filemanager al frontend

                    icestorm

publisher.py                        Subscriber.py

                                        #aqui tenemos los objetos de tipo printer
                                        le decimos que va a sersubcriber a icestorm

