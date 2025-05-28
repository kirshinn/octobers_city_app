from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm
from .models import Feedback


@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.user.is_authenticated:
                feedback.user = request.user
            feedback.save()

            # Отправка email
            subject = f"New Feedback: {feedback.subject}"
            message = f"From: {feedback.user if feedback.user else 'Anonymous'}\n\nMessage:\n{feedback.message}"
            # send_mail(
            #     subject=subject,
            #     message=message,
            #     from_email=settings.DEFAULT_FROM_EMAIL,
            #     recipient_list=settings.DEFAULT_TO_EMAILS,
            #     fail_silently=False,
            # )
            messages.success(request, 'Your feedback has been sent successfully!')
            return redirect('home')
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})
