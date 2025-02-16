import argparse
import requests
import sys
import subprocess

# Función para realizar la búsqueda en VirusTotal
def search_virustotal(api_key, search_type, search_value):
    url = f"https://www.virustotal.com/api/v3/{search_type}/{search_value}"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza un error si la respuesta tiene un status diferente a 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la búsqueda: {e}")
        sys.exit(1)

# Función para realizar la búsqueda en MalwareBazaar
def search_malwarebazaar(auth_key, search_type, search_value):
    url = "https://mb-api.abuse.ch/api/v1/"
    headers = {
        "Auth-Key": auth_key
    }

    data = None

    if search_type == "hash":
        data = {"query": "get_info", "hash": search_value}
    elif search_type == "tag":
        data = {"query": "get_taginfo", "tag": search_value, "limit": 50}
    elif search_type == "sig":
        data = {"query": "get_siginfo", "signature": search_value, "limit": 50}
    elif search_type == "filetype":
        data = {"query": "get_file_type", "file_type": search_value, "limit": 10}
    elif search_type == "sample":
        data = {"query": "get_file", "sha256_hash": search_value}
    elif search_type == "upload":
        files = {"file": open(search_value, "rb")}
        response = requests.post(url, files=files, headers=headers)
        return response.json()
    
    if data:
        response = requests.post(url, headers=headers, data=data)
        return response.json()

# Función principal que maneja la entrada del usuario
def main():
    # Definir el parser de argumentos
    parser = argparse.ArgumentParser(description="Buscar información en VirusTotal o MalwareBazaar por hash, ip, dominio, etc.")
    
    # Opciones para VirusTotal
    parser.add_argument("--vt", action="store_true", help="Buscar en VirusTotal")
    parser.add_argument("--ip", type=str, help="Buscar por dirección IP en VirusTotal.")
    parser.add_argument("--hash", type=str, help="Buscar por hash (MD5, SHA1, SHA256) en VirusTotal o MalwareBazaar.")
    parser.add_argument("--domain", type=str, help="Buscar por dominio en VirusTotal.")
    
    # Opciones para MalwareBazaar
    parser.add_argument("--mb", action="store_true", help="Buscar en MalwareBazaar")
    parser.add_argument("--tag", type=str, help="Buscar por tag en MalwareBazaar.")
    parser.add_argument("--sig", type=str, help="Buscar por signature en MalwareBazaar.")
    parser.add_argument("--filetype", type=str, help="Buscar por tipo de archivo en MalwareBazaar.")
    parser.add_argument("--sample", type=str, help="Obtener muestra de un hash en MalwareBazaar.")
    parser.add_argument("--uploadSample", type=str, help="Subir una muestra a MalwareBazaar.")
    
    # Aquí debes poner tu clave API de VirusTotal y MalwareBazaar
    vt_api_key = "TU_API_KEY_DE_VIRUSTOTAL"
    mb_auth_key = "TU_API_KEY_DE_MALWAREBAZAAR"

    # Parsear los argumentos
    args = parser.parse_args()

    # Si se solicita VirusTotal
    if args.vt:
        if args.ip:
            search_type = "ip_addresses"
            search_value = args.ip
        elif args.hash:
            search_type = "files"
            search_value = args.hash
        elif args.domain:
            search_type = "domains"
            search_value = args.domain
        else:
            print("Debes especificar un tipo de búsqueda en VirusTotal: --ip, --hash, --domain.")
            sys.exit(1)
        
        # Realizar la búsqueda en VirusTotal
        print(f"Buscando {search_type} '{search_value}' en VirusTotal...")
        result = search_virustotal(vt_api_key, search_type, search_value)
        print(result)

    # Si se solicita MalwareBazaar
    elif args.mb:
        if args.hash:
            search_type = "hash"
            search_value = args.hash
        elif args.tag:
            search_type = "tag"
            search_value = args.tag
        elif args.sig:
            search_type = "sig"
            search_value = args.sig
        elif args.filetype:
            search_type = "filetype"
            search_value = args.filetype
        elif args.sample:
            search_type = "sample"
            search_value = args.sample
        elif args.uploadSample:
            search_type = "upload"
            search_value = args.uploadSample
        else:
            print("Debes especificar un tipo de búsqueda en MalwareBazaar: --hash, --tag, --sig, --filetype, --sample, --uploadSample.")
            sys.exit(1)
        
        # Realizar la búsqueda en MalwareBazaar
        print(f"Buscando {search_type} '{search_value}' en MalwareBazaar...")
        result = search_malwarebazaar(mb_auth_key, search_type, search_value)
        print(result)

    else:
        print("Debes especificar si deseas buscar en VirusTotal (--vt) o MalwareBazaar (--mb).")
        sys.exit(1)

if __name__ == "__main__":
    main()
