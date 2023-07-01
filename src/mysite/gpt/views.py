from django.shortcuts import render
import openai

# Create your views here.
from django.http import HttpResponse

api_key = "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"
openai.api_key = api_key


def generate_text(request):
    data = request.POST.get("prompt")
    answer = ""
    if data is not None:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=data,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Extract the generated answer from the response
        answer = response.choices[0].text.strip()
    return render(request, './gpt.html', {'data':answer})
    # return HttpResponse("This is the specific text you want to display.")
