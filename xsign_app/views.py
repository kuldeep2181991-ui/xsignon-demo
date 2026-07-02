from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def index_white(request):
    return render(request,"index-white.html")

def index_white_01(request):
    return render(request,"index-white-01.html")

def overview(request):
    return render(request,"overview.html")

def about_us(request):
    return render(request,"about-us.html")

def contact(request):
    return render(request,"contact.html")

# what we do

def identity_governance(request):
    return render(request,"identity-governance.html")

#def identity_governance2(request):
    #return render(request,"identity-governance2.html")

def ai_digital_governance(request):
    return render(request,"ai-digital-governance.html")

def quantum_safe_security(request):
    return render(request,"quantum-safe-security.html")

def business_process_solutions(request):
    return render(request,"business-process-solutions.html")

def enterprise_performance(request):
    return render(request,"enterprise-technology-solutions.html")

def regulatory_risk_forensic(request):
    return render(request,"regulatory-risk-forensic.html")

def strategy(request):
    return render(request,"strategy.html")

# products

def posture_one(request):
    return render(request,"posture-one.html")

def passwordless_authenticator(request):
    return render(request,"passwordless-authenticators.html")

def complaince_automation(request):
    return render(request,"complaince-automation.html")

def industry_thinking(request):
    return render(request,"industry-thinking.html")

def xsignon_insights(request):
    return render(request,"xsignon-insights.html")

def use_cases(request):
    return render(request,"use-cases.html")

# careers

def careers(request):
    return render(request,"careers.html")

# legal pages

def privacy_policy(request):
    return render(request,"privacy-policy.html")

def terms_and_conditions(request):
    return render(request,"terms-and-conditions.html")

def unsubscribe(request):
    return render(request, "unsubscribe.html")

def news_details(request):
    return render(request, "news-details.html")

def news_details1(request):
    return render(request, "news-details1.html")

def news_details2(request):
    return render(request, "news-details2.html")

def news_details3(request):
    return render(request, "news-details3.html")

def news_details4(request):
    return render(request, "news-details4.html")