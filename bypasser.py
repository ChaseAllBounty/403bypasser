import requests

def load_headers(file_path):
    headers_list = []
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                headers_list.append({key.strip(): value.strip()})
    return headers_list

url = "http://example.com"
headers_file = "headers_to_test.txt"

headers_to_test = load_headers(headers_file)

for headers in headers_to_test:
    try:
        response = requests.get(url, headers=headers)
        print(f"Headers: {headers}")
        print(f"Status Code: {response.status_code}")
        if response.status_code != 403:
            print(f"Potential Bypass with headers: {headers}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
