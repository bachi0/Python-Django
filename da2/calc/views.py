from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Kiran'})


def multiply(request):
    n = int(request.POST["n"])
    one = request.POST["maxone"]
    two = request.POST["maxtwo"]
    a = [list(map(int, x.split("@"))) for x in one.split("#")]
    b = [list(map(int, x.split("@"))) for x in two.split("#")]
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += int(a[i][k]) * int(b[k][j])
    return render(request, 'result.html', {'one': a, 'two': b, 'result': result})