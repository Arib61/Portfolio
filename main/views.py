from django.shortcuts import render ,get_object_or_404,Http404 ,redirect
from .models import Project, Service, TechnicalSkill, SoftSkill, Certificate ,ProjetML, ProjetDL, ProjetDEV,Project
from .forms import ContactForm
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    services = Service.objects.all()
    tech_skills = TechnicalSkill.objects.all()
    soft_skills = SoftSkill.objects.all()
    certificates = Certificate.objects.all()
    form = ContactForm()
    context = {
        'projects': projects,
        'services': services,
        'technical_skills': tech_skills,  # Remplacer tech_skills par technical_skills ici
        'soft_skills': soft_skills,
        'certificates': certificates,
        'form': form,
    }
    return render(request, 'main/home.html', context)


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'main/portfolio.html', {'projects': projects})

def about(request):
    tech = TechnicalSkill.objects.all()
    soft = SoftSkill.objects.all()
    certif = Certificate.objects.all()
    context = {
        'tech_skills': tech,
        'soft_skills': soft,
        'certificates': certif,
    }
    return render(request, 'main/about.html', context)

def services(request): 
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def skills(request):
    technical_skills = TechnicalSkill.objects.all()
    soft_skills = SoftSkill.objects.all()
    context = {
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
    }
    return render(request, 'main/skills.html', context)


def project_detail(request, id):
    # Charger le projet principal basé sur l'ID
    projet = get_object_or_404(Project, id=id)
    
    if id == 7:
        # Récupérer tous les projets ML
        projets_ml = ProjetML.objects.all()
        template_name = 'main/project_list7.html'
        context = {
            'projetml': projets_ml,  # Passez tous les projets ML au contexte
        }
    elif id == 8:
        # Récupérer tous les projets DL
        projets_dl = ProjetDL.objects.all()
        template_name = 'main/project_list8.html'
        context = {
            'projetdl': projets_dl,  # Passez tous les projets DL au contexte
        }
    elif id == 9:
        # Récupérer tous les projets ML
        projets_dev = ProjetDEV.objects.all()
        template_name = 'main/project_list9.html'
        context = {
            'projetdev': projets_dev,  # Passez tous les projets ML au contexte
        }
    else:
        return Http404("Page not found")

    return render(request, template_name, context)



def project_list(request):
    projets_ml = ProjetML.objects.all()
    projets_dl = ProjetDL.objects.all()
    projets_dev = ProjetDEV.objects.all()

    context = {
        'projets_ml': projets_ml,
        'projets_dl': projets_dl,
        'projets_dev': projets_dev,
    }

    return render(request, 'main/project_list.html', context)



def projects(request):
    # Retrieve and pass data to template
    context = {
        'projets': Project.objects.all(),
    }
    return render(request, 'main/projects.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message!')
            return redirect('home')  
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = ContactForm()
    return redirect('home')