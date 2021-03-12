from django.shortcuts import render

from .models import Job, Subscriber, Subscription

from .signals import new_subscriber


def get_jobs(request):
    # get all jobs from the DB
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'job.html', {'job': job})


def subscribe(request, id):
    job = Job.objects.get(pk=id)
    sub = Subscriber(email=request.POST['email'])
    sub.save()

    subscription = Subscription(user=sub, job=job, email=sub.email)
    subscription.save()

    new_subscriber.send(sender=subscription.__class__, job=job, subscriber=sub)

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'subscribed.html', {'payload': payload})
