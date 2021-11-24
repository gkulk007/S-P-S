from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'profiles':profiles})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        summary = request.POST['summary']
        education = request.POST['education']
        skills = request.POST['skills']
        instagram = request.POST['instagram']
        twitter = request.POST['twitter']
        facebook = request.POST['facebook']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        website = request.POST['website']

        update_profile = Profile.objects.get(user=request.user)
        update_profile.username=username
        update_profile.name=name
        update_profile.email=email
        update_profile.phone_no=phone
        update_profile.summary=summary 
        update_profile.education=education 
        update_profile.skills=skills
        update_profile.instagram=instagram
        update_profile.facebook=facebook
        update_profile.twitter=twitter
        update_profile.linkedin=linkedin
        update_profile.github=github 
        update_profile.website=website
        update_profile.save()

        # write a function for updating the profile
        # update_profile = Profile.objects.get(user=request.user)

    # get post data from textarea and save it to the database



        return render(request, 'profile/edit.html',{'profile':update_profile})

    return render(request, 'profile/edit.html',{'profile':profile})
