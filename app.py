import os
import requests
import gradio as gr
from dotenv import load_dotenv
from scraper import extract_text_from_url

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def find_official_website(company_name):
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "q": f"{company_name} official website",
        "gl": "in"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    for result in data.get("organic", []):
        link = result.get("link", "")
        if company_name.lower() in link.lower():
            return link

    return None


def generate_company_report(company_name):

    if not company_name.strip():
        return "Please enter a company name."

    website = find_official_website(company_name)

    if website:
        content = extract_text_from_url(website)
    else:
        content = "Official website not found. Try LinkedIn or search manually."

    report = f"""
# 🏢 {company_name} - Company Intelligence Report

## 🌐 Website
{website if website else "Not Found"}

---

## 📌 About Company
{content[:1000]}

---

## 🎯 Vision & Mission
(Search within official content manually or extend logic to detect keywords like 'vision' or 'mission')

---

## 🛠 Products & Services
(Search within scraped content for product keywords)

---

## 👥 Customers
(If mentioned in website content)

---

## 🏆 Recognitions
(Search awards / recognitions section)

---

## 📍 Locations
(Check contact/about page manually or extend scraping logic)
"""

    return report


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Company Interview Preparation Assistant")
    gr.Markdown("Get deep company insights directly from official sources.")

    with gr.Row():
        company_input = gr.Textbox(label="Enter Company Name", placeholder="Example: Aptean")
        submit_btn = gr.Button("Generate Report")

    output = gr.Markdown()

    submit_btn.click(generate_company_report, inputs=company_input, outputs=output)

if __name__ == "__main__":
    demo.launch()