import gradio as gr, json

def chatbot(frage, code):
    try:
        with open(f"kunden/{code}.json", "r") as f:
            daten = json.load(f)
        for k, v in daten["antworten"].items():
            if k.lower() in frage.lower():
                return v
        return daten.get("fallback", "Bitte kontaktieren Sie unseren Support.")
    except:
        return "Ungültiger Kundencode."

gr.Interface(
    fn=chatbot,
    inputs=[gr.Text(label="Frage"), gr.Text(label="Kundencode")],
    outputs="text",
    title="Kunden-Support-Chatbot"
).launch()
