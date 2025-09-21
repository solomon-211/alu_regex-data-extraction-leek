import re
from datetime import datetime

# Regex Patterns (5 Data types extracted)

PATTERNS = {
    'emails': {
        'pattern': r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    },
    'urls': {
        'pattern': r'https?://(a-zA-Z.-)?\w+\.',
        'description': 'Extract HTTP/HTTPS URLs'
    },
    'phones': {
        'pattern': r'(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}',
    },
    'credit_cards': {
        'pattern': r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
    },
    'times': {
        'pattern': r'\b(?:[01]?\d|2[0-3]):[0-5]\d\s?(?:[AP]M)?\b', 
    },
}

# Sample Data for Extraction

SAMPLE_TEXT = """
Reach out to us at james.karim@elevatefuturesightfoundation.org or mercy.okello@elevatefuturesightfoundation.co.uk.
Visit our site at https://www.elevatefuturesightfoundation.org or https://subdomain.elevatefuturesightfoundation.org/events.
Call us at (091) 123-4567, 070-234-5678, or 078-888-9999.
Use credit card 4321 8765 2109 6543 or 4321-8765-2109-6543 to pay.
Our office hours are 9:00 AM to 6:00 PM, and the server backup runs at 02:30.
Meeting scheduled for 14:30 tomorrow.
"""

# Extraction Function

def extract_data(text):
    results = {}
    for key, info in PATTERNS.items():
        matches = re.findall(info['pattern'], text, re.IGNORECASE)
        # Remove duplicates while keeping order
        results[key] = list(dict.fromkeys(matches))
    return results

# Display Results

def display_results(results):
    print(f"REGEX DATA EXTRACTION RESULTS ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print("=" * 60)
    for data_type, matches in results.items():
        print(f"\n🔹 {data_type.upper()}")
        if matches:
            for i, match in enumerate(matches, 1):
                print(f"  {i}. {match}")
        else:
            print("No matches found")
    print("=" * 60)

# Main Execution

if __name__ == "__main__":
    extracted = extract_data(SAMPLE_TEXT)
    display_results(extracted)
