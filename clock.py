from apscheduler.schedulers.blocking import BlockingScheduler

from attendance import mail_attendance


sched = BlockingScheduler()

# Schedule mail_attendance to be called every day
sched.add_job(mail_attendance, 'interval', days=1)

sched.start()