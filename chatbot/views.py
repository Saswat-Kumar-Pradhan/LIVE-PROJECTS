from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import google.generativeai as genai
import markdown2
import re

genai.configure(api_key="AIzaSyAXRbUrO4mVxs5QdNk5VCaHBqJICzKbucU")

model = genai.GenerativeModel('gemini-1.5-flash')

custom_responses = [
    (re.compile(r'hi|hii|hello|hey', re.IGNORECASE), 'Hello! Welcome to Saswat\'s Generative AI. How can I assist you today?'),
    (re.compile(r'help', re.IGNORECASE), 'Sure, I am here to help! What do you need assistance with?'),
    (re.compile(r'bye|goodbye', re.IGNORECASE), 'Goodbye! Have a great day! Always feel free to ask anything to Saswat\'s Gen AI when you want to know something.'),
    
]

def chatWithAi(request):
    if 'entries' not in request.session:
        request.session['entries'] = []

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input:
            messages = []
            for entry in request.session['entries'][-5:]:
                messages.append({'role': 'user', 'parts': [entry['input']]})
                messages.append({'role': 'model', 'parts': [entry['output']]})
            messages.append({'role': 'user', 'parts': [user_input]})
            
            response_text = None
            for pattern, response in custom_responses:
                if pattern.search(user_input):
                    response_text = response
                    break
            
            if response_text is None:
                response = model.generate_content(messages)
                response_text = response.text
            
            processed_output = markdown2.markdown(response_text)
            request.session['entries'].append({
                'input': user_input,
                'output': processed_output
            })
            request.session.modified = True
        
        return HttpResponseRedirect(reverse('chatWithAi'))
    
    entries = request.session.get('entries', [])[::-1]
    return render(request, 'chatbot.html', {'entries': entries})

def delete(request):
    if 'entries' in request.session:
        del request.session['entries']
    return redirect('chatWithAi')