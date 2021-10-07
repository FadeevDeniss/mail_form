from django.http import HttpResponseRedirect, HttpResponse
from mail.forms import Credentials
from mail.models import Mail
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.template import loader


def feedback(request):
    if request.method == 'POST':
        form = Credentials(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg_text = form.cleaned_data['message_text']
            Mail.objects.create(
                name=name,
                email=email,
                message_text=msg_text
            ).save()
            return HttpResponseRedirect('/Thanks/')
        else:
            raise ValidationError([
                ValidationError(_('You must enter the value'), code='err_01')
            ])

    else:
        form = Credentials()
        return render(request, 'Credentials.html', {'form': form})


def thanks(request):
    mail_list = Mail.objects.order_by('-id')[:1]
    context = {'mail_list': mail_list}  
    return render(request, 'Thanks.html', context)


def index(request):
    latest_mail_list = Mail.objects.order_by('id')[:10]
    context = {'latest_mail_list': latest_mail_list}
    return render(request, 'Index.html', context)


def get_mail(request, mail_id):
    summary = "Summary of mail with ID %s."
    return HttpResponse(summary % mail_id, 'Summary.html')


