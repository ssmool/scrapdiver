<div align="center">
  <img src="https://via.placeholder.com/800x200/000000/FFFFFF?text=Scrapdiver" alt="Scrapdiver Banner">
  <h1>🌊 Scrapdiver</h1>
  <p><b>Advanced Screenscraping & OCR Text Extraction Tool</b></p>
</div>

## 📖 About
**Scrapdiver** is a powerful screenscraping utility designed to traverse lists of web pages, capture full-page screenshots, and extract text using Optical Character Recognition (OCR). The extracted text is then systematically stored in local databases for deep content sweeping, archiving, and analysis. 

Unlike traditional HTML parsers, Scrapdiver renders the page as a user sees it, making it ideal for bypassing complex JavaScript-heavy layouts, Canvas-rendered text, and anti-scraping DOM obfuscation.

Developed by **#asytrick**  
Available at: [github.com/ssmool/scrapdiver](https://github.com/ssmool/scrapdiver)  
Contact: eusmool@gmail.com

---

## 🚀 Installation

**Coming Soon!** You will soon be able to install the best stable version (v1.0.0) directly via pip:
```bash
pip install scrapdiver
```

*For now, you can clone the repository and install the dependencies listed in `requirements.txt` for your Python console environments.*

---

## 💻 Usage

Scrapdiver is extremely straightforward to use. Just import the library, set up your SQLite database, queue up your target URLs, and let the diver do the work!

```python
from scrapdiver import *

# Set the SQLite database name
set_db("db.sqlite")

# Add URLs to the task pipe
add_task("https://example.com")
add_task("https://another-example.com")

# Start the screenscraping and OCR extraction process
start_diver()
```

---

## 🤖 The Power of Screenscraping for AI, RAGs, and LLMs

In the era of Artificial Intelligence, clean and accurately contextualized data is paramount. Traditional scraping methods often fail when dealing with modern, dynamically rendered Single Page Applications (SPAs). 

**How Scrapdiver bridges the gap:**
* **Retrieval-Augmented Generation (RAG):** RAG systems rely on vast, accurate vector databases. Scrapdiver ensures that the text fed into your embedding models is exactly what the user sees, capturing embedded data in images, charts, and complex UI components through OCR.
* **LLM Pre-training & Fine-tuning:** By combining visual context (screenshots) with extracted text, Scrapdiver provides rich, multimodal datasets perfect for fine-tuning Large Language Models.
* **Bypassing DOM Traps:** Many modern websites use obfuscated CSS classes and heavily nested `div` structures to prevent scraping. Because Scrapdiver takes a *printscreen* and reads it visually, it completely ignores DOM complexities.

---

## 💡 Possibilities & Projects

With Scrapdiver, the possibilities are vast. Here are a few project ideas you can build:
1. **Automated Threat Intelligence Feeds:** Sweep deep-web forums or visually complex dashboards and extract the text for automated keyword alerting.
2. **Visual Content Auditing:** Ensure that UI elements render properly across different resolutions by taking screenshots and confirming the presence of specific textual elements via OCR.
3. **Sentiment Analysis Pipelines:** Scrape lists of review sites or comment sections that heavily rely on dynamic loading, store them in SQLite, and run local LLMs to process sentiment.
4. **Historical Archiving Tool:** Create a permanent visual and textual archive of volatile web pages (news sites, competitor pricing pages) before they change.
5. **Accessibility Datasets:** Build datasets pairing visual web layouts with their textual content to train AI models focused on web accessibility for the visually impaired.

---
*Dive deep into the web with Scrapdiver!*
