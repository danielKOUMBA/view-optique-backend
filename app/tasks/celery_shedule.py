from celery.schedules import crontab

shedules={
    'email_every_25':{
        'task':'tasks.send_email_mensuelle',
        'shedule':crontab(day_of_month=25,hour=9,minute=30)
    }
}

# email mensuelle est le nom de la fonction qui declenche l'envoie