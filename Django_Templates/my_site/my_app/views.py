from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var = {'first_name':'Satish', 'last_name':'Leo',
    'some_list':[1,2,3], 'some_dict':{'inside_dict':'inside_value'}, 'user_logged_in':True
    }
    return render(request,'my_app/variable.html',context=my_var)