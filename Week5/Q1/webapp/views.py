from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text_area = None
    get_dict = {}
    if request.method == 'POST':
        try:
            get_dict['text_area_details'] = ""
            params = ['Name', 'Dob', 'Address', 'ContactNumber', 'Email', 'Eng_Score', 'Phy_Score', 'Chem_Score']
            for param in params:
                get_dict[param] = request.POST.get(param)
                get_dict['text_area_details'] += f'Student\'s {param}: {get_dict[param]}\n'
            get_dict['avg_marks'] = sum(list(map(float, [get_dict['Eng_Score'], get_dict['Phy_Score'], get_dict['Chem_Score']]))) / 3.0
        except (ValueError, TypeError):
            pass
    return render(request, "form.html", get_dict)