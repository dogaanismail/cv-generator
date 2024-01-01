import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CV_data, Interests, Education, WorkExperience, Skills
from django.template import loader
from .forms import cvDataForm
import pdfkit


def index(request):
    cv_data_form = cvDataForm()
    return render(request, "CV_gen/index.html", {
        "cv_data_form": cv_data_form
    })


def cv_list(request):
    cv_data = CV_data.objects.all()
    return render(request, "CV_gen/list.html", {
        'cv_data': cv_data
    })


def cv_download(request, num, template):
    cv_data = CV_data.objects.get(id=num)
    education = cv_data.education.all()
    work_experience = cv_data.work_experience.all()
    skills = cv_data.skills.all()
    interests = cv_data.interests.all()

    template = loader.get_template('CV_gen/cv.html')
    html = template.render({
        'cv_data': cv_data,
        'interests': interests,
        'education': education,
        'skills': skills,
        'work_experience': work_experience
    })
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    pdf = pdfkit.from_string(html, False, options)
    file_name = f"{cv_data.first_name}_{cv_data.last_name}_cv.pdf"
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response


def submit(request):
    if request.method == 'POST':
        data = json.loads(request.body).get('data')
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data['phone']
        about_yourself = data['aboutYourself']
        university = data['university']
        degree = data['degree']
        gpa = data['gpa']
        job_title = data['jobTitle']
        company_name = data['companyName']
        start_date = data['startDate']
        end_date = data['endDate']
        other_Information = data['otherInformation']
        skill = data['skills']
        interests = data['interest']
        cv_data = CV_data(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          phone=phone,
                          about_yourself=about_yourself)
        cv_data.save()

        for item in interests:
            interests_table = Interests(interest=item)
            interests_table.save()
            cv_data.interests.add(interests_table)

        for item in skill:
            skills_table = Skills(skills=item)
            skills_table.save()
            cv_data.skills.add(skills_table)

        for (item_1, item_2, item_3) in zip(university, degree, gpa):
            education_table = Education(university=item_1, degree=item_2, gpa=item_3)
            education_table.save()
            cv_data.education.add(education_table)

        for (item_1, item_2, item_3, item_4, item_5) in zip(job_title, company_name, start_date, end_date,
                                                            other_Information):
            work_experience_table = WorkExperience(job_title=item_1, company_name=item_2, start_date=item_3,
                                                   end_date=item_4, other_information=item_5)
            work_experience_table.save()
            cv_data.work_experience.add(work_experience_table)
        return JsonResponse({'status': 'sucess', 'message': 'Good Job'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
