from openai import OpenAI
from .config import OPENAI_API_KEY, MODEL

def generate_commit_message(diff_content, is_new_file=False, is_deleted_file=False):
    """Generate a commit message using OpenAI's GPT-3.5 API."""
    base_prompt = (
        "You are a helpful assistant tasked with generating accurate and concise commit messages for git repositories.\n\n"
        "Rules:\n"
        "1. Focus only on the changes provided. Do not invent or infer modifications that are not explicitly shown.\n"
        "2. If a file is newly created, indicate this clearly in the title and body of the commit message.\n"
        "3. If the modifications are additions to an otherwise empty file, note this explicitly.\n"
        "4. If a file is deleted, indicate this clearly in the title and body of the commit message.\n"
        "5. Provide a short, descriptive title summarizing the changes.\n"
        "6. For the detailed message, mention each change accurately and concisely.\n"
        "7. Title should be labeled with the prefix 'Title:' and commit message should be labeled with the prefix 'Commit Message:' exactly for your response to be parsed correctly. Never add styling to your response.\n\n"
    )

    if is_new_file:
        additional_instructions = (
            "The current file is newly created. Your commit message should reflect this, emphasizing the created file with its name and a brief summary of its content if present.\n\n"
        )
    elif is_deleted_file:
        additional_instructions = (
            "The current file has been deleted. Your commit message should reflect this, emphasizing the deleted file with its name and brief summary of its contant if present.\n\n"
        )
    else:
        additional_instructions = ""

    prompt = (
        base_prompt +
        additional_instructions +
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