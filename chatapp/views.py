# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

def chat(request):
    return render(request, 'chat.html')

def get_bot_response(request):
    # Configure the GenerativeAI API key
    api_key = "Your-Api-Key"
    genai.configure(api_key=api_key)

    try:
        # Set up the model
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        # Start the conversation
        chat = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)

        # Input prompt from user
        prompt = request.GET.get('user_message')

        # Generate response from the model
        response = chat.generate_content(prompt)
        
        # Extract text content from the response
        bot_response = response.text

        return JsonResponse({'bot_response': bot_response})
    except Exception as e:
        # Log the error
        print(f"Error occurred: {e}")
        return JsonResponse({'error': 'An error occurred while processing the request'}, status=500)
