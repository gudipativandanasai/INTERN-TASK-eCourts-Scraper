import requests 
from bs4 import BeautifulSoup
import json
import argparse
from datetime import datetime

BASE_URL = "https://services.ecourts.gov.in/ecourtindia_v6/"

def get_case_status(case_type, case_number, case_year):
    """Fetch case details based on inputs"""
    url = f"{BASE_URL}?p=casestatus/index/"
    params = {
        "case_type": case_type,
        "case_number": case_number,
        "case_year": case_year
    }

    print("🔍 Fetching case details...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("❌ Error fetching case details.")
        return None

    # In real scraping, parse HTML here.
    # We'll simulate parsed data for demo.
    data = {
        "case_number": f"{case_type}/{case_number}/{case_year}",
        "status": "Listed Tomorrow",
        "serial_no": "27",
        "court_name": "Courtroom 5 - Justice S. Rao",
        "date": datetime.today().strftime("%d-%m-%Y")
    }

    return data


def download_cause_list():
    """Download today's cause list PDF"""
    cause_list_url = f"{BASE_URL}/downloads/causelist.pdf"
    print("⬇ Downloading cause list...")

    response = requests.get(cause_list_url)
    if response.status_code == 200:
        filename = "cause_list_today.pdf"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Cause list downloaded: {filename}")
    else:
        print("❌ Could not download cause list (may not be available).")


def save_json(data, filename="case_result.json"):
    """Save result as JSON"""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"💾 Result saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description="eCourts Scraper Tool")
    parser.add_argument("--today", action="store_true", help="Check today's listing")
    parser.add_argument("--tomorrow", action="store_true", help="Check tomorrow's listing")
    parser.add_argument("--causelist", action="store_true", help="Download today's cause list")

    args = parser.parse_args()

    if args.causelist:
        download_cause_list()
        return

    print("=== eCourts Case Lookup ===")
    case_type = input("Enter Case Type (e.g., WP, CR, CC): ").strip()
    case_number = input("Enter Case Number: ").strip()
    case_year = input("Enter Case Year (e.g., 2023): ").strip()

    result = get_case_status(case_type, case_number, case_year)

    if result:
        print("\n=== Case Details ===")
        print(f"Case Number: {result['case_number']}")
        print(f"Status: {result['status']}")
        print(f"Serial Number: {result['serial_no']}")
        print(f"Court Name: {result['court_name']}")
        print(f"Date: {result['date']}")
        save_json(result)
    else:
        print("No case details found.")


if __name__ == "__main__":
    main()