```markdown
# 🏢 Companyinfo

Companyinfo is a Python toolkit designed to automate the extraction and summarization of official company information from the web. By simply entering a company name, Companyinfo utilizes large language models (LLMs), modern web scraping techniques, and search APIs to locate the official website and gather relevant details. This project aims to streamline the process of researching companies, making it faster and more accurate.

---

## ✨ Features

- **Automated Website Discovery:** Uses search APIs to find a company's official website from its name.
- **Intelligent Web Scraping:** Gathers relevant information using Playwright and BeautifulSoup, focusing on important pages (e.g., About, Products, Contact).
- **LLM-Powered Summarization:** Summarizes extracted data for easy consumption.
- **Simple Interface:** Gradio-based web app for user-friendly interaction.
- **Configurable & Extensible:** Easily add new keywords or improve extraction logic.

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mathi7585/companyinfo.git
   cd companyinfo
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root.
   - Add your Serper API key:
     ```
     SERPER_API_KEY=your_serper_api_key_here
     ```

---

## 💡 Usage

1. **Run the app**
   ```bash
   python app.py
   ```

2. **Interact via Gradio**
   - Open the provided URL in your browser.
   - Enter a company name.
   - View the summarized company information.

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Submit a pull request.

Please follow the [Contributor Covenant](https://www.contributor-covenant.org/) guidelines and ensure your code adheres to project conventions.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> For questions, feedback, or suggestions, please open an issue or contact the maintainer.
```


## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/mathi7585/Companyinfo
