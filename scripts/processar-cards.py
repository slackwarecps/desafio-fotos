#!/usr/bin/env python3
import anthropic
import base64
import json
import os
import glob
from pathlib import Path

def encode_image(image_path):
    """Encode image to base64"""
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")

def extract_question_from_image(client, image_path):
    """Extract question and options from image using Claude Vision"""
    image_data = encode_image(image_path)

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Extract the multiple-choice question from this image.
                        Return a JSON object with:
                        {
                            "question": "the question text",
                            "options": {
                                "A": "option A text",
                                "B": "option B text",
                                "C": "option C text",
                                "D": "option D text"
                            }
                        }

                        Return ONLY the JSON, no markdown or extra text."""
                    }
                ],
            }
        ],
    )

    # Parse JSON response
    try:
        result = json.loads(response.content[0].text)
        return result
    except json.JSONDecodeError:
        print(f"Failed to parse JSON for {image_path}")
        return None

def determine_correct_answer(client, question, options):
    """Use Claude to determine the correct answer based on technical merit"""
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"""You are an expert in software architecture and Claude AI certifications.

Question: {question}

Options:
A) {options['A']}
B) {options['B']}
C) {options['C']}
D) {options['D']}

Based on technical merit and best practices, which answer is correct?
Respond with ONLY the letter (A, B, C, or D) - nothing else."""
            }
        ],
    )

    answer = response.content[0].text.strip()
    return answer[0] if answer else "A"

def generate_enriched_card(client, idx, question, options, correct_answer):
    """Generate an enriched card with translations and explanations"""
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"""You are a certification exam instructor specializing in Claude AI architecture patterns.

Generate a complete enriched flashcard for this question:

Question: {question}

Options:
A) {options['A']}
B) {options['B']}
C) {options['C']}
D) {options['D']}

Correct Answer: {correct_answer}

Format your response as markdown with these sections:

### TRANSLATED QUESTION
[Portuguese translation of the question]

### TRANSLATED OPTIONS
- A) [Portuguese translation]
- B) [Portuguese translation]
- C) [Portuguese translation]
- D) [Portuguese translation]

### EXPLANATION (Tech Lead)
[Deep technical explanation for experienced developers covering:
- What architectural pattern/concept is being tested
- Why the correct answer is best (detailed analysis)
- Why each wrong option fails (specific technical reasons)
- Pattern insights and connections to broader topics]

### CHILDREN EXPLANATION (Simple)
[Accessible explanation for beginners covering:
- The concept in plain language
- Why the correct answer works (simple terms)
- Why other options don't work
- Key takeaway to remember]

### CORRECT ANSWER
{correct_answer}"""
            }
        ],
    )

    return response.content[0].text

def create_simple_card(question, options):
    """Create a simple card with just the question and options"""
    card = f"""{question}
---
[ ] A - {options['A']}
[ ] B - {options['B']}
[ ] C - {options['C']}
[ ] D - {options['D']}"""
    return card

def main():
    # Initialize Anthropic client (uses ANTHROPIC_API_KEY env var by default)
    client = anthropic.Anthropic()

    # Get all foto images
    images = sorted(glob.glob("foto-*.png"))

    print(f"📸 Processando {len(images)} fotos...\n")

    for idx, image_path in enumerate(images, 1):
        photo_num = f"{idx:03d}"
        print(f"Processing {image_path}...")

        # Extract question from image
        extracted = extract_question_from_image(client, image_path)
        if not extracted:
            print(f"  ❌ Failed to extract from {image_path}")
            continue

        question = extracted.get("question")
        options = extracted.get("options", {})

        # Determine correct answer
        correct_answer = determine_correct_answer(client, question, options)

        # Create simple card
        simple_card = create_simple_card(question, options)
        simple_file = f"{photo_num}-card.md"
        with open(simple_file, "w") as f:
            f.write(simple_card)
        print(f"  ✅ {simple_file}")

        # Generate enriched card
        enriched_content = generate_enriched_card(client, idx, question, options, correct_answer)
        enriched_file = f"{photo_num}-enriched-card.md"
        with open(enriched_file, "w") as f:
            f.write(enriched_content)
        print(f"  ✅ {enriched_file}")

    print(f"\n✨ Completed! Generated {len(images)} pairs of cards.")

if __name__ == "__main__":
    main()
