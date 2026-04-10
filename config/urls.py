"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from xsign_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index-white', views.index_white, name="index-white"),
    path('index-white-01', views.index_white_01, name="index-white-01"),
    path('overview/', views.overview, name="overview"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact/', views.contact, name="contact"),

    # what we do

    path('identity-governance/', views.identity_governance, name="identity-governance"),
    path('identity-governance2/', views.identity_governance2, name="identity-governance2"),
    path('ai-digital-governance/', views.ai_digital_governance, name="ai-digital-governance"),
    path('quantum-safe-security/', views.quantum_safe_security, name="quantum-safe-security"),
    path('business-process-solutions/', views.business_process_solutions, name="business-process-solutions"),
    path('enterprise-performance/', views.enterprise_performance, name="enterprise-performance"),
    path('regulatory-risk-forensic/', views.regulatory_risk_forensic, name="regulatory-risk-forensic"),
    path('strategy/', views.strategy, name="strategy"),
    

    # Products
    
    path('posture-one/', views.posture_one, name="posture-one"),
    path('passwordless-authenticator/', views.passwordless_authenticator, name="passwordless-authenticator"),
    path('complaince-automation/', views.complaince_automation, name="complaince-automation"),

    #our thinking
    
    path('industry-thinking/', views.industry_thinking, name="industry-thinking"),
    path('xsignon-insights/', views.xsignon_insights, name="xsignon-insights"),
    path('use-cases/', views.use_cases, name="use-cases"),

    # career
    

    path('careers/', views.careers, name="careers"),

    # Legal pages

    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('terms-and-conditions/', views.terms_and_conditions, name="terms-and-conditions"),
]
