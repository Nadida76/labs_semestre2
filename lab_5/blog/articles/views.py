from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Article
from django.shortcuts import render
from django.http import Http404

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title':
                    request.POST["title"]
            }
        # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
            # если поля заполнены без ошибок
                # проверка на уникальность названия статьи
                try:
                    Article.objects.create(text=form["text"],
                                   title=form["title"], author=request.user)
                except:
                    form['errors'] = u"Статья с подобным названием уже существует"
                    return render(request, 'create_post.html',
                          {'form': form})
                p = str(Article.objects.get(text=form["text"])) # тут получается что то вроде Article objects (31)


                res = ''.join(filter(lambda i: i.isdigit(), p)) # извлекаю номер 31

                return redirect('get_article',
                            article_id=res)

            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html',
                          {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

