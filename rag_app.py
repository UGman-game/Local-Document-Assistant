from shiny import App, ui, render, reactive
from backend import query_rag, create_vectorstore_from_uploaded_file, extract_preview_from_file

app_ui = ui.page_fluid(
    ui.h2("📚🤖 Local Document Assistant - Realtime Document Information Extract"),
    ui.h3("Provide context for more better responses (upload a file first)"),

    # File upload input (drag-and-drop supported natively)
    ui.input_file("upload", "Upload a PDF, DOCX, or TXT file only (Drag-and-drop supported):", accept=[".pdf", ".docx", ".txt"]),
    ui.output_text_verbatim("upload_status"),
    ui.output_text_verbatim("file_preview"),  # <- Preview area

    # Query input and action buttons
    ui.input_text("query", "Ask your question (Use Reset after every question):"),
    ui.layout_columns(
        ui.input_action_button("submit", "Submit"),
        ui.input_action_button("reset", "Reset")
    ),

    ui.output_text_verbatim("response")
)

def server(input, output, session):
    response_text = reactive.Value("")
    upload_status_text = reactive.Value("")
    file_preview_text = reactive.Value("")
    file_ready = reactive.Value(False)

    @reactive.effect
    def _disable_inputs_initially():
        if not file_ready.get():
            ui.update_text("query", value="(Wait for the message 'Document Processed')")

    # Handle file upload
    @reactive.effect
    def process_upload():
        if input.upload():
            file_info = input.upload()[0]
            upload_status_text.set("📄 Document is being processed, please wait...")
            file_ready.set(False)

            try:
                create_vectorstore_from_uploaded_file(file_info["datapath"], file_info["name"])
                preview = extract_preview_from_file(file_info["datapath"], file_info["name"])
                file_preview_text.set(preview.strip())
                file_ready.set(True)
                upload_status_text.set("✅ Document processed. You can now ask questions.")
            except Exception as e:
                upload_status_text.set(f"❌ Error processing file: {str(e)}")

    @reactive.effect
    def handle_submit():
        if input.submit() and file_ready.get():
            query = input.query().strip()
            if query:
                response_text.set("")
                result = query_rag(query)
                response_text.set(result)

    @reactive.effect
    def handle_reset():
        if input.reset():
            response_text.set("")
            ui.update_text("query", value="")

    @output
    @render.text
    def upload_status():
        return upload_status_text.get()

    @output
    @render.text
    def file_preview():
        if file_ready.get():
            return f"📝 File Preview:\n{file_preview_text.get()[:1000]}..."
        return ""

    @output
    @render.text
    def response():
        return response_text.get()

app = App(app_ui, server)