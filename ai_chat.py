#!/usr/bin/env python3
import urllib.request, json, sys

API_URL = "https://api.hindsight.vectorize.io/v1/default/banks/cybersecurity-assistant/reflect"
API_KEY = "hsk_50b425c99734390d6a9f74d59a7f5e78_021b3c05d1268660"
PROJECT_NAME = "SBOM Generator & Vulnerability Matcher"

def main():
    print(f"=== Hindsight AI Cyber Assistant: {PROJECT_NAME} ===")
    print("🎁 Promo Code: MEMHACK1019 (Redeem for free credits at https://vectorize.io)")
    print("Type 'exit' or 'quit' to end session.\n")
    
    while True:
        try:
            query = input("\033[1;36mUser> \033[0m").strip()
            if not query:
                continue
            if query.lower() in ['exit', 'quit']:
                break
                
            headers = {
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            }
            payload = json.dumps({'query': f'[Context: {PROJECT_NAME}] {query}'}).encode('utf-8')
            req = urllib.request.Request(API_URL, data=payload, headers=headers, method='POST')
            
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                ans = data.get('text', 'No response.')
                print(f"\n\033[1;32mAssistant>\033[0m {ans}\n")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\033[1;31mError: {e}\033[0m\n")

if __name__ == '__main__':
    main()
