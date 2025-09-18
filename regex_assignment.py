import re
from datetime import datetime

# Regex Patterns (minimum 5 types)

PATTERNS = {
    'emails': {
        'pattern': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        'description': 'Extract email addresses'
    },
    'urls': {
        'pattern': r'https?://[^\s/$.?#].[^\s]*',
        'description': 'Extract HTTP/HTTPS URLs'
    },
    'phones': {
        'pattern': r'(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}',
        'description': 'Extract phone numbers in multiple formats'
    },
    'credit_cards': {
        'pattern': r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        'description': 'Extract credit card numbers with spaces or dashes'
    },
    'times': {
        'pattern': r'\b(?:[01]?\d|2[0-3]):[0-5]\d\s?(?:[AP]M)?\b',
        'description': 'Extract times in 24-hour and 12-hour formats'
    },
}

# Sample Data for Extraction

SAMPLE_TEXT = """
Contact us at john.doe@example.com or jane.smith@company.co.uk.
Visit our site at https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 987-654-3210, or 123-456-7890.
Use credit card 1234 5678 9012 3456 or 1234-5678-9012-3456 to pay.
Our office hours are 9:00 AM to 5:30 PM, and the server backup runs at 23:45.
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
