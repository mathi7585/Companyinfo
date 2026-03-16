# 🏢 companyinfo-llm

companyinfo-llm is a Python-based toolkit that leverages LLMs, modern web scraping, and search APIs to extract and summarize official company information from the web. By inputting a company name, the project automatically finds the official website with search APIs, scrapes relevant sections, and processes the content for downstream use.

---

## ✨ Features

- 🔍 **Automated Website Discovery:** Finds the official website for any company using search APIs.
- 🕸️ **Smart Web Scraping:** Crawls and extracts data from important company web pages (e.g., About, Products, Contact).
- 🧠 **LLM-Ready:** Prepares data for further processing with Large Language Models.
- 🐍 **Simple Python Interface:** Easily integrate with `app.py` and `scraper.py` modules.
- 🦾 **Gradio UI:** Interactive interface for trying out the workflow.

---

## ⚡ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mathi7585/companyinfo-llm.git
   cd companyinfo-llm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** You need [Playwright](https://playwright.dev/python/) and [Gradio](https://www.gradio.app/) installed.  
   Install Playwright browsers:
   ```bash
   playwright install
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env` and add your [Serper API Key](https://serper.dev/):
     ```
     SERPER_API_KEY=your_serper_api_key_here
     ```

---

## 🚀 Usage

1. **Run the application**

   ```bash
   python app.py
   ```

2. **Interact with the Gradio UI**

   - Enter a company name.
   - The app will:
     - Find the official website.
     - Scrape relevant company information.
     - Display or process the extracted data.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

**Happy scraping! 🚀**

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/mathi7585/companyinfo-llm