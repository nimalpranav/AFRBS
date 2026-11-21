import base64
from pathlib import Path
import streamlit as st

# 1. Load your logo for the title bar and HTML card
logo_path = Path("logo.png")
b64_logo = base64.b64encode(logo_path.read_bytes()).decode()

st.set_page_config(
    page_title="Advanced File Recovery And Backup System",
    page_icon=str(logo_path),
    layout="centered",
)

# 2. Load your .exe file
exe_path = Path("AdvancedFileRecoveryAndBackupSystem.exe")
file_size_mb = round(exe_path.stat().st_size / (1024 * 1024), 2)
b64_exe = base64.b64encode(exe_path.read_bytes()).decode()

# 3. Stylish Download Card matching your logo's deep navy & cyan-blue theme
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://cloudflare.com">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  body {{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: transparent;
    padding: 16px;
  }}
  .card {{
    background: linear-gradient(145deg, #0b0e2d, #121742);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 20px;
    padding: 40px 32px;
    max-width: 520px;
    width: 100%;
    text-align: center;
    box-shadow: 0 16px 36px rgba(11, 14, 45, 0.28);
    color: #ffffff;
  }}
  .icon-badge {{
    width: 88px;
    height: 88px;
    margin: 0 auto 20px;
    border-radius: 22px;
    overflow: hidden;
    border: 2px solid rgba(34, 211, 238, 0.4);
    box-shadow: 0 0 24px rgba(34, 211, 238, 0.25);
    background: #0b0e2d;
  }}
  .icon-badge img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  h1 {{
    font-size: 23px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 10px;
    line-height: 1.3;
  }}
  p.subtitle {{
    font-size: 14.5px;
    color: #94a3b8;
    margin-bottom: 28px;
    line-height: 1.5;
  }}
  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
    background: linear-gradient(135deg, #06b6d4, #2563eb);
    color: #ffffff;
    padding: 15px 24px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.35);
  }}
  .btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(6, 182, 212, 0.5);
  }}
  .btn:active {{
    transform: translateY(0);
  }}
  .meta {{
    margin-top: 16px;
    font-size: 12.5px;
    color: #64748b;
  }}
</style>
</head>
<body>

  <div class="card">
    <div class="icon-badge">
      <img src="data:image/png;base64,{b64_logo}" alt="AFRBS Logo">
    </div>
    <h1>Advanced File Recovery And Backup System</h1>
    <p class="subtitle">Your files. Protected, organised, and recoverable.</p>
    
    <a href="data:application/octet-stream;base64,{b64_exe}" download="AdvancedFileRecoveryAndBackupSystem.exe" class="btn">
      <i class="fa fa-download"></i> Download for Windows
    </a>
    
    <div class="meta">Windows 10 / 11 &bull; {file_size_mb} MB &bull; .EXE</div>
  </div>

</body>
</html>
"""

st.iframe(html_code, height=430)

st.divider()

# 4. Product Overview & Features Summary
st.markdown("""
### About AFRBS
**Advanced File Recovery And Backup System (AFRBS)** is a Windows desktop application that helps you protect important files, organise backups, monitor duplicates, and recover previous versions.

---

### Key Features
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 1. Smart File Backup
    - Create backups of important files.
    - Keep backup copies separate from original files.
    - Track backup information and file details.
    - View your previous backup activity.

    #### 3. File Version History
    - Maintain multiple saved versions of files.
    - Browse available file versions.
    - Compare versions to identify changes.
    - Restore an earlier version when needed.

    #### 5. Duplicate File Manager
    - Detect duplicate files using SHA-256 hashes.
    - Review detected duplicate files.
    - Select individual files for deletion & confirm.
    - Send deleted files to the Windows Recycle Bin.

    #### 7. Backup Dashboard
    - View the last backup time.
    - Check storage usage with charts.
    - View the backup health indicator.
    - Get a quick overview of backup status.

    #### 9. Duplicate Monitoring
    - Run the duplicate monitoring component.
    - Monitor files for duplicate-related activity.
    - Access the duplicate manager to review detected files.
    """)

with col2:
    st.markdown("""
    #### 2. File Recovery
    - Access available backup copies.
    - Restore files from saved backups.
    - Recover earlier versions when available.
    - Keep your original files organised.

    #### 4. Secure Backup Encryption
    - Protect new backup snapshots with AES-256-GCM encryption.
    - Use Windows DPAPI to protect encryption keys.
    - Keep encrypted backup data protected from unauthorised access.
    - Preserve compatibility with existing unencrypted `.bak` backups.

    #### 6. File Library
    - Browse, search, filter, and organise collections.
    - Add/remove favourites and edit file notes.
    - Open files directly (or double-click) and locate in File Explorer.
    - Access extra actions through the three-dot menu.

    #### 8. Cloud Backup Integration
    - Connect the application to its configured cloud backend.
    - Upload backup records and files to Supabase Storage.
    - Keep backup metadata in the connected database.
    - Access cloud backup functionality through the application.
    """)

st.info("**Important:** DPAPI-protected backups are tied to the Windows user profile that created them. Keep your Windows profile and recovery arrangements safe.")

st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    ### Designed For
    - Personal file protection
    - Important documents
    - School and work files
    - Project folders
    - Photos and other personal files
    """)

with c2:
    st.markdown("""
    ### Why Choose AFRBS?
    - File backup and recovery tools in one application.
    - Encrypted backup snapshots & SHA-256 duplicate detection.
    - File version history & organised file library.
    - Backup status dashboard & Windows desktop integration.
    """)

st.success("**Advanced File Recovery And Backup System — Keep your files safe and your work recoverable.**")
