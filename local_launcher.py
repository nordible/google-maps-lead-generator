import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    # Handle PyInstaller paths
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

if __name__ == "__main__":
    print("--------------------------------------------------")
    print("🚀 AI-Powered Google Maps Lead Generator")
    print("--------------------------------------------------")
    print("📦 Initializing system... (May take a moment)")
    print("🌐 Starting web server...")
    
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())