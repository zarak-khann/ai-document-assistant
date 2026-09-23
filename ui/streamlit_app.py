import requests
import streamlit as st


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
)

st.title("📚 AI Document Assistant")

st.write(
    "Upload a PDF, DOCX, or TXT document and ask questions about it."
)


uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx", "txt"],
)


if uploaded_file:
    st.write(f"Selected: **{uploaded_file.name}**")

    if st.button("Upload Document"):
        with st.spinner("Processing document..."):
            response = requests.post(
                "http://127.0.0.1:8000/upload",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type,
                    )
                },
            )

        if response.ok:
            result = response.json()

            st.success(result["message"])

            st.write(
                f"Chunks stored: **{result['chunks_stored']}**"
            )

        else:
            st.error(
                f"Upload failed: {response.text}"
            )


question = st.text_input(
    "Ask a question about your document"
)


if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/query",
                json={
                    "question": question,
                },
            )

        if response.ok:
            result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

            sources = result.get("sources", [])

            if sources:
                st.subheader("Sources")

                unique_sources = set()

                for source in sources:
                    source_name = source.get("source", "Unknown")

                    if "page_number" in source:
                        source_label = (
                            f"📄 **{source_name}** — "
                            f"Page {source['page_number']}"
                        )
                    else:
                        source_label = f"📄 **{source_name}**"

                    if source_label not in unique_sources:
                        st.write(source_label)
                        unique_sources.add(source_label)

            else:
                st.info("No sources found.")

        else:
            st.error(
                f"Question failed: {response.text}"
            )