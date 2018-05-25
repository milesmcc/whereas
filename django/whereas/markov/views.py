# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import model, corpus

# Create your views here.
def index(request):
    return render(request, 'markov/index.html')

def apologize(request):
    builtmodel = model.build_model(corpus.sentences)
    sentence = model.compose(model.generate_sentence(builtmodel, "whereas"))
    return render(request, "markov/apologize.html", context={"sentence": sentence})
