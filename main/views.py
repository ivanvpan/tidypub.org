from tidypub.main.models import Post
from tidypub.tp_markdown.tp_markdown import tp_markdown
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings

def index(request):
    if request.POST.has_key('text'):
        text = request.POST['text']
        title = request.POST.get('title', None)
        blank_field = request.POST['some_in']

        # validate this stuff. crudely
        if len(text.strip()) < 1 \
            or len(text) > 32767 \
            or len(blank_field) > 0:
            return redirect('/')
        elif title and len(title) > Post.TITLE_LENGTH:
            return redirect('/')

        #text = text.replace('![', '[') # no images
        #text = markdown(text, safe_mode='escape')
        p = Post(title=title, text=text)
        p.save()
        return redirect('/' + p.id)

    return render_to_response('index.html',
            {'sample_id': settings.SAMPLE_POST_ID},
            context_instance=RequestContext(request))


def view(request, id):
    new_post = False
    post = get_object_or_404(Post, id=id)
    
    if (post.new):
        post.new = False
        new_post = True
        post.save()
    title = post.title
    text = tp_markdown(post.text)
    return render_to_response('view.html',
                              dict(id=post.id, new_post=new_post, title=title, text=text))


def moving(request):
    return render_to_response('moving.html')

def terms(request):
    title = 'Terms of Service'
    return render_to_response('terms.html', dict(title=title))

def contact(request):
    title = 'Contact'
    text = '''Send email to ivan $at$ tidypub org.<br><br>@tidypub on twitter.'''
    return render_to_response('contact.html', dict(title=title))

def robots(request):
    text = 'User-agent: *\nDisallow: '
    return HttpResponse(text, mimetype='text/plain')

def donate(request):
    title = 'Donate'
    return render_to_response('donate.html', dict(title=title))
