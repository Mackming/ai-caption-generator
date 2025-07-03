import base64
import io
import csv
import json

def generate_downloads(captions, meta_data):
    formatted_captions = "\n\n".join(captions)
    b64_txt = base64.b64encode(formatted_captions.encode()).decode()

    output_csv = io.StringIO()
    writer = csv.writer(output_csv)
    writer.writerow(["Platform", "Tone", "Persona", "Caption"])
    for caption in captions:
        writer.writerow([meta_data["platform"], meta_data["tone"], meta_data["persona"], caption])
    b64_csv = base64.b64encode(output_csv.getvalue().encode()).decode()

    json_data = [
        {
            "platform": meta_data["platform"],
            "tone": meta_data["tone"],
            "persona": meta_data["persona"],
            "caption": c
        } for c in captions
    ]
    b64_json = base64.b64encode(json.dumps(json_data, indent=2).encode()).decode()

    return formatted_captions, output_csv.getvalue(), json.dumps(json_data, indent=2)