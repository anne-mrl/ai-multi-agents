import openai
from strategies.base_strategy import ResolutionStrategy


class GPTResolution(ResolutionStrategy):
    """Strategy to resolve question using GPT-4o."""

    def resolve(self, question: str) -> str:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": question}]
            )
            return f"AGENT GPT-4o RESPONSE:\n\n" \
                   f"{response.choices[0].message.content}"
        except openai.OpenAIError as e:
            return f"Error with OpenAI API: {str(e)}"
