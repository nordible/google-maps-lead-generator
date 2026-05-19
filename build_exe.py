import PyInstaller.__main__
import os
import shutil

# This script bundles the Streamlit app into a single executable folder.
# Note: Users will still need to have Google Chrome installed on their system
# for Playwright to function correctly in the bundled version.

def build():
    print("🚀 Starting build process...")
    
    # Define the main entry point for the executable
    # We use a wrapper to start streamlit
    with open("launcher.py", "w") as f:
        f.write("""
import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(bundle_dir, path)

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
""")

    PyInstaller.__main__.run([
        'launcher.py',
        '--onefile',
        '--additional-hooks-dir=.',
        '--add-data=app.py;.',
        '--add-data=src;src',
        '--add-data=.env.example;.',
        '--name=LeadGenerator',
        '--clean',
    ])

    # Cleanup
    if os.path.exists("launcher.py"):
        os.remove("launcher.py")
        
    print("\n✅ Build complete! Check the 'dist' folder for LeadGenerator.exe")

if __name__ == "__main__":
    build()
