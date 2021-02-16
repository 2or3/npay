from django.shortcuts import render, redirect


def api_redirect(request):
    return redirect("/api")
