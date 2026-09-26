
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
    layout="centered",
)


# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background-color: #252525;
    }

    /* Main content */
    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    h1 {
        color: #f2f0e8;
        font-size: 2.6rem;
        margin-bottom: 0.5rem;
    }

    /* Section headings */
    h2, h3 {
        color: #eeeeea;
        font-size: 1.55rem;
    }

    /* Normal text */
    p, label {
        color: #d4d1c8;
        font-size: 1.08rem;
    }

    /* Caption */
    [data-testid="stCaptionContainer"] {
        color: #aaa79f;
        font-size: 1rem;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #303030;
        border: 1px solid #44433f;
        border-radius: 10px;
        padding: 0.9rem;
    }

    /* Text input */
    [data-testid="stTextInput"] input {
        background-color: #303030;
        color: #eeeeea;
        border: 1px solid #4a4843;
        border-radius: 8px;
        font-size: 1.05rem;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #d6b84c;
        color: #000000 !important;
        border: 1px solid #c5a83f;
        border-radius: 8px;
        padding: 0.5rem 1.35rem;
        font-size: 1.02rem;
        font-weight: 600;
    }

    /* Button text */
    div.stButton > button p {
        color: #000000 !important;
    }

    /* Button hover */
    div.stButton > button:hover {
        background-color: #e2c65a;
        border-color: #d6b84c;
        color: #000000 !important;
    }

    /* Information / success / warning boxes */
    [data-testid="stAlert"] {
        border-radius: 8px;
        font-size: 1rem;
    }

    /* Metric */
    [data-testid="stMetric"] {
        background-color: #303030;
        border: 1px solid #44433f;
        border-radius: 10px;
        padding: 0.8rem;
    }

    /* Divider */
    hr {
        border-color: #44433f;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Header
# -----------------------------

st.title("📚 AI Document Assistant")

st.caption(
    "Upload a document and ask questions using AI-powered semantic search."
)


# -----------------------------
# Document Upload
# -----------------------------

st.header("📄 Upload Document")

st.write(
    "Supported formats: PDF, DOCX, and TXT."
)

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "docx", "txt"],
)

if uploaded_file:
    st.info(f"Selected document: **{uploaded_file.name}**")

    if st.button("Upload & Process"):
        with st.spinner("Reading and processing your document..."):
            try:
                response = requests.post(
                    f"{API_URL}/upload",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type,
                        )
                    },
                    timeout=120,
                )

                if response.ok:
                    result = response.json()

                    st.success(
                        "Document uploaded and processed successfully."
                    )

                    st.metric(
                        "Chunks stored",
                        result["chunks_stored"],
                    )

                else:
                    st.error(
                        f"Upload failed: {response.text}"
                    )

            except requests.exceptions.RequestException:
                st.error(
                    "Could not connect to the FastAPI server. "
                    "Make sure the backend is running."
                )


st.divider()


# -----------------------------
# Question & Answer
# -----------------------------

st.header("💬 Ask a Question")

question = st.text_input(
    "What would you like to know?",
    placeholder="Example: What are the main ideas discussed in this document?",
)

if st.button("Ask Question"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner(
            "Searching the document and generating an answer..."
        ):
            try:
                response = requests.post(
                    f"{API_URL}/query",
                    json={
                        "question": question,
                    },
                    timeout=120,
                )

                if response.ok:
                    result = response.json()

                    st.subheader("Answer")

                    st.info(result["answer"])

                    sources = result.get("sources", [])

                    if sources:
                        st.subheader("📚 Sources")

                        displayed_sources = set()

                        for source in sources:
                            source_name = source.get(
                                "source",
                                "Unknown",
                            )

                            page_number = source.get(
                                "page_number"
                            )

                            if page_number is not None:
                                source_label = (
                                    f"📄 **{source_name}** "
                                    f"— Page {page_number}"
                                )
                            else:
                                source_label = (
                                    f"📄 **{source_name}**"
                                )

                            if source_label not in displayed_sources:
                                st.write(source_label)
                                displayed_sources.add(source_label)

                    else:
                        st.info(
                            "No document sources were found for this answer."
                        )

                else:
                    st.error(
                        f"Question failed: {response.text}"
                    )

            except requests.exceptions.RequestException:
                st.error(
                    "Could not connect to the FastAPI server. "
                    "Make sure the backend is running."
                )


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "AI Document & Study Assistant • "
    "FastAPI + ChromaDB + RAG + Ollama"
)

