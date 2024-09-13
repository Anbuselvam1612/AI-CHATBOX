from django.shortcuts import render
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Initialize the tokenizer and model
tokenizer = BlenderbotTokenizer.from_pretrained('facebook/blenderbot-400M-distill')
model = BlenderbotForConditionalGeneration.from_pretrained('facebook/blenderbot-400M-distill')

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Tokenize and generate a response
        inputs = tokenizer(user_input, return_tensors='pt')
        reply_ids = model.generate(inputs['input_ids'])
        response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
        return render(request, 'chatbot/home.html', {'user_input': user_input, 'response': response})
    return render(request, 'chatbot/home.html')
