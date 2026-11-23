
import hashlib
from pathlib import Path
from datetime import date

import streamlit as st

# =========================================================
# AFRBS WEBSITE CONFIGURATION
# =========================================================

APP_NAME = "Advanced File Recovery And Backup System"
SHORT_NAME = "AFRBS"

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
EXE_PATH = BASE_DIR / "Nimalpranav.AFRBS_1.0.0.0_x64.msix"

# Update these whenever you release a new version.
APP_VERSION = "1.0.0"
RELEASE_DATE = "21 November 2026"
WINDOWS_REQUIREMENT = "Windows 10 / 11"

# Replace with your real Microsoft Store listing URL
MICROSOFT_STORE_URL = ""

# Replace with your real support email
SUPPORT_EMAIL = "codenimalpranav@gmail.com"

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title=f"{SHORT_NAME} | {APP_NAME}",
    page_icon=str(LOGO_PATH) if LOGO_PATH.exists() else "🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% 0%, #182451 0%, transparent 40%),
        #080b1c;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(145deg, #0b0e2d, #121742);
    border: 1px solid rgba(56,189,248,0.25);
    border-radius: 24px;
    padding: 45px 30px;
    text-align: center;
    box-shadow: 0 15px 45px rgba(0,0,0,0.25);
}

.hero h1 {
    color: #f8fafc;
    font-size: 30px;
    font-weight: 800;
    margin: 15px 0 10px 0;
}

.hero p {
    color: #94a3b8;
    font-size: 15px;
}

.version {
    display: inline-block;
    padding: 7px 14px;
    background: rgba(6,182,212,0.12);
    border: 1px solid rgba(34,211,238,0.3);
    color: #67e8f9;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
}

.store-card {
    background: linear-gradient(145deg, #101a38, #14234a);
    border: 1px solid rgba(56,189,248,0.3);
    border-radius: 18px;
    padding: 26px;
    text-align: center;
    margin-top: 20px;
}

.store-card h3 {
    color: #f8fafc;
}

.store-card p {
    color: #a5b4cf;
}

.feature-card {
    background: linear-gradient(145deg, #10152e, #121a38);
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 16px;
    padding: 20px;
    min-height: 190px;
    margin-bottom: 15px;
}

.feature-card h4 {
    color: #67e8f9;
    font-size: 16px;
}

.feature-card p {
    color: #cbd5e1;
    font-size: 13px;
    line-height: 1.7;
}

.small-text {
    color: #94a3b8;
    font-size: 12px;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px 0;
    font-size: 12px;
}

div.stDownloadButton > button {
    width: 100%;
    background: linear-gradient(135deg, #06b6d4, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px;
    font-weight: 700;
}

div.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #0891b2, #1d4ed8);
    color: white;
    border: none;
}

[data-testid="stTabs"] button {
    font-weight: 600;
}

hr {
    border-color: rgba(148,163,184,0.15);
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD FILES AND RELEASE INFORMATION
# =========================================================

logo_available = LOGO_PATH.exists()
exe_available = EXE_PATH.is_file()

exe_data = None
file_size_mb = 0
exe_hash = None

if exe_available:
    exe_data = EXE_PATH.read_bytes()
    file_size_mb = len(exe_data) / (1024 * 1024)
    exe_hash = hashlib.sha256(exe_data).hexdigest()

# =========================================================
# NAVIGATION
# =========================================================

home_tab, privacy_tab = st.tabs([
    "🏠 Home & Downloads",
    "🔒 Privacy Policy"
])

# =========================================================
# HOME PAGE
# =========================================================

with home_tab:

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    if logo_available:
        st.image(str(LOGO_PATH), width=100)

    st.markdown(
        f'<h1>{APP_NAME}</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p>Your files. Protected, organised, and recoverable.</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<span class="version">VERSION {APP_VERSION}</span>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    # -----------------------------------------------------
    # DOWNLOAD SECTION
    # -----------------------------------------------------

    st.markdown("## Download AFRBS")

    st.markdown(
        "Get the AFRBS Windows desktop application."
    )

    if exe_available:

        col1, col2 = st.columns([2, 1])

        with col1:
            st.download_button(
                label="⬇ Download AFRBS for Windows",
                data=exe_data,
                file_name="AdvancedFileRecoveryAndBackupSystem.exe",
                mime="application/vnd.microsoft.portable-executable",
                use_container_width=True
            )

        with col2:
            st.metric(
                "Download size",
                f"{file_size_mb:.2f} MB"
            )

        st.caption(
            f"{WINDOWS_REQUIREMENT} · EXE · Version {APP_VERSION}"
        )

        with st.expander("View download verification details"):
            st.write("**SHA-256 checksum**")
            st.code(exe_hash, language="text")
            st.caption(
                "You can use this checksum to verify that "
                "your downloaded executable matches the published file."
            )

    else:
        st.warning(
            "The AFRBS executable is not currently available. "
            "Please check back later."
        )

    st.write("")
    st.divider()

    # -----------------------------------------------------
    # MICROSOFT STORE SECTION
    # -----------------------------------------------------

    st.markdown("""
    <div class="store-card">
        <h3>Prefer the Microsoft Store?</h3>
        <p>
        Get AFRBS through Microsoft's official application
        distribution platform.
        </p>
        <p>
        The Store provides a familiar installation experience,
        Microsoft-managed package signing and updates when
        supported by the published application.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if MICROSOFT_STORE_URL.strip():
        st.link_button(
            "🛍 Get it from Microsoft Store",
            MICROSOFT_STORE_URL,
            use_container_width=True
        )
    else:
        st.info(
            "**Microsoft Store listing coming soon.** "
            "The Store button will become available after AFRBS "
            "has been published and its official listing URL is added."
        )

    st.caption(
        "Why choose the Store? Store distribution gives users "
        "a trusted installation channel and avoids the usual "
        "browser-downloaded unsigned EXE installation route."
    )

    st.divider()

    # -----------------------------------------------------
    # RELEASE DETAILS
    # -----------------------------------------------------

    st.markdown("## Release Information")

    c1, c2, c3 = st.columns(3)

    c1.metric("Version", APP_VERSION)
    c2.metric("Release date", RELEASE_DATE)
    c3.metric("Platform", "Windows")

    st.write("**System requirements**")
    st.markdown("""
    - Windows 10 or Windows 11.
    - Internet connection for cloud features.
    - Available storage for backups.
    """)

    st.divider()

    # -----------------------------------------------------
    # ABOUT
    # -----------------------------------------------------

    st.markdown("""
    ## About AFRBS

    **Advanced File Recovery And Backup System (AFRBS)** is
    a Windows desktop application designed to help users
    protect important files, organise backups, monitor
    duplicates, and recover previous versions.

    ---

    ## Key Features
    """)

    features = [
        (
            "1. Smart File Backup",
            "Create backups of important files, keep copies "
            "separate from originals, and track backup activity."
        ),
        (
            "2. File Recovery",
            "Access available backup copies and restore "
            "files or earlier versions when available."
        ),
        (
            "3. File Version History",
            "Maintain multiple saved versions, browse "
            "available versions, and restore earlier copies."
        ),
        (
            "4. Secure Backup Encryption",
            "Protect supported portable backups using "
            "AES-256-GCM encryption and account-password-based "
            "key derivation. Legacy DPAPI backups use "
            "Windows user-profile protection."
        ),
        (
            "5. Duplicate File Manager",
            "Detect duplicates using SHA-256 hashes, review "
            "matching files, and send selected files to "
            "the Windows Recycle Bin."
        ),
        (
            "6. File Library",
            "Browse, search, filter, organise collections, "
            "manage favourites, edit notes, and open files."
        ),
        (
            "7. Backup Dashboard",
            "View the last backup time, storage usage, "
            "and backup health information."
        ),
        (
            "8. Cloud Backup Integration",
            "Connect to the configured cloud backend, "
            "upload backup files, and store backup metadata."
        ),
        (
            "9. Duplicate Monitoring",
            "Access duplicate monitoring functionality "
            "and review detected duplicate files."
        )
    ]

    col1, col2 = st.columns(2)

    for index, (heading, description) in enumerate(features):
        target = col1 if index % 2 == 0 else col2

        with target:
            st.markdown(
                f"""
                <div class="feature-card">
                    <h4>{heading}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    # -----------------------------------------------------
    # DESIGNED FOR / WHY CHOOSE
    # -----------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        ## Designed For

        - Personal file protection
        - Important documents
        - School and work files
        - Project folders
        - Photos and personal files
        """)

    with c2:
        st.markdown("""
        ## Why Choose AFRBS?

        - Backup and recovery tools in one application.
        - Encrypted backup snapshots.
        - SHA-256 duplicate detection.
        - File version history.
        - Organised file library.
        - Backup status dashboard.
        """)

    st.success(
        "Advanced File Recovery And Backup System — "
        "Keep your files safe and your work recoverable."
    )

    st.markdown(
        '<div class="footer">© 2026 AFRBS. All rights reserved.</div>',
        unsafe_allow_html=True
    )

# =========================================================
# PRIVACY POLICY PAGE
# =========================================================

with privacy_tab:

    st.title("🔒 Privacy Policy")
    st.caption(APP_NAME)
    st.caption(f"Last updated: {RELEASE_DATE}")

    st.markdown("""
    ## 1. Introduction

    Welcome to Advanced File Recovery And Backup System (AFRBS).

    We respect your privacy and aim to protect your personal
    information and files. This policy explains how information
    may be processed when you use AFRBS.

    ## 2. Information We Process

    Depending on the features you use, AFRBS may process:

    - Account information, such as your username and email address.
    - Authentication information required for account access.
    - Backup names, file metadata, and backup timestamps.
    - File hashes used for integrity verification and duplicate detection.
    - Encrypted backup files uploaded to cloud storage.
    - Technical information needed to operate and troubleshoot the service.

    ## 3. File Access and Backups

    AFRBS accesses files and folders that you select or explicitly
    allow the application to back up.

    The application may create backup copies and process file
    metadata to provide backup, recovery, and file-management features.

    Backup contents and metadata may be stored locally or in
    configured cloud storage, depending on the features you use.

    ## 4. Encryption and Security

    AFRBS uses security measures designed to protect backup data.
    Depending on the backup format, these may include:

    - AES-256-GCM encryption for supported portable backups.
    - Account-password-based encryption for cross-PC restoration.
    - Windows Data Protection API (DPAPI) for supported
      machine/user-profile-protected backup formats.
    - SHA-256 hashing for file integrity verification.
    - Authentication controls for account access.

    Different backup formats have different restoration requirements.
    Legacy DPAPI-protected backups may only be decryptable under
    the Windows user profile and environment that protected them.

    No method of electronic storage or transmission is completely
    secure. Absolute security cannot be guaranteed.

    ## 5. Cloud Storage and Third-Party Services

    AFRBS may use Supabase services for:

    - Account authentication.
    - Database storage.
    - Cloud backup storage.

    Information processed by these services is also subject to
    their respective privacy policies and terms.

    AFRBS does not sell your personal information.

    ## 6. How Information Is Used

    Information may be used to:

    - Provide backup and recovery functionality.
    - Authenticate users and manage accounts.
    - Display backup history and storage information.
    - Verify backup integrity.
    - Detect duplicate files.
    - Maintain and troubleshoot the application.
    - Protect the service against unauthorised access.

    ## 7. Data Retention and Deletion

    Backup files and account information may remain stored while
    your account or backups are active.

    You may request account or data deletion by contacting us
    using the support email below.

    Deletion requests may require identity verification.
    Some information may need to be retained where required by law
    or for legitimate security purposes.

    Deleting an account or cloud backup does not automatically
    delete separate copies stored on your own devices.

    ## 8. Your Responsibilities

    You are responsible for:

    - Keeping your account password secure.
    - Maintaining access to recovery credentials.
    - Choosing appropriate backup locations.
    - Keeping additional copies of important files.
    - Reviewing files before restoring or deleting them.

    ## 9. Children's Privacy

    AFRBS is not knowingly designed to collect personal
    information from children without appropriate permission
    where required by applicable law.

    If you believe personal information has been provided
    improperly, please contact us.

    ## 10. Changes to This Policy

    This Privacy Policy may be updated when AFRBS features,
    security practices, or legal requirements change.

    The latest version will be published on this page.

    ## 11. Contact Information

    **Application:** Advanced File Recovery And Backup System

    **Abbreviation:** AFRBS

    **Privacy and support email:**
    """)

    st.markdown(f"**{SUPPORT_EMAIL}**")

    st.markdown("""
    Please replace the example email address in the application
    configuration with your real support email before publishing.

    ---

    © 2026 AFRBS. All rights reserved.
    """)

    st.info(
        "This privacy policy must be reviewed against your actual "
        "data collection, Supabase configuration, retention practices, "
        "and deletion procedures before public release."
    )

