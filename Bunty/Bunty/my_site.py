from django.http import HttpResponse

from django.shortcuts import render
def funcy(request):
    return HttpResponse("Hi Bunty, </n> <b>How are you</b>")



def funcy2(request):
    return render(request, "ht1.html")


def count_words(request):
    return render (request, "count_words.html")

def result(request):
    message = request.GET["message"]
    words = message.split()
    word_count= {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    return render(request, "result.html", {'message':message, 'count':len(words), 'word_count':word_count})
