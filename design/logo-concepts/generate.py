import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

BRAND = (
    "Brand palette: deep dusk blue #1F3A52, warm bronze #8C6A3F, gold #B8924D, "
    "sand cream #E8DCC0, dark ink brown #3B2F1E. Tone: serious, reverent, "
    "classic/timeless Reformed theology ministry resource for adults -- NOT "
    "cartoonish, NOT a children's Bible-story illustration, no cute faces. "
    "Clean vector-flat emblem/crest illustration style, bold confident "
    "linework, suitable as a small website favicon AND a larger header logo. "
    "Plain solid white background, logo centered, no extra text or borders "
    "beyond the design itself."
)

prompts = {
    "shield_sling_1": (
        "A heraldic shield emblem logo for a Christian ministry called "
        "'David Slays Goliath'. Inside the shield: a simple, elegant "
        "leather sling with a single round stone mid-flight, rendered in "
        "gold/bronze on a dusk-blue shield background, thin gold border "
        "outline. No text in this version. " + BRAND
    ),
    "shield_sling_2": (
        "A minimalist heraldic shield crest logo: five smooth stones "
        "stacked in a small pyramid at the base, with a sling strap "
        "looping above them, all in bronze and gold line-art on a deep "
        "dusk-blue shield. Subtle, dignified, not literal/illustrative -- "
        "more like a coat-of-arms symbol. No text. " + BRAND
    ),
    "monogram_dsg": (
        "A minimal modern monogram logo combining the letters 'D' and 'G' "
        "into one interlocked geometric mark (representing 'David' and "
        "'Goliath'), bronze/gold gradient on dusk blue, inside a thin "
        "circular or shield-shaped outline. Clean, abstract, timeless -- "
        "think a serious theological publisher's mark, not playful. "
        "No other text. " + BRAND
    ),
    "monogram_d_stone": (
        "A minimal monogram logo: a bold serif letter 'D' with a single "
        "small round stone integrated into the negative space or as a "
        "subtle accent, in dusk blue and gold. Extremely simple, works "
        "as a tiny favicon. No other text. " + BRAND
    ),
    "crest_full_name_1": (
        "A shield crest emblem logo with the full ministry name 'DAVID "
        "SLAYS GOLIATH' arched in small bold serif capital letters above "
        "the shield, and the shield containing a simple sling-and-stone "
        "symbol in bronze and gold on dusk blue. Balanced, legible at "
        "header size, classic theological-ministry branding feel. " + BRAND
    ),
    "crest_full_name_2": (
        "A circular emblem/seal logo: the words 'DAVID SLAYS GOLIATH' "
        "curving around the top inside a thin gold ring border, a small "
        "shield with a sling and stone centered below the text, dusk "
        "blue and gold/bronze color scheme, like a classic seminary or "
        "publishing house seal. " + BRAND
    ),
}

for name, prompt in prompts.items():
    print(f"Generating {name}...")
    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(aspect_ratio="1:1", image_size="2K"),
        ),
    )
    saved = False
    for part in response.parts:
        if part.text:
            print("  note:", part.text[:200])
        elif part.inline_data:
            img = part.as_image()
            out_path = os.path.join(os.path.dirname(__file__), f"{name}.jpg")
            img.save(out_path)
            print("  saved", out_path)
            saved = True
    if not saved:
        print("  WARNING: no image returned for", name)
