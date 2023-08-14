from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from django.contrib.auth.decorators import login_required
from .forms import userReg, userUpdForm
from django.views.generic import CreateView




class create_url(CreateView):
    model = URL

    fields = ['full_url']
    template_name = 'short/links_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super(create_url, self).get_context_data(**kwargs)

        ctx['slider'] = URL.objects.all()
        return ctx
def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)


def reg(request):
    if request.method == 'POST':
        form = userReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = userReg()
    data = {
        'form': form
    }
    return render(request, 'short/auth_sign-up.html', data)

@login_required()
def profile(request):
    if request.method == 'POST':
        updForm = userUpdForm(request.POST, instance=request.user)
        if updForm.is_valid():
            updForm.save()
    else:
        updForm = userUpdForm(instance=request.user)
    data = {
        'slider': URL.objects.all(),
        'updForm': updForm
    }
    return render(request, 'short/profile.html', data)





