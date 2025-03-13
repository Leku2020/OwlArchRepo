#!/usr/bin/env python3

import argparse
import configparser
import os
import requests
import sys
import json
from datetime import datetime

HISTORY_FILE = "/usr/share/owlSearch/history.json"

# Leer las claves API desde un archivo de configuración
def load_config(args):
    config_path = os.path.expanduser("/usr/share/owlSearch/config.ini")
    config = configparser.ConfigParser()

    if not os.path.exists(config_path):
        print(f"Error: Config file not found at {config_path}. Please create it with VT_API_KEY and MB_AUTH_KEY.")
        sys.exit(1)

    config.read(config_path)
    vt_api_key, mb_auth_key, abuseipdb_api_key, shodan_api_key = None, None, None, None
    try:
        if "keys" not in config:
            print(f"Error: [keys] section not found in the config file. {config_path}")
            sys.exit(1)
        if args.vt:
            vt_api_key = config["keys"]["VT_API_KEY"]
            if vt_api_key == "":
                print(f"Error: VT_API_KEY must be defined in the config file. {config_path}")
                sys.exit(1)
        elif args.mb:
            mb_auth_key = config["keys"]["MB_AUTH_KEY"]
            if mb_auth_key == "":
                print(f"Error: MB_AUTH_KEY must be defined in the config file. {config_path}")
                sys.exit(1)
        elif args.abuseipdb:
            abuseipdb_api_key = config["keys"]["ABUSEIPDB_API_KEY"]
            if abuseipdb_api_key == "":
                print(f"Error: ABUSEIPDB_API_KEY must be defined in the config file. {config_path}")
                sys.exit(1)
        elif args.shodan:
            shodan_api_key = config["keys"]["SHODAN_API_KEY"]
            if shodan_api_key == "":
                print(f"Error: SHODAN_API_KEY must be defined in the config file. {config_path}")
                sys.exit(1)
    except KeyError:
        print("Error: VT_API_KEY, MB_AUTH_KEY, SHODAN_API_KEY and ABUSEIPDB_API_KEY must be defined in the config file. {config_path}")
        sys.exit(1)

    return vt_api_key, mb_auth_key, abuseipdb_api_key, shodan_api_key

def show_interactive_help():
    print("""
    Welcome to OwlSearch - Interactive Help

    This tool allows you to search for information from various threat intelligence sources.
    Below are the available options:

    1. VirusTotal (--vt)
       - Search by IP (--ip): Example: python owlSearch.py --vt --ip 8.8.8.8
       - Search by domain (--domain): Example: python owlSearch.py --vt --domain example.com
       - Search multiple domains (--domains): Example: python owlSearch.py --vt --domains example.com,test.com
       - Use a domain file (--domain-file): Example: python owlSearch.py --vt --domain-file domains.txt
       - Search by Hash (--hash): Example: python owlSearch.py --vt --hash d41d8cd98f00b204e9800998ecf8427e
       - Use a hash file (--hash-file): Example: python owlSearch.py --vt --hash-file hashes.txt
       - Search by IP (--ip): Example: python owlSearch.py --vt --ip 8.8.8.8
       - Use an IP file (--ip-file): Example: python owlSearch.py --vt --ip-file ips.txt

    2. MalwareBazaar (--mb)
       - Search by tag (--tag): Example: python owlSearch.py --mb --tag ransomware
       - Search by signature (--sig): Example: python owlSearch.py --mb --sig "Trojan.Generic"
       - Obtain a sample (--sample): Example: python owlSearch.py --mb --sample d41d8cd98f00b204e9800998ecf8427e
       - Upload a sample (--uploadSample): Example: python owlSearch.py --mb --uploadSample sample.zip
       - Search by Hash (--hash): Example: python owlSearch.py --mb --hash d41d8cd98f00b204e9800998ecf8427e
       - Use a hash file (--hash-file): Example: python owlSearch.py --mb --hash-file hashes.txt
       - Search by IP (--ip): Example: python owlSearch.py --mb --ip 8.8.8.8
       - Use an IP file (--ip-file): Example: python owlSearch.py --mb --ip-file ips.txt

    3. AbuseIPDB (--abuseipdb)
       - Check an IP (--check-ip): Example: python owlSearch.py --abuseipdb --check-ip 192.168.1.1
       - Fetch blacklist (--blacklist): Example: python owlSearch.py --abuseipdb --blacklist
       - Fetch reports (--reports): Example: python owlSearch.py --abuseipdb --reports 192.168.1.1

    4. Shodan (--shodan)
       - Count results (--count): Example: python owlSearch.py --shodan --count "port:22"
       - Search for hosts (--search): Example: python owlSearch.py --shodan --search "port:22"
       - Resolve domain names (--resolve): Example: python owlSearch.py --shodan --resolve google.com,qwen.ai

    5. History (--history)
       - Show query history: Example: python owlSearch.py --history

    For more details, use: python owlSearch.py --help
    """)

def save_to_history(params, response):
    params = vars(params) if hasattr(params, "__dict__") else str(params)
    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "params": params,
        "response": response
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    else:
        history = []

    history.append(history_entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("No history available.")
        return

    with open(HISTORY_FILE, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            print("Error reading history file.")
            return

    if not history:
        print("No history available.")
        return

    print("\n--- History ---")
    for entry in history:
        print(f"Timestamp: {entry['timestamp']}")
        print(f"Params: {entry['params']}")
        print(f"Response: {entry['response']}")
        print("-" * 40)

def search_shodan_ips(api_key, ip):
    url = f"https://api.shodan.io/shodan/host/{ip}"
    params = {
        "key": api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while searching in Shodan (host): {e}")
        return None

def search_shodan_domains(api_key, domain):
    url = f"https://api.shodan.io/dns/domain/{domain}"
    params = {
        "key": api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while searching in Shodan (domains): {e}")
        return None

def shodan_resolve(api_key, hostnames):
    url = "https://api.shodan.io/dns/resolve"
    params = {
        "key": api_key,
        "hostnames": hostnames,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while getting hostnames in Shodan: {e}")
        return None

def shodan_reverse(api_key, ips):
    url = "https://api.shodan.io/dns/reverse"
    params = {
        "key": api_key,
        "ips": ips,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while getting hostnames in Shodan: {e}")
        return None

def shodan_count(api_key, query, facets=None):
    url = "https://api.shodan.io/shodan/host/count"
    params = {
        "key": api_key,
        "query": query,
    }
    if facets:
        params["facets"] = facets

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while counting results in Shodan: {e}")
        return None


def search_shodan(api_key, query, facets=None):
    url = "https://api.shodan.io/shodan/host/search"
    params = {
        "key": api_key,
        "query": query
    }
    if facets:
        params["facets"] = facets

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while searching in Shodan: {e}")
        return None


def list_shodan_facets(api_key):
    url = "https://api.shodan.io/shodan/host/search/facets"
    params = {"key": api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while listing Shodan facets: {e}")
        return None


def list_shodan_filters(api_key):
    url = "https://api.shodan.io/shodan/host/search/filters"
    params = {"key": api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while listing Shodan filters: {e}")
        return None


def analyze_shodan_tokens(api_key, query):
    url = "https://api.shodan.io/shodan/host/search/tokens"
    params = {"key": api_key, "query": query}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while analyzing Shodan tokens: {e}")
        return None

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
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            content_disposition = response.headers.get("Content-Disposition", "")
            filename = f"{search_value}.zip"
            if "filename=" in content_disposition:
                original_filename = content_disposition.split("filename=")[1].strip('"')
                _, file_extension = os.path.splitext(original_filename)
                filename = f"{search_value}{file_extension}"

            current_directory = os.getcwd()
            file_path = os.path.join(current_directory, filename)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"File saved to: {file_path}")
            return {"message": f"File saved to {file_path}", "filename": filename}
        else:
            return {"error": "Failed to download the file", "status_code": response.status_code}

    elif search_type == "upload":
        files = {"file": open(search_value, "rb")}
        response = requests.post(url, files=files, headers=headers)
        return response.json()
    
    if data:
        response = requests.post(url, headers=headers, data=data)
        return response.json()

def get_abuseipdb_check(api_key, ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }
    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while searching in AbuseIPDB: {e}")
        return None


def get_abuseipdb_blacklist(api_key, confidence_minimum=90):
    url = "https://api.abuseipdb.com/api/v2/blacklist"
    querystring = {
        "confidenceMinimum": str(confidence_minimum),
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching AbuseIPDB blacklist: {e}")
        return None

def get_abuseipdb_reports(api_key, ip_address, max_age_in_days=30, page=1, per_page=25):
    url = "https://api.abuseipdb.com/api/v2/reports"
    querystring = {
        "ipAddress": ip_address,
        "maxAgeInDays": str(max_age_in_days),
        "page": str(page),
        "perPage": str(per_page),
    }
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching AbuseIPDB reports: {e}")
        return None
    
def process_queries(query_list, query_file):
    queries = []
    if query_list:
        queries = query_list.split(",")
    elif query_file:
        try:
            with open(query_file, "r") as f:
                queries = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Error reading query file: {e}")
            sys.exit(1)
    return queries

def pretty_print_json(data):
    print("\n--- Results ---")
    
    def print_dict(d, indent=0):
        """Helper function to recursively print dictionaries."""
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"{key}:")
                print_dict(value, indent + 1)
            elif isinstance(value, list):
                print("  " * indent + f"{key}:")
                for index, item in enumerate(value, start=1):
                    if isinstance(item, dict):
                        print("  " * (indent + 1) + f"Item {index}:")
                        print_dict(item, indent + 2)
                    else:
                        print("  " * (indent + 1) + f"- {item}")
            else:
                print("  " * indent + f"{key}: {value}")

    if isinstance(data, dict):
        # Handle the case where data is a dictionary with multiple queries as keys
        for query, result in data.items():
            print(f"\nQuery: {query}")
            if isinstance(result, dict):
                print_dict(result)
            elif isinstance(result, list):
                for index, item in enumerate(result, start=1):
                    print(f"  Result {index}:")
                    if isinstance(item, dict):
                        print_dict(item, indent=2)
                    else:
                        print(f"    - {item}")
            else:
                print(f"  Result: {result}")
    elif isinstance(data, list):
        # Handle the case where data is a list of results
        for index, item in enumerate(data, start=1):
            print(f"\nResult {index}:")
            if isinstance(item, dict):
                print_dict(item, indent=1)
            else:
                print(f"  - {item}")
    else:
        # Handle the case where data is neither a dictionary nor a list
        print(data)

def read_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            values = [line.strip() for line in f if line.strip()]
        return values
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def read_from_file_parse_comma(file_path):
    try:
        with open(file_path, "r") as f:
            values = [line.strip() for line in f if line.strip()]
            result = ",".join(values)
            print (result)
        return result
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Save results to a file in JSON format
def save_results_to_file(data, output_file):
    try:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results to file: {e}")
        sys.exit(1)


def query_virustotal(vt_api_key, args):
    search_type = None 
    queries = []
    if args.domain:
        search_type = "domains"
        queries = process_queries(args.domain, None)
    elif args.ip:
        search_type = "ip_addresses"
        queries = process_queries(args.ip, None)
    elif args.hash:
        search_type = "files"
        queries = process_queries(args.hash, None)
    elif args.domain_file:
        search_type = "domains"
        queries = read_from_file(args.domain_file)
    elif args.ip_file:
        search_type = "ip_addresses"
        queries = read_from_file(args.ip_file)
    elif args.hash_file:
        search_type = "files" if args.vt else "hash"
        queries = read_from_file(args.hash_file)
    else:
        print("You must specify a search type to use VirusTotal: --ip, --hash, --domain.")
        sys.exit(1)
    all_results = {}
    for query in queries:
        print(f"\nProcessing query: {query}")
        result = search_virustotal(vt_api_key, search_type, query)
        all_results[query] = result
    return all_results

def query_malwarebazaar(mb_auth_key, args):
    search_type = None 
    queries = []
    if args.hash:
        search_type = "hash"
        queries = process_queries(args.hash, None)
    elif args.tag:
        search_type = "tag"
        queries = process_queries(args.tag, None)
    elif args.sig:
        search_type = "sig"
        queries = process_queries(args.sig, None)
    elif args.filetype:
        search_type = "filetype"
        queries = process_queries(args.filetype, None)
    elif args.sample:
        search_type = "sample"
        queries = process_queries(args.sample, None)
    elif args.uploadSample:
        search_type = "upload"
        queries = [args.uploadSample]
    elif args.hash_file:
        search_type = "files"
        queries = read_from_file(args.hash_file)
    elif args.tag_file:
        search_type = "tag"
        queries = read_from_file(args.tag_file)
    elif args.sig_file:
        search_type = "sig"
        queries = read_from_file(args.sig_file)
    elif args.filetype_file:
        search_type = "filetype"
        queries = read_from_file(args.filetype_file)
    elif args.sample_file:
        search_type = "sample"
        queries = read_from_file(args.sample_file)
    else:
        print("You must specify a search type to use MalwareBazaar: --hash, --tag, --sig, --filetype, --sample.")
    all_results = {}
    for query in queries:
        print(f"\nProcessing query: {query}")
        result = search_malwarebazaar(mb_auth_key, search_type, query)
        all_results[query] = result
    return all_results

def query_abuseipdb(abuseipdb_api_key, args):
    if args.blacklist:
        queries = [1,1]
    elif args.ip:
        queries = process_queries(args.ip, None)
    elif args.ip_file:
        queries = read_from_file(args.ip_file)
    else:
        print("You must specify a search type for AbuseIPDB: --blacklist, or set a list of ip addresses.")
    all_results = {}
    for query in queries:
        print(f"\nProcessing query: {query}")
        if args.blacklist:
            result = get_abuseipdb_blacklist(abuseipdb_api_key, confidence_minimum=args.confidence_minimum)
        elif args.reports:
            result = get_abuseipdb_reports(abuseipdb_api_key, ip_address=query, max_age_in_days=args.max_age, page=args.page, per_page=args.per_page)
        elif args.check:
            result = get_abuseipdb_check(abuseipdb_api_key, query)
        else:
            print("You must specify a search type for AbuseIPDB: --blacklist, --reports, --check.")
        all_results[query] = result
    return all_results

def query_shodan(shodan_api_key, args):
    queries = []
    all_results = {}
    if args.ip:
        queries = process_queries(args.ip, None)
    if args.query:
        queries = [args.query]
    elif args.ip_file:
        queries = process_queries(read_from_file_parse_comma(args.ip_file), None)
    elif args.dns:
        queries = process_queries(args.dns, None)
    elif args.dns_file:
        queries = process_queries(read_from_file_parse_comma(args.dns_file), None)
    elif args.reverse:
        queries = process_queries(args.reverse, None)
    elif args.reverse_file:
        queries = process_queries(read_from_file_parse_comma(args.reverse_file), None)
    elif args.resolve:
        queries = process_queries(args.resolve, None)
    elif args.resolve_file:
        queries = process_queries(read_from_file_parse_comma(args.resolve_file), None)
    elif args.tokens or args.facets or args.filters:
        queries = [1,1]
    for query in queries:
        print(f"\nProcessing query: {query}")
        if args.ip or args.ip_file:
            result = search_shodan_ips(shodan_api_key, query)
        elif args.count:
            result = shodan_count(shodan_api_key, query, args.facets)
        elif args.search:
            result = search_shodan(shodan_api_key, query, args.facets)
        elif args.tokens:
            result = analyze_shodan_tokens(shodan_api_key, query)
        elif args.facets:
            result = list_shodan_facets(shodan_api_key)
        elif args.filters:
            result = list_shodan_filters(shodan_api_key)
        elif args.dns or args.dns_file:
            result = search_shodan_domains(shodan_api_key, query)
        elif args.reverse or args.reverse_file:
            result = shodan_reverse(shodan_api_key, query)
        elif args.resolve or args.resolve_file:
            result = shodan_resolve(shodan_api_key, query)
        else:
            print("You must specify a search type for Shodan: --count, --search, --facets, --filters, --tokens, --dns, --reverse, --resolve.")
        all_results[query] = result
    return all_results
# Main function that handles user input
def main():

    # Argument parser configuration
    parser = argparse.ArgumentParser(
        description="OwlSearch: A tool to search for information in VirusTotal, MalwareBazaar, AbuseIPDB, and Shodan.",
        epilog="Usage examples:\n"
               "  python owlSearch.py --vt --ip 8.8.8.8\n"
               "  python owlSearch.py --mb --hash d41d8cd98f00b204e9800998ecf8427e\n"
               "  python owlSearch.py --abuseipdb --check-ip 192.168.1.1\n"
               "  python owlSearch.py --shodan --resolve google.com,qwen.ai\n"
               "  python owlSearch.py --history\n",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-o", "--output", type=str, help="Save results to a file in JSON format.")
    parser.add_argument("--help-interactive", action="store_true", help="Show interactive help.")

    # VirusTotal parameters
    parser.add_argument("--vt", action="store_true", help="Search in VirusTotal")
    parser.add_argument("--domain", type=str, help="Search by Domain in VirusTotal.")
    parser.add_argument("--domains", type=str, help="Comma-separated list of domains (multiple queries).")
    parser.add_argument("--domain-file", type=str, help="File containing a list of domains (one per line).")
    
    # MalwareBazaar Parameters
    parser.add_argument("--mb", action="store_true", help="Search in MalwareBazaar")
    parser.add_argument("--tag", type=str, help="Search by tag in MalwareBazaar")
    parser.add_argument("--sig", type=str, help="Search by signature in MalwareBazaar.")
    parser.add_argument("--filetype", type=str, help="Search by file type in MalwareBazaar.")
    parser.add_argument("--sample", type=str, help="Obtain a hash sample from MalwareBazaar.")
    parser.add_argument("--uploadSample", type=str, help="Upload a hash sample to MalwareBazaar.")
    parser.add_argument("--tag-file", type=str, help="File containing a list of tags (one per line).")
    parser.add_argument("--sig-file", type=str, help="File containing a list of signatures (one per line).")
    parser.add_argument("--filetype-file", type=str, help="File containing a list of file types (one per line).")
    parser.add_argument("--sample-file", type=str, help="File containing a list of samples (one per line).")

    # AbuseIPDB Parameters
    parser.add_argument("--abuseipdb", action="store_true", help="Search in AbuseIPDB")
    parser.add_argument("--blacklist", action="store_true", help="Fetch the AbuseIPDB blacklist.")
    parser.add_argument("--check", action="store_true", help="Fetch the AbuseIPDB check.")
    parser.add_argument("--reports", action="store_true", help="Fetch the AbuseIPDB reports.")
    parser.add_argument("--confidence-minimum", type=int, default=90, help="Confidence minimum for the blacklist (default: 90).")
    parser.add_argument("--max-age", type=int, default=30, help="Max age in days for AbuseIPDB reports (default: 30).")
    parser.add_argument("--page", type=int, default=1, help="Page number for AbuseIPDB reports pagination (default: 1).")
    parser.add_argument("--per-page", type=int, default=25, help="Number of results per page for AbuseIPDB reports (default: 25).")

    # Shodan Parameters
    parser.add_argument("--shodan", action="store_true", help="Search in Shodan")
    parser.add_argument("--count", type=str, help="Count results for a Shodan query without returning details.")
    parser.add_argument("--search", type=str, help="Search for hosts using a Shodan query.")
    parser.add_argument("--facets", action="store_true", help="List available facets for Shodan analysis.")
    parser.add_argument("--filters", action="store_true", help="List available filters for Shodan queries.")
    parser.add_argument("--tokens", type=str, help="Analyze a Shodan query and break it into tokens.")
    parser.add_argument("--query", type=str, help="Query for shodan params.")
    parser.add_argument("--dns", type=str, help="Search by DNS in Shodan.")
    parser.add_argument("--dns-file", type=str, help="File containing a list of DNS (one per line) in Shodan.")
    parser.add_argument("--reverse", type=str, help="Search by Reverse DNS in Shodan.")
    parser.add_argument("--reverse-file", type=str, help="File containing a list of Reverse DNS (one per line) in Shodan.")
    parser.add_argument("--resolve", type=str, help="Search by Resolve DNS in Shodan.")
    parser.add_argument("--resolve-file", type=str, help="File containing a list of Resolve DNS (one per line) in Shodan.")

    parser.add_argument("--hash-file", type=str, help="File containing a list of hashes (one per line) in either VirusTotal or MalwareBazaar.")
    parser.add_argument("--ip", type=str, help="Search by IP in VirusTotal, AbuseIPDB or Shodan.")
    parser.add_argument("--ip-file", type=str, help="File containing a list of IPs (one per line) in VirusTotal, AbuseIPDB or Shodan.")
    parser.add_argument("--hash", type=str, help="Search by Hash(MD5, SHA1, SHA256) in either VirusTotal or MalwareBazaar.")
    parser.add_argument("--history", action="store_true", help="Show the request history.")

    # Parse the arguments
    args = parser.parse_args()

    # Load API keys from config file
    vt_api_key, mb_auth_key, abuseipdb_api_key, shodan_api_key = load_config(args)

    if args.vt:
        all_results = query_virustotal(vt_api_key, args)
        save_to_history(args, all_results)
    elif args.mb:
        all_results = query_malwarebazaar(mb_auth_key, args)
        save_to_history(args, all_results)
    elif args.abuseipdb:
        all_results = query_abuseipdb(abuseipdb_api_key, args)
        save_to_history(args, all_results)
    elif args.shodan:
        all_results = query_shodan(shodan_api_key, args)
        save_to_history(args, all_results)
    elif args.history:
        show_history()
        sys.exit(0)
    elif args.help_interactive:
        show_interactive_help()
        sys.exit(0)
    else:
        print("You must specify if you would like to use VirusTotal (--vt), MalwareBazaar (--mb), Shodan (--shodan) or AbuseIPDB (--abuseipdb).")
        sys.exit(1)

    if args.output:
        save_results_to_file(all_results, args.output)
    else:
        pretty_print_json(all_results)

if __name__ == "__main__":
    main()