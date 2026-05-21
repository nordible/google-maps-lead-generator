import PyInstaller.__main__
import os
import shutil
import sys

# This script provides a fast local fallback for generating the executable.
# It uses PyInstaller for speed, while maintaining the robust metadata and 
# launcher logic used in the GitHub Actions pipeline.

def build():
    print("--------------------------------------------------")
    print("🛠️  Lead Generator Local Build Tool")
    print("--------------------------------------------------")
    
    # 1. Create the Launcher Wrapper
    print("📦 Creating launcher wrapper...")
    launcher_content = """
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
"""
    with open("local_launcher.py", "w", encoding="utf-8") as f:
        f.write(launcher_content.strip())

    # 2. Run PyInstaller
    print("🚀 Starting PyInstaller build... (This may take 2-3 minutes)")
    
    # Determine separator based on OS
    sep = ';' if sys.platform == 'win32' else ':'

    args = [
        'local_launcher.py',
        '--onefile',
        '--additional-hooks-dir=.',
        '--collect-all=streamlit',
        '--collect-all=langchain_openai',
        '--collect-all=playwright',
        '--collect-all=html2text',
        '--collect-all=openpyxl',
        '--collect-all=pandas',
        f'--add-data=app.py{sep}.',
        f'--add-data=src{sep}src',
        f'--add-data=.env.example{sep}.',
        '--name=GoogleMapsLeadGenerator',
        '--clean',
    ]

    # Windows Metadata
    if os.path.exists('version_info.txt'):
        args.append('--version-file=version_info.txt')

    PyInstaller.__main__.run(args)

    # 3. Cleanup
    if os.path.exists("local_launcher.py"):
        os.remove("local_launcher.py")
        
    print("\n✅ Local build complete! Check the 'dist' folder for GoogleMapsLeadGenerator.exe")

if __name__ == "__main__":
    build()
