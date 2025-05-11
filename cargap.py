import os
import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # Cambia "mysite" por el nombre de tu proyecto si es distinto
django.setup()

from polls.models import Question, Choice

# Lista de preguntas y sus opciones
data = [
    {
        "question": "¿Te gusta Python?",
        "choices": ["Sí", "No", "Más o menos"]
    },
    {
        "question": "¿Usas VSCode?",
        "choices": ["Sí, siempre", "A veces", "Prefiero otro editor"]
    },
    {
        "question": "¿Conoces Django?",
        "choices": ["Sí", "No", "Lo he oído nombrar"]
    },
    {
        "question": "¿Has hecho una API REST?",
        "choices": ["Sí", "No", "Estoy aprendiendo"]
    },
    {
        "question": "¿Te interesa la inteligencia artificial?",
        "choices": ["Mucho", "Un poco", "Nada"]
    }
]

# Crear preguntas y sus opciones
for entry in data:
    q = Question.objects.create(question_text=entry["question"], pub_date=timezone.now())
    for choice_text in entry["choices"]:
        Choice.objects.create(question=q, choice_text=choice_text, votes=0)

print("Preguntas y opciones cargadas correctamente.")
