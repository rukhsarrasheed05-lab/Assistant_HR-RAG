import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

# ── SECRETS ──────────────────────────────────────────────────────────
def get_secret(key: str) -> str:
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key, "")

os.environ["GROQ_API_KEY"]      = get_secret("GROQ_API_KEY")
os.environ["MISTRAL_API_KEY"]   = get_secret("MISTRAL_API_KEY")
os.environ["SUPABASE_URL"]      = get_secret("SUPABASE_URL")
os.environ["SUPABASE_ANON_KEY"] = get_secret("SUPABASE_ANON_KEY")
os.environ["DATABASE_URL"]      = get_secret("DATABASE_URL")

supabase = create_client(
    get_secret("SUPABASE_URL"),
    get_secret("SUPABASE_ANON_KEY")
)

# ── PAGE CONFIG ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="AssistHR",
    page_icon="🤖",
    layout="centered"
)

# ══════════════════════════════════════════════════════════════════════
#  EMBEDDED CSS  (no external file needed)
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --bg       : #080c18;
    --bg2      : #0e1525;
    --card     : #131c30;
    --card-h   : #18243d;
    --border   : #1a2640;
    --border-l : #223050;
    --indigo   : #6366f1;
    --indigo-l : #818cf8;
    --gold     : #f59e0b;
    --emerald  : #10b981;
    --rose     : #f43f5e;
    --txt      : #dde4f0;
    --txt2     : #7b93b8;
    --txt3     : #3d5270;
    --glow     : rgba(99,102,241,0.14);
    --r        : 12px;
    --r-s      : 8px;
    --t        : 0.22s cubic-bezier(.4,0,.2,1);
}

*, *::before, *::after { box-sizing:border-box; }
html, body, [class*="css"] {
    font-family:'DM Sans',sans-serif !important;
    color:var(--txt) !important;
    background:var(--bg) !important;
}
::-webkit-scrollbar { width:4px; height:4px; }
::-webkit-scrollbar-track { background:var(--bg2); }
::-webkit-scrollbar-thumb { background:var(--border-l); border-radius:99px; }

.stApp {
    background:
        radial-gradient(ellipse 60% 40% at 15% 0%, rgba(99,102,241,.09) 0%, transparent 70%),
        radial-gradient(ellipse 50% 35% at 85% 100%, rgba(245,158,11,.06) 0%, transparent 70%),
        var(--bg) !important;
}
.block-container {
    padding-top:2rem !important;
    padding-bottom:4rem !important;
    max-width:880px !important;
}

h1,h2,h3 { font-family:'Sora',sans-serif !important; letter-spacing:-.02em !important; }
h1 { font-size:2.1rem !important; font-weight:800 !important; color:var(--txt) !important; }
h2 { font-size:1.45rem !important; font-weight:700 !important; color:var(--txt) !important; }
h3 { font-size:1.1rem !important; font-weight:600 !important; color:var(--txt2) !important; }
.stMarkdown p, [data-testid="stMarkdownContainer"] p {
    color:var(--txt2) !important; line-height:1.75 !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background:var(--bg2) !important;
    border-right:1px solid var(--border) !important;
    padding:1.5rem 1rem !important;
}
[data-testid="stSidebar"] .stRadio > div { gap:2px !important; }
[data-testid="stSidebar"] .stRadio label {
    display:flex !important; align-items:center !important; gap:10px !important;
    padding:10px 14px !important; border-radius:var(--r-s) !important;
    font-size:.9rem !important; font-weight:500 !important;
    color:var(--txt2) !important; cursor:pointer !important;
    transition:var(--t) !important; border:1px solid transparent !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background:var(--card) !important; color:var(--txt) !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color:var(--txt3) !important; font-size:.75rem !important;
}

/* BUTTONS */
.stButton > button {
    background:linear-gradient(135deg,var(--indigo),var(--indigo-l)) !important;
    color:#fff !important; border:none !important;
    border-radius:var(--r-s) !important; padding:.6rem 1.6rem !important;
    font-family:'DM Sans',sans-serif !important; font-weight:600 !important;
    font-size:.9rem !important; transition:var(--t) !important;
    box-shadow:0 4px 18px rgba(99,102,241,.35) !important;
}
.stButton > button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 7px 24px rgba(99,102,241,.52) !important;
}
.stButton > button:active { transform:translateY(0) !important; }
.stButton > button[kind="secondary"] {
    background:transparent !important; border:1px solid var(--border-l) !important;
    color:var(--txt2) !important; box-shadow:none !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color:var(--indigo) !important; color:var(--indigo) !important;
    background:var(--glow) !important; box-shadow:none !important;
}

/* INPUTS */
.stTextInput > div > div {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:var(--r-s) !important; transition:var(--t) !important;
}
.stTextInput > div > div:focus-within {
    border-color:var(--indigo) !important; box-shadow:0 0 0 3px var(--glow) !important;
}
.stTextInput input { color:var(--txt) !important; font-family:'DM Sans',sans-serif !important; font-size:.9rem !important; }
.stTextInput input::placeholder { color:var(--txt3) !important; }
.stTextInput label { color:var(--txt2) !important; font-weight:500 !important; font-size:.82rem !important; }

/* SELECTBOX */
.stSelectbox > div > div {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:var(--r-s) !important; color:var(--txt) !important;
}
.stSelectbox label { color:var(--txt2) !important; font-size:.82rem !important; }

/* TABS */
.stTabs [data-baseweb="tab-list"] {
    background:var(--card) !important; border-radius:var(--r-s) !important;
    padding:4px !important; border:1px solid var(--border) !important; gap:2px !important;
}
.stTabs [data-baseweb="tab"] {
    background:transparent !important; border-radius:6px !important;
    color:var(--txt2) !important; font-weight:500 !important; font-size:.88rem !important;
    padding:8px 20px !important; border:none !important; transition:var(--t) !important;
}
.stTabs [aria-selected="true"] {
    background:var(--indigo) !important; color:#fff !important;
    box-shadow:0 2px 10px rgba(99,102,241,.4) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding:1.5rem 0 0 !important; }

/* METRICS */
[data-testid="stMetric"] {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:var(--r) !important; padding:1.3rem 1.4rem !important;
    transition:var(--t) !important; position:relative !important; overflow:hidden !important;
}
[data-testid="stMetric"]::before {
    content:''; position:absolute; top:0; left:0; right:0; height:2px;
    background:linear-gradient(90deg,var(--indigo),var(--gold));
}
[data-testid="stMetric"]:hover {
    border-color:var(--border-l) !important; transform:translateY(-2px) !important;
    box-shadow:0 8px 28px rgba(0,0,0,.4) !important;
}
[data-testid="stMetricLabel"] p {
    color:var(--txt2) !important; font-size:.75rem !important; font-weight:600 !important;
    text-transform:uppercase !important; letter-spacing:.08em !important;
}
[data-testid="stMetricValue"] {
    color:var(--txt) !important; font-family:'Sora',sans-serif !important;
    font-size:1.9rem !important; font-weight:700 !important;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background:var(--card) !important; border:2px dashed var(--border-l) !important;
    border-radius:var(--r) !important; transition:var(--t) !important;
}
[data-testid="stFileUploader"]:hover {
    border-color:var(--indigo) !important; background:var(--glow) !important;
}

/* CHAT */
[data-testid="stChatMessage"] {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:var(--r) !important; padding:1rem 1.2rem !important; margin-bottom:.6rem !important;
}
[data-testid="stChatInput"] textarea {
    background:var(--card) !important; border:1px solid var(--border-l) !important;
    border-radius:var(--r) !important; color:var(--txt) !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color:var(--indigo) !important; box-shadow:0 0 0 3px var(--glow) !important; outline:none !important;
}

/* EXPANDER */
[data-testid="stExpander"] {
    background:var(--card) !important; border:1px solid var(--border) !important;
    border-radius:var(--r) !important; margin-bottom:.6rem !important; overflow:hidden !important;
}
[data-testid="stExpander"] summary {
    color:var(--txt) !important; font-weight:600 !important; padding:1rem 1.2rem !important;
}
[data-testid="stExpander"] summary:hover { background:var(--card-h) !important; }

/* PROGRESS */
.stProgress > div > div { background:var(--border) !important; border-radius:99px !important; height:7px !important; }
.stProgress > div > div > div { background:linear-gradient(90deg,var(--indigo),var(--gold)) !important; border-radius:99px !important; }

/* ALERTS */
.stSuccess { background:rgba(16,185,129,.1) !important; border:1px solid rgba(16,185,129,.3) !important; color:#6ee7b7 !important; }
.stError   { background:rgba(244,63,94,.1)  !important; border:1px solid rgba(244,63,94,.3)  !important; color:#fda4af !important; }
.stWarning { background:rgba(245,158,11,.1) !important; border:1px solid rgba(245,158,11,.3) !important; }
.stInfo    { background:rgba(99,102,241,.1) !important; border:1px solid rgba(99,102,241,.3) !important; color:#a5b4fc !important; }
[data-testid="stAlert"] { border-radius:var(--r-s) !important; }

hr { border-color:var(--border) !important; margin:1.4rem 0 !important; }
.stApp .stCaption, [data-testid="stCaptionContainer"] p { color:var(--txt3) !important; font-size:.76rem !important; }
.stSpinner > div { border-top-color:var(--indigo) !important; }

/* DOC ITEM */
.doc-item {
    background:var(--card); border:1px solid var(--border); border-radius:var(--r-s);
    padding:11px 16px; margin-bottom:5px; color:var(--txt2); font-size:.88rem;
    display:flex; align-items:center; gap:10px; transition:var(--t);
}
.doc-item:hover { border-color:var(--border-l); color:var(--txt); transform:translateX(4px); }

/* SKILL PILLS */
.pill-green { background:rgba(16,185,129,.15); color:#6ee7b7; padding:3px 11px; border-radius:99px; font-size:.76rem; display:inline-block; margin:3px; }
.pill-red   { background:rgba(244,63,94,.15);  color:#fda4af; padding:3px 11px; border-radius:99px; font-size:.76rem; display:inline-block; margin:3px; }

/* LOGIN HERO */
.hero { text-align:center; padding:2.5rem 0 1.8rem; }
.hero-icon { font-size:3.5rem; display:block; margin-bottom:.5rem; animation:float 3s ease-in-out infinite; }
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
.hero-title {
    font-family:'Sora',sans-serif; font-size:3rem; font-weight:800;
    background:linear-gradient(135deg,#ffffff 0%,var(--indigo-l) 50%,var(--gold) 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    margin:0 0 .4rem; letter-spacing:-.03em;
}
.hero-sub { color:var(--txt3); font-size:.95rem; margin:0; }

/* USER BADGE */
.user-badge { background:var(--card); border:1px solid var(--border); border-radius:10px; padding:10px 14px; margin-bottom:12px; }
.user-badge-label { font-size:.68rem; color:var(--txt3); text-transform:uppercase; letter-spacing:.07em; margin-bottom:4px; }
.user-badge-email { font-size:.83rem; color:var(--txt2); font-weight:500; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }

/* PAGE HEADER */
.page-header { margin-bottom:1.5rem; }
.page-header h1 { margin-bottom:.2rem !important; }
.page-header p  { color:var(--txt3); font-size:.88rem; margin:0; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
#  LOGIN
# ══════════════════════════════════════════════════════════════════════
def login_page():
    st.markdown("""
        <div class="hero">
            <span class="hero-icon">🤖</span>
            <h1 class="hero-title">AssistHR</h1>
            <p class="hero-sub">AI-powered HR Assistant — smarter hiring, faster decisions</p>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔑  Login", "📝  Register"])

    with tab1:
        st.markdown("<p style='color:var(--txt3);font-size:.84rem;margin-bottom:.8rem;'>Welcome back! Sign in to continue.</p>", unsafe_allow_html=True)
        email    = st.text_input("Email",    key="login_email", placeholder="you@company.com")
        password = st.text_input("Password", key="login_pass",  placeholder="••••••••", type="password")
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        if st.button("Login", use_container_width=True):
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                try:
                    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                    st.session_state.user  = res.user
                    st.session_state.token = res.session.access_token
                    st.success("✅ Logged in! Redirecting…")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Login failed: {e}")

    with tab2:
        st.markdown("<p style='color:var(--txt3);font-size:.84rem;margin-bottom:.8rem;'>Create your free account.</p>", unsafe_allow_html=True)
        name     = st.text_input("Full Name",       key="reg_name",    placeholder="John Smith")
        email    = st.text_input("Email",            key="reg_email",   placeholder="you@company.com")
        password = st.text_input("Password",         key="reg_pass",    placeholder="Min 6 characters", type="password")
        confirm  = st.text_input("Confirm Password", key="reg_confirm", placeholder="Repeat password",  type="password")
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        if st.button("Create Account", use_container_width=True):
            if not name or not email or not password or not confirm:
                st.error("Please fill in all fields.")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters.")
            elif password != confirm:
                st.error("Passwords do not match.")
            else:
                try:
                    supabase.auth.sign_up({"email": email, "password": password, "options": {"data": {"name": name}}})
                    st.success("✅ Account created! Please login.")
                except Exception as e:
                    st.error(f"❌ Registration failed: {e}")


# ══════════════════════════════════════════════════════════════════════
#  LOGOUT
# ══════════════════════════════════════════════════════════════════════
def logout():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    st.session_state.user  = None
    st.session_state.token = None
    st.rerun()


# ══════════════════════════════════════════════════════════════════════
#  SESSION INIT
# ══════════════════════════════════════════════════════════════════════
if "user" not in st.session_state:
    st.session_state.user  = None
    st.session_state.token = None

if not st.session_state.user:
    login_page()
    st.stop()

current_user  = st.session_state.user
current_email = current_user.email


# ══════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
        <div style='display:flex;align-items:center;gap:10px;margin-bottom:4px;'>
            <span style='font-size:1.5rem;'>🤖</span>
            <span style='font-family:Sora,sans-serif;font-size:1.15rem;font-weight:700;color:#dde4f0;'>AssistHR</span>
        </div>
        <p style='color:#3d5270;font-size:.73rem;margin:0 0 1.2rem 2px;'>AI-Powered HR Assistant</p>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "📄 Documents", "💬 Chat", "👥 Screening"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(f"""
        <div class="user-badge">
            <div class="user-badge-label">Logged in as</div>
            <div class="user-badge-email">👤 {current_email}</div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Logout", use_container_width=True):
        logout()

    st.divider()
    st.markdown("<p style='color:#3d5270;font-size:.7rem;text-align:center;'>AssistHR v1.0</p>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
#  DASHBOARD
# ══════════════════════════════════════════════════════════════════════
if page == "📊 Dashboard":
    st.markdown("""
        <div class="page-header">
            <h1>📊 Dashboard</h1>
            <p>Overview of your HR workspace</p>
        </div>
    """, unsafe_allow_html=True)

    from embedding import get_existing_files

    try:
        all_docs   = get_existing_files()
        docs_count = len(all_docs)
    except Exception:
        all_docs   = []
        docs_count = 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄  Documents",  docs_count)
    with col2:
        st.metric("🤖  AI Model",   "Groq")
    with col3:
        st.metric("🗄️  Vector DB",  "Supabase")

    st.divider()
    st.markdown("<h3 style='margin-bottom:.75rem;'>📁 Uploaded Documents</h3>", unsafe_allow_html=True)

    if not all_docs:
        st.info("No documents uploaded yet. Go to **Documents** to upload your first file.")
    else:
        for doc in all_docs:
            st.markdown(f'<div class="doc-item">📄 {doc}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
#  DOCUMENTS
# ══════════════════════════════════════════════════════════════════════
elif page == "📄 Documents":
    st.markdown("""
        <div class="page-header">
            <h1>📄 HR Documents</h1>
            <p>Upload and manage your policy &amp; knowledge base</p>
        </div>
    """, unsafe_allow_html=True)

    from document_loader import load_document
    from chunking        import chunk_documents
    from embedding       import create_vector_store, get_existing_files

    st.markdown("<h3 style='margin-bottom:.5rem;'>⬆️ Upload Document</h3>", unsafe_allow_html=True)
    uploaded = st.file_uploader("Drag & drop or click to browse", type=["pdf", "docx", "txt"])

    if uploaded:
        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        if st.button("⚙️  Upload & Process", use_container_width=True):
            with st.spinner(f"Processing '{uploaded.name}'…"):
                tmp_path = f"/tmp/{uploaded.name}"
                with open(tmp_path, "wb") as f:
                    f.write(uploaded.getbuffer())
                try:
                    docs   = load_document(tmp_path)
                    chunks = chunk_documents(docs)
                    create_vector_store(chunks)
                    st.success(f"✅ '{uploaded.name}' processed — {len(chunks)} chunks created.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)

    st.divider()
    st.markdown("<h3 style='margin-bottom:.75rem;'>📂 Existing Documents</h3>", unsafe_allow_html=True)

    try:
        existing = get_existing_files()
        if not existing:
            st.info("No documents uploaded yet.")
        else:
            for doc in existing:
                st.markdown(f'<div class="doc-item">📄 {doc}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Could not load documents: {e}")


# ══════════════════════════════════════════════════════════════════════
#  CHAT
# ══════════════════════════════════════════════════════════════════════
elif page == "💬 Chat":
    st.markdown("""
        <div class="page-header">
            <h1>💬 HR Assistant</h1>
            <p>Ask anything about HR policies, leaves, compliance &amp; more</p>
        </div>
    """, unsafe_allow_html=True)

    from rag_chain  import ask
    from chat_store import create_session, load_history

    col1, col2 = st.columns([2, 1])
    with col1:
        session_id = st.text_input("Session Name", value="default", placeholder="e.g. hr-queries")
    with col2:
        model = st.selectbox("Model", [
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
            "meta-llama/llama-4-scout-17b-16e-instruct",
        ])

    full_session = f"{current_email}_{session_id}"

    if ("messages"     not in st.session_state or
        "last_session" not in st.session_state or
         st.session_state.last_session != full_session):
        st.session_state.last_session = full_session
        try:
            create_session(full_session)
            history = load_history(full_session)
            st.session_state.messages = [
                {"role": "user" if m.type == "human" else "assistant", "content": m.content}
                for m in history
            ]
        except Exception:
            st.session_state.messages = []

    st.divider()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Ask about HR policies, leave, dress code…"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("AssistHR is thinking…"):
                try:
                    answer = ask(prompt, full_session, model)
                    st.write(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"❌ Error: {e}")


# ══════════════════════════════════════════════════════════════════════
#  SCREENING
# ══════════════════════════════════════════════════════════════════════
elif page == "👥 Screening":
    st.markdown("""
        <div class="page-header">
            <h1>👥 Resume Screening</h1>
            <p>Upload a JD and resumes — AI ranks the best candidates instantly</p>
        </div>
    """, unsafe_allow_html=True)

    from screener import screen_all

    model = st.selectbox("AI Model", [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "meta-llama/llama-4-scout-17b-16e-instruct",
    ])

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='margin-bottom:.5rem;'>📋 Job Description</h3>", unsafe_allow_html=True)
        jd = st.file_uploader("Upload JD (PDF or DOCX)", type=["pdf", "docx"], key="jd")
    with col2:
        st.markdown("<h3 style='margin-bottom:.5rem;'>📄 Resumes</h3>", unsafe_allow_html=True)
        resumes = st.file_uploader(
            "Upload Resumes (multiple allowed)",
            type=["pdf", "docx", "jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="resumes"
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if st.button("🔍  Screen Candidates", type="primary", use_container_width=True):
        if not jd:
            st.error("Please upload a Job Description.")
        elif not resumes:
            st.error("Please upload at least one resume.")
        else:
            jd_path = f"/tmp/{jd.name}"
            with open(jd_path, "wb") as f:
                f.write(jd.getbuffer())

            resume_paths = []
            for r in resumes:
                path = f"/tmp/{r.name}"
                with open(path, "wb") as f:
                    f.write(r.getbuffer())
                resume_paths.append(path)

            with st.spinner("Screening candidates… this may take a moment."):
                try:
                    results = screen_all(resume_paths, jd_path, model)
                except Exception as e:
                    st.error(f"❌ Screening failed: {e}")
                    results = []

            if os.path.exists(jd_path):
                os.remove(jd_path)
            for path in resume_paths:
                if os.path.exists(path):
                    os.remove(path)

            if results:
                st.success(f"✅ Screened {len(results)} candidate(s)")
                st.divider()

                for i, r in enumerate(results, 1):
                    verdict = r.get("verdict", "")
                    score   = r.get("score",   0)
                    name    = r.get("name",    "Unknown")

                    bar_color = (
                        "#10b981" if score >= 75 else
                        "#f59e0b" if score >= 50 else
                        "#f43f5e"
                    )

                    with st.expander(f"#{i}  {name}   |   {score}%   |   {verdict}"):

                        c1, c2 = st.columns(2)
                        c1.metric("Score",      f"{score}%")
                        c2.metric("Experience", r.get("experience", "Not specified"))

                        st.markdown(f"""
                            <div style='background:var(--border);border-radius:99px;
                                        height:7px;margin:8px 0 16px;overflow:hidden;'>
                                <div style='width:{score}%;height:100%;border-radius:99px;
                                    background:linear-gradient(90deg,var(--indigo),{bar_color});
                                    transition:width .6s ease;'></div>
                            </div>
                        """, unsafe_allow_html=True)

                        st.divider()

                        c1, c2 = st.columns(2)
                        c1.write(f"📧 {r.get('email', 'N/A')}")
                        c1.write(f"📞 {r.get('phone', 'N/A')}")
                        c2.write(f"🎓 {r.get('education', 'N/A')}")
                        if r.get("linkedin"):
                            c2.write(f"🔗 [LinkedIn]({r.get('linkedin')})")
                        if r.get("github"):
                            c2.write(f"💻 [GitHub]({r.get('github')})")

                        st.divider()

                        c1, c2 = st.columns(2)
                        with c1:
                            if r.get("matched_skills"):
                                st.markdown("**✅ Matched Skills**")
                                pills = "".join(f'<span class="pill-green">{s}</span>' for s in r["matched_skills"])
                                st.markdown(pills, unsafe_allow_html=True)
                        with c2:
                            if r.get("missing_skills"):
                                st.markdown("**❌ Missing Skills**")
                                pills = "".join(f'<span class="pill-red">{s}</span>' for s in r["missing_skills"])
                                st.markdown(pills, unsafe_allow_html=True)

                        st.divider()
                        st.write(f"💪 **Strengths:** {r.get('strengths', '')}")
                        st.write(f"⚠️ **Weaknesses:** {r.get('weaknesses', '')}")
                        st.caption(f"Model used: {r.get('model')}")
            else:
                st.warning("No results returned.")