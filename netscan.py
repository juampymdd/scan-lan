import nmap
import requests

def get_device_name(mac_address):
    api_url = f"https://macvendors.com/query/{mac_address}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Genera una excepción si la solicitud no tiene éxito
        
        # Comprobamos si la respuesta es un string válido
        if response.text.strip():
            return response.text.strip()
        else:
            return "No se encontró información para esta dirección MAC."
    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def scan_network():
    nm = nmap.PortScanner()
    ip_range = "192.168.0.1/24"
    
    nm.scan(hosts=ip_range, arguments='-sn')
    
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']
            
            print('IP:', ip)
            print('mac', mac)
            print('device', get_device_name(mac))

scan_network()