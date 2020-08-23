from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from JobFun import seven_point,eleven_point,seventeen_point,twentyone_point
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(seven_point, 'cron',  hour=7, minute=9)
scheduler.add_job(eleven_point, 'cron',  hour=11, minute=10)
scheduler.add_job(seventeen_point, 'cron',  hour=17, minute=12)
scheduler.add_job(twentyone_point, 'cron',  hour=21, minute=10)
#scheduler.add_job(seven_point, 'cron',  hour=0, minute=39)
scheduler.start()