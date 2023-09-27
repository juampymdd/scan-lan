## Escaneo de Dispositivos en una Red Local Usando Nmap y Macvendors API

Este script de Python utiliza las bibliotecas `nmap` y `requests` para escanear dispositivos en una red local y luego consulta la API de Macvendors para obtener información sobre el fabricante de la dirección MAC de cada dispositivo detectado. A continuación, se proporciona una explicación paso a paso y los requisitos previos necesarios para que funcione correctamente.

### Requisitos Previos

1. **Python**: Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python (https://www.python.org/downloads/).

2. **Bibliotecas Python**: Debes instalar las siguientes bibliotecas de Python utilizando `pip`, que es el administrador de paquetes de Python:
   
   ```bash
   pip install nmap requests
   ```

3. **Nmap**: Debes tener Nmap instalado en tu sistema. Nmap es una herramienta de código abierto para el descubrimiento de redes y la auditoría de seguridad. Puedes descargarlo desde el sitio web oficial de Nmap (https://nmap.org/download.html) o instalarlo a través del administrador de paquetes de tu sistema.

### Cómo Funciona el Script

El script consta de dos funciones principales:

#### `get_device_name(mac_address)`

Esta función toma una dirección MAC como entrada y consulta la API de Macvendors para obtener información sobre el fabricante de ese dispositivo. Luego, devuelve el nombre del fabricante o un mensaje de error si la consulta falla.

#### `scan_network()`

Esta función utiliza la biblioteca `nmap` para escanear una red local especificada (`ip_range`) en busca de dispositivos activos. Utiliza el argumento `-sn` para realizar un escaneo de ping simple que detecta dispositivos vivos sin necesidad de realizar un escaneo de puertos completo. Luego, itera a través de los hosts encontrados y, si encuentra una dirección MAC, llama a la función `get_device_name` para obtener el nombre del fabricante del dispositivo.

### Ejecutando el Script

Para ejecutar el script:

1. Asegúrate de haber instalado las bibliotecas Python y Nmap como se mencionó en los requisitos previos.

2. Reemplaza la variable `ip_range` en la función `scan_network` con la dirección IP y el rango de red de tu red local.

3. Ejecuta el script desde la línea de comandos:

   ```bash
   python nombre_del_script.py
   ```

El script escaneará la red local y mostrará información sobre los dispositivos detectados, incluyendo la dirección IP, la dirección MAC y el nombre del fabricante obtenido de la API de Macvendors.

Es importante destacar que el uso de este script debe realizarse con respeto a la privacidad y las leyes aplicables, y debes obtener el consentimiento adecuado antes de utilizarlo en una red o para fines de identificación de dispositivos.