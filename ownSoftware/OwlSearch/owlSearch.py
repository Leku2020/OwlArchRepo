import argparse
import requests
import sys
import subprocess

# VirusTotal search function
def search_virustotal(api_key, search_type, search_value):
    url = f"https://www.virustotal.com/api/v3/{search_type}/{search_value}"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Throws an error if the response has a status other than 2xx.
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error whilst searching: {e}")
        sys.exit(1)

# Function to perform the search in MalwareBazaar
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

# Main function that handles user input
def main():
    # Define the parser arguments
    parser = argparse.ArgumentParser(description="Search for information in VirusTotal or MalwareBazaar by hash, ip, domain, etc.")
    
    # VirusTotal parameters
    parser.add_argument("--vt", action="store_true", help="Search in VirusTotal")
    parser.add_argument("--ip", type=str, help="Search by IP in VirusTotal.")
    parser.add_argument("--hash", type=str, help="Search by Hash(MD5, SHA1, SHA256) in either VirusTotal or MalwareBazaar.")
    parser.add_argument("--domain", type=str, help="Search by Domain in VirusTotal.")
    
    # MalwareBazaar Paramenters
    parser.add_argument("--mb", action="store_true", help="BSearch in MalwareBazaar")
    parser.add_argument("--tag", type=str, help="Search by tag in MalwareBazaar")
    parser.add_argument("--sig", type=str, help="Search by signature in MalwareBazaar.")
    parser.add_argument("--filetype", type=str, help="Search by file type in MalwareBazaar.")
    parser.add_argument("--sample", type=str, help="Obtain a hash sample from MalwareBazaar.")
    parser.add_argument("--uploadSample", type=str, help="Upload a hash sample to MalwareBazaar.")
    
    # Here, the API Keys must be placed
    vt_api_key = "YOUR_API_KEY_FROM_VIRUSTOTAL"
    mb_auth_key = "YOUR_API_KEY_FROM_MALWAREBAZAAR"

    # Parse the arguments
    args = parser.parse_args()

    # If VirusTotal is used
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
            print("You must specify a search type to use VirusTotal: --ip, --hash, --domain.")
            sys.exit(1)
        
        # Performs the search in VirusTotal
        print(f"Searching {search_type} '{search_value}' in VirusTotal...")
        result = search_virustotal(vt_api_key, search_type, search_value)
        print(result)

    # If MalwareBazaar is used
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
            print("You must specify a search type to use MalwareBazaar: --hash, --tag, --sig, --filetype, --sample, --uploadSample.")
            sys.exit(1)
        
        # Performs the search in MalwareBazaar
        print(f"Searching {search_type} '{search_value}' in MalwareBazaar...")
        result = search_malwarebazaar(mb_auth_key, search_type, search_value)
        print(result)

    else:
        print("you must specify if you would like to use (--vt) or MalwareBazaar (--mb).")
        sys.exit(1)

if __name__ == "__main__":
    main()
