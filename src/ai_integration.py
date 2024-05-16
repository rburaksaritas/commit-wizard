from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

def generate_commit_message(api_key, diff_content):
    """Generate a commit message using OpenAI's GPT-3.5 API."""
    prompt = (
        "Provide a short title for the commit.\n\n"
        "Based on the following changes, provide a commit message under the title that explains the changes. If multiple places are changed, mention each.\n\n"
        "Changed Lines:\n\n"
        f"{diff_content}\n\n"
        "Commit Message:\n\n"
    )
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

def parse_commit_message(response):
    """Parse the commit message response from GPT-3."""
    lines = response.split('\n')
    title = ""
    message = ""
    capture_title = False
    capture_message = False

    for line in lines:
        if line.startswith("Title:"):
            capture_title = True
            capture_message = False
            title += line[len("Title:"):].strip()
        elif line.startswith("Commit Message:"):
            capture_title = False
            capture_message = True
            if message:
                message += "\n"
            message += line[len("Commit Message:"):].strip()
        else:
            if capture_title:
                title += " " + line.strip()
            elif capture_message:
                if message:
                    message += "\n"
                message += line.strip()

    return title.strip(), message.strip()