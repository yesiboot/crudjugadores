from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

from apps.crudjugadores.models import Jugador
from apps.crudjugadores.forms import JugadorForm


from django.http import HttpResponse
# Create your views here.






class JugadorCreate(CreateView):
	model = Jugador
	form_class = JugadorForm
	template_name = 'crudjugadores/jugador_form.html'
	success_url = reverse_lazy('jugadores:jugador_listar')

class JugadorList(ListView):
	queryset = Jugador.objects.order_by('id')
	template_name = 'crudjugadores/jugadores_list.html'
	paginate_by = 5


class JugadorUpdate(UpdateView):
	model = Jugador
	form_class = JugadorForm
	template_name = 'crudjugadores/jugador_form.html'
	success_url = reverse_lazy('jugadores:jugador_listar')


class JugadorDelete(DeleteView):
	model = Jugador
	form_class = JugadorForm
	template_name = 'crudjugadores/jugador_delete.html'
	success_url = reverse_lazy('jugadores:jugador_listar')


class JugadorShow(DetailView):
	model = Jugador
	template_name = 'crudjugadores/jugador_show.html'


