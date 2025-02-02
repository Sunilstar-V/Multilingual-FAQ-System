# D:\last_war\myproject\blog\views.py

from django.http import JsonResponse
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all().values('question', 'answer')
    return JsonResponse(list(faqs), safe=False)

from django.views import View

class FAQListView(View):
    def get(self, request):
        faqs = FAQ.objects.all().values('question', 'answer')
        return JsonResponse(list(faqs), safe=False)

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Welcome to My Blog</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
                h1 { color: #2c3e50; }
                p { margin: 10px 0; }
                .container { max-width: 800px; margin: auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to My Blog!</h1>
                <p>I am Sunil, a B-Tech graduate excelling in academics as well as in sports such as Cricket and many others.</p>
                <p>My journey in technology began with a deep-seated desire to create meaningful solutions. From developing VoxAI, an AI-driven voice assistant for individuals with disabilities, to my recent recognition as one of the top 30 finalists in the Solve for Tomorrow India 2023 by Samsung, I have honed my skills in Python, Java, UX design, and Azure services.</p>
                <p>Additionally, I am thrilled to share that I have been selected as a delegate for the HPAIR 2024 conference at Bangkok, Thailand, further validating my commitment to innovation and leadership in technology. We are also selected for the finale for COMEUP STARS 2024 Korea. I was recently awarded at the India AI Impact Festival 2024.</p>
                <p>These experiences have equipped me with a strong foundation in software development, coupled with a keen eye for user-centric design and innovation.</p>
                <p>My academic pursuits in B-Tech from Vidya Jyothi Institute of Technology, Hyderabad, alongside certifications such as the Google UX Design Professional Certificate, Salesforce Superset virtual internship, and Microsoft Azure AI Vision Solutions Certification have further solidified my technical expertise and commitment to continuous learning.</p>
                <p>In addition to my technical skills, I bring a proactive mindset, strong problem-solving abilities, and a collaborative spirit to the table. I thrive in dynamic environments and am eager to contribute to projects that push the boundaries of innovation and drive positive change.</p>
                <p>I am particularly drawn to the company's reputation for innovation and commitment to pushing the boundaries of technology. I am confident that my background, skills, and passion align seamlessly with the goals of your organization, and I am eager to make a meaningful impact as a member of your team.</p>
            </div>
        </body>
    </html>
    """)
    
    