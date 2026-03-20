from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def overview(request):
    return render(request,"overview.html")

def about_us(request):
    return render(request,"about-us.html")

def contact(request):
    return render(request,"contact.html")

# what we do

def identity_governance(request):
    return render(request,"identity-governance.html")

def identity_governance2(request):
    return render(request,"identity-governance2.html")

def ai_digital_governance(request):
    return render(request,"ai-digital-governance.html")

def quantum_safe_security(request):
    return render(request,"quantum-safe-security.html")

def business_process_solutions(request):
    return render(request,"business-process-solutions.html")

def enterprise_performance(request):
    return render(request,"enterprise-performance.html")

def regulatory_risk_forensic(request):
    return render(request,"regulatory-risk-forensic.html")

def strategy(request):
    return render(request,"strategy.html")

# products

def posture_one(request):
    return render(request,"posture-one.html")

def passwordless_authenticator(request):
    return render(request,"passwordless-authenticator.html")

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