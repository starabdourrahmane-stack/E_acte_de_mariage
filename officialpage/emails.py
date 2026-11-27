from django.core.mail import send_mail

def notifier_achat(user, acte):
    send_mail(
        subject="Nouvel achat d'acte de mariage",
        message=f"{user.username} ({user.email}) vient d'acheter l'acte {acte.numero}.",
        from_email=None,
        recipient_list=['ton.adresse@gmail.com'],
        fail_silently=True,
    )