from django.views import generic
from dal import autocomplete
from .models import School, House, Student


class SchoolView(generic.ListView):
    template_name = 'StudentApp/school.html'
    model = School


class HouseView(generic.DetailView):
    template_name = 'StudentApp/house.html'
    model = School


class StudentView(generic.DetailView):
    template_name = 'StudentApp/student.html'
    model = School

    def get_context_data(self, **kwargs):
        """
        gets the students in the house in the school
        :param kwargs: not used
        :return: students in the house
        """
        context = super(StudentView, self).get_context_data(**kwargs)
        # get the school
        school = self.get_object(self.get_queryset())
        # get the house slug from the url
        house_slug = self.kwargs.get('house_slug')
        house = House.objects.get(slug=house_slug, school=school)
        # get students from the house
        students = house.students.all()
        # add the students to the context
        context['students'] = students
        return context


class StudentAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if self.q:
            return Student.objects.filter(last_name__istartswith=self.q)
        else:
            return Student.objects.all()

    def get_result_label(self, student):
        return '%s, %s (%s)' % (student.last_name, student.first_name, student.house)
