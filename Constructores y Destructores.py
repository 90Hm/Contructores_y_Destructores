class FileManager:
    def __init__(self, file_name, mode):
        """
        Constructor: Se ejecuta automáticamente al crear una instancia de la clase.
        Inicializa la apertura del archivo.
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None
        print(f"Abrir archivo: {self.file_name} en modo {self.mode}")
        self.open_file()

    def open_file(self):
        """
        Método que abre el archivo con el modo especificado.
        """
        try:
            self.file = open(self.file_name, self.mode)
            print(f"Archivo {self.file_name} abierto correctamente.")
        except IOError as e:
            print(f"Error al abrir el archivo: {e}")

    def write_to_file(self, content):
        """
        Método que escribe contenido en el archivo.
        """
        if self.file and not self.file.closed:
            self.file.write(content)
            print(f"Escrito en el archivo: {content}")
        else:
            print("El archivo no está abierto.")

    def read_from_file(self):
        """
        Método que lee el contenido del archivo.
        """
        if self.file and not self.file.closed:
            content = self.file.read()
            print(f"Contenido del archivo:\n{content}")
        else:
            print("El archivo no está abierto.")

    def close_file(self):
        """
        Método que cierra el archivo.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo {self.file_name} cerrado.")

    def __del__(self):
        """
        Destructor: Se ejecuta automáticamente al eliminar una instancia de la clase.
        Cierra el archivo si está abierto.
        """
        if self.file and not self.file.closed:
            self.close_file()
        print(f"Destruyendo instancia de FileManager para {self.file_name}")


# Ejemplo de uso de la clase
if __name__ == "__main__":
    # Crear una instancia de FileManager en modo escritura
    file_manager = FileManager("example.txt", "w")

    # Escribir en el archivo
    file_manager.write_to_file("Hola, mundo!\n")

    # Eliminar la instancia explícitamente (esto llamará al destructor)
    del file_manager

    # Crear una instancia de FileManager en modo lectura
    file_manager = FileManager("example.txt", "r")

    # Leer desde el archivo
    file_manager.read_from_file()

    # Eliminar la instancia explícitamente (esto llamará al destructor)
    del file_manager

    # Pausa para observar la salida antes de que el programa termine
    input("Presiona Enter para finalizar el programa...")
#