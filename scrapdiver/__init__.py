import sqlite3
import time
from PIL import Image
from rapidocr import RapidOCR
from playwright.sync_api import sync_playwright
from urllib.parse import urlparse

_db_name = "db.sqlite"
_tasks = []
_ocr = RapidOCR()

def set_db(db_name):
    global _db_name
    _db_name = db_name
    _create_table()


def _get_connection():
    return sqlite3.connect(_db_name)


def _create_table():
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS www_scraperdiver (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            www_uri TEXT NOT NULL,
            www_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def add_task(_uri):
    if not isinstance(_uri, str):
        raise TypeError("URL only is string.")
    _uri = _uri.strip()
    if not _uri:
        raise ValueError("URL is empty.")
    parsed = urlparse(_uri)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(
            "Star URL with http:// or https://"
        )
    _tasks.append(_uri)
    print(f"[TASK] URL added: {_uri}")

def _screenscrape_url(page, url):
    try:
        print("[BROWSER] Opening URL...")
        page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )
        print("[BROWSER] Page loaded.")
        time.sleep(3)
        print("[SCREEN] Capturing page...")
        screenshot_path = (
            "www_scraperdiver_screen.png"
        )
        page.screenshot(
            path=screenshot_path,
            full_page=True
        )
        print("[OCR] Processing screenshot...")
        image = Image.open(
            screenshot_path
        )
        result = _ocr(
            image
        )
        text = ""
        if result and result.txts:

            text = "\n".join(
                result.txts
            )
        text = text.strip()
        return text
    except Exception as e:
        print(f"[ERROR] {url}")
        print(f"        {e}")
        return None


def _save_result(url, text):
    conn = _get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO www_scraperdiver
        (
            www_uri,
            www_text
        )
        VALUES (?, ?)
    """, (
        url,
        text
    ))
    conn.commit()
    conn.close()

def start_diver():
    if not _db_name:
        raise RuntimeError(
            "Database not configured "
            "Execute set_db('db.sqlite') after."
        )
    if not _tasks:
        print("[DIVER] URL pipe is empty.")
        return
    _create_table()
    print("")
    print("======================================")
    print(" WWW SCRAPER DIVER")
    print("======================================")
    print(f"Database: {_db_name}")
    print(f"URLs:  {len(_tasks)}")
    print("======================================")
    print("")
    total = len(_tasks)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False
        )
        page = browser.new_page(
            viewport={
                "width": 1920,
                "height": 1080
            }
        )
        for index, url in enumerate(
            _tasks,
            start=1
        ):
            print(
                f"[{index}/{total}] "
                f"Screenscraping: {url}"
            )
            text = _screenscrape_url(
                page,
                url
            )
            if text is None:
                print(
                    "[SKIP] "
                    "Screen/OCR error."
                )
                print("")
                continue
            _save_result(
                url,
                text
            )
            print(
                f"[OK] "
                f"{len(text)} saved chars."
            )
            print("")
            time.sleep(1)
        browser.close()
    print("======================================")
    print(" DIVER END ")
    print("======================================")