from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def generate_study_plan(hours):
    prompt = f"""
    Você é um mentor especialista em ENEM.

    O aluno possui {hours} horas para estudar hoje.

    Gere um plano de estudos com:

    - Distribuição das horas
    - Conteúdos
    - Pequeno resumo
    - Exercícios sugeridos
    - Links para aprofundamento

    Retorne em markdown.
    """

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content