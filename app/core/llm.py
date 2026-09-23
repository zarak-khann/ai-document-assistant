from ollama import chat


class LLM:
    """Generate responses using a local Ollama model."""

    def __init__(self, model_name: str = "qwen2.5:3b"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        """Generate a response from the local LLM."""
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]