# 🚀 AI-Powered Google Maps Lead Generator: Universal Setup Guide

This guide will help you set up the Google Maps Lead Generator on **Windows, macOS, or Linux** from scratch. 

## 📋 Prerequisites
Before you begin, you will need:
1. **Python 3.10 or higher**
2. **Serper API Key:** [Get it here (2,500 free searches)](https://serper.dev)
3. **OpenRouter API Key:** [Get it here](https://openrouter.ai/) (Add $5 credits for best results)

---

## 💰 Lead Capacity & ROI ($15 Investment)
If you invest **$15** ($10 in Serper + $5 in OpenRouter), here is what you can expect:

| API | Investment | Leads Generated | Notes |
| :--- | :--- | :--- | :--- |
| **Serper.dev** | $10 (50k credits) | **~16,500 Leads** | Each search (20 results) costs 3 credits. |
| **OpenRouter** | $5 (Credits) | **~10,000+ Leads** | Using `gpt-4o-mini` (extremely cheap). |
| **Total** | **$15** | **~10,000+ Full Leads** | Fully enriched with emails and social media. |

**Comparison:** Other platforms charge ~$150 for 1,000 leads. With this tool, you get **10x the data for 10% of the cost.**

---

## 🛠️ Step 1: Install Python

### **Windows**
1. Download the latest installer from [python.org](https://www.python.org/downloads/windows/).
2. **IMPORTANT:** Check the box that says **"Add Python to PATH"** during installation.

### **macOS**
1. Open Terminal and install via Homebrew (recommended):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install python
   ```

### **Linux (Ubuntu/Debian)**
1. Open Terminal and run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

---

## 📂 Step 2: Download & Prepare the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nordible/google-maps-lead-generator.git
   cd google-maps-lead-generator
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   # Windows
   python -m venv venv && venv.\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Browsers (For Web Scraping):**
   ```bash
   python -m playwright install chromium
   ```

---

## 🔑 Step 3: Configure API Keys

1. Create a file named `.env` in the root folder (or rename `.env.example`).
2. Open it with any text editor and add your keys:

```env
SERPER_API_KEY="your_serper_key_here"
OPENROUTER_API_KEY="your_openrouter_key_here"
LLM_MODEL="openai/gpt-4o-mini"
```

---

## 🚀 Step 4: Run the Generator

### **Option 1: Command Line (Fastest)**
Edit the bottom of `main.py` to set your desired location and business type, then run:
```bash
python main.py
```

### **Option 2: Web Interface (User Friendly)**
```bash
python -m streamlit run app.py
```
*A browser window will open automatically where you can enter your search queries.*

---

## 🐳 Option 3: Docker Setup (Easiest & Most Reliable)
If you have Docker installed, this is the recommended way to run the app as it handles all dependencies (Playwright, Python, etc.) automatically.

1. **Install Docker:** Download from [docker.com](https://www.docker.com/).
2. **Configure `.env`:** Ensure your `.env` file is ready with your API keys.
3. **Run the container:**
   ```bash
   docker-compose up --build
   ```
4. **Access the App:** Open `http://localhost:8501` in your browser.

---

## 📦 Option 4: One-Click Executable (Best for Privacy)
If you want to run the app without touching the source code or installing Python manually, you can use the standalone executable.

1. **Download:** [Insert Link to your LeadGenerator.exe here]
2. **Setup:** 
   - Place the `.exe` in a new folder.
   - Create a `.env` file in the same folder with your keys.
3. **Run:** Double-click `LeadGenerator.exe`.
   - *Note: The first launch may take 30-60 seconds to extract components.*

---

## 🔒 Protecting Your Source Code
If you are distributing this tool and want to hide your logic:
- **Use the Executable:** The PyInstaller build (Option 4) bundles your code into a binary format that is harder to read than raw `.py` files.
- **Docker:** (Option 3) keeps your environment and code inside a container, which is excellent for professional deployments.
- **Obfuscation:** For maximum security, you can run `pip install pyarmor` and obfuscate the `src/` folder before building the executable.

---

## 🧪 Troubleshooting
- **Windows Filename Error:** Ensure your code uses underscores `_` instead of colons `:` in filenames.
- **Missing Credentials:** Ensure `load_dotenv(override=True)` is used in your script to force-load the `.env` file.
- **Playwright Error:** Run `python -m playwright install chromium` again if scraping fails.

---

## 💰 Cost Breakdown (Market Comparison)
| Tool | Cost (Monthly) | Cost (INR) |
| :--- | :--- | :--- |
| Apollo/Clay | ~$60 - $150 | ₹5,000 - ₹12,000 |
| **This Tool** | **~$5 (Pay-as-you-go)** | **~₹420** |

---
*Created for marketing and distribution.*
