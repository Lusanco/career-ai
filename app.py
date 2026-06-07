import os
import gradio as gr
from typing import cast
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from guardrails import validate_input, check_rate_limit, apply_preamble


def env_to_str(env: str) -> str:
    return cast(str, os.getenv(env))


HEADER_HTML = """
<div style="text-align: center; padding: 2rem 1rem 0.5rem 1rem;">
    <h1 style="margin: 0; font-size: 1.8rem;">Luis Santiago</h1>
    <p style="margin: 0.25rem 0 0 0; color: #64748b;">
        Software Developer &middot; Career Agent AI
    </p>
    <hr style="margin: 1rem auto; width: 60px; border: 1px solid #e2e8f0;">
</div>
"""

FOOTER_HTML = """
<div style="text-align: center; padding: 0.5rem 1rem 1.5rem 1rem; font-size: 0.85rem; color: #94a3b8;">
    <a href="https://linkedin.com/in/lusanco" target="_blank">LinkedIn</a>
    &nbsp;&middot;&nbsp;
    <a href="https://github.com/Lusanco" target="_blank">GitHub</a>
    &nbsp;&middot;&nbsp;
    <a href="mailto:lasc1026@gmail.com">Email</a>
</div>
"""

CUSTOM_CSS = """
#component-0, .gradio-container { max-width: 100% !important; }
footer { display: none !important; }
"""


def main():
    load_dotenv(override=True)

    gemini_api_key = env_to_str("GEMINI_API_KEY")
    gemini_base_url = env_to_str("GEMINI_BASE_URL")
    model_gemini_flash = env_to_str("MODEL_GEMINI_FLASH")

    gemini = OpenAI(api_key=gemini_api_key, base_url=gemini_base_url)

    try:
        with open("./career-data/master_prompt.md", "r", encoding="utf-8") as file:
            master_prompt = file.read()
        with open("./career-data/refined_resume.md", "r", encoding="utf-8") as file:
            refined_resume = file.read()
        with open("./career-data/linkedin.md", "r", encoding="utf-8") as file:
            linkedin = file.read()
        with open(
            "./career-data/refined_simulated_interview.md", "r", encoding="utf-8"
        ) as file:
            refined_simulated_interview = file.read()

        system_prompt = f"""
Master Prompt:
{master_prompt}

Refined Resume:
{refined_resume}

LinkedIn Details:
{linkedin}

Refined Simulated Interview:
{refined_simulated_interview}
"""
        system_prompt = apply_preamble(system_prompt)

    except FileNotFoundError:
        print("File Not Found. Using default system prompt.")
        system_prompt = apply_preamble(
            "You are a helpful AI assistant. Since your personal context "
            "is not available, please inform the user and refrain from answering."
        )

    def chat(message, history):
        error = validate_input(message)
        if error:
            return error

        key = str(hash(str(history)))
        rate_error = check_rate_limit(key)
        if rate_error:
            return rate_error

        messages = (
            [{"role": "system", "content": system_prompt}]
            + history
            + [{"role": "user", "content": message}]
        )

        try:
            response = gemini.chat.completions.create(
                model=model_gemini_flash, messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"API Error: {e}")
            return (
                "I'm having trouble connecting right now. "
                "Please try again in a moment."
            )

    custom_theme = gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate",
        neutral_hue="gray",
        font=gr.themes.GoogleFont("Inter"),
    )

    with gr.Blocks(
        theme=custom_theme, title="Luis Santiago \u2014 Career AI", css=CUSTOM_CSS
    ) as demo:
        gr.HTML(HEADER_HTML)
        chatbot = gr.ChatInterface(chat, type="messages")
        gr.HTML(FOOTER_HTML)

    demo.launch()


if __name__ == "__main__":
    main()
