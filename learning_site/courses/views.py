from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from courses.models import Course, Step  # or .models import Course
import datetime

# Create your views here.


def course_list(request):
    courses = Course.objects.all()
#  Without template
#    output = ', '.join([str(course) for course in courses])
#    return HttpResponse(output)
#  With template                                       # This is the context (Parameters)
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    #   course = Course.objects.get(pk=pk)
    #   Get 404 ERROR
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    # course_id refer to the foreign key on the Step
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
