# INTERN-TASK-eCourts-Scraper
# ⚖ eCourts Scraper

This repository contains my *CodeAlpha Internship Task* — the eCourts Scraper Project.  
The project automates the process of collecting case data from the *Indian eCourts portal*, which provides judicial case details and updates from multiple district and high courts.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Automation](https://img.shields.io/badge/Automation-Web%20Scraping-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 🧾 Overview
The *eCourts Scraper* is a web automation and data extraction tool developed in Python to fetch and organize legal case data.  
It helps users collect case status, judgment dates, court names, and party details efficiently instead of manually searching the website.

This is particularly useful for:
- Legal researchers
- Law firms monitoring multiple cases
- Data analysts studying court patterns
- Developers building legal information systems

---

## ⚙ Features
- Automated scraping of case data from eCourts websites.  
- Support for multiple district and high courts.  
- Extracts relevant case details such as:
  - Case number  
  - Court and judge name  
  - Petitioner and respondent details  
  - Current status and next hearing date  
- Outputs collected data into structured *CSV* or *JSON* format.  
- Error handling for unavailable pages or invalid case numbers.

---

## 🛠 Technologies Used
- *Python 3*
- *BeautifulSoup / Selenium* for web scraping
- *Pandas* for data processing
- *Requests* for site interactions
- *CSV / JSON* for data storage

---

## 🚀 How to Run
1. Clone this repository:
2. git clone https://github.com//CodeAlpha.tasks.git
cd CodeAlpha.tasks/ecourts_scraper

2. Install dependencies:pip install -r requirements.txt3.
3. Run the scraper:python ecourts_scraper.py

4. Enter the court type or case number when prompted.  
The script will fetch data and save the output to output.csv.

---

## 📂 Project Structureecourts_scraper/
│
├── ecourts_scraper.py        # Main Python script
├── requirements.txt           # Dependencies
├── output.csv                 # Example scraped data
└── README.md                  # Project documentation

---

## 📈 Future Enhancements
- Add GUI to search and display results interactively.
- Enable scheduling for daily automated scraping.
- Integrate with database systems (MySQL / MongoDB).
- Include captcha bypass methods (with permission compliance).

---

## 👨‍💻 Author
*Your Name*  GUDIPATI VANDANA SAI
Python Development Intern  

📫 Email: gvandhanasai@gmail.com  
🔗 GitHub: (user name:gudipati vandana sai) (github link: https://github.com/gudipativandanasai/CodeAlpha.task1)

---

## 📜 License
This project is licensed under the *MIT License*. You may use, modify, and distribute this software with attribution.

---

⭐ If you find this project useful, please consider starring the repository!
