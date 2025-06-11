import schedule
import time
from plyer import notification

def job():
    notification.notify(
        title="do!",
        message="wake up stretching",
        timeout=10
    )

schedule.every().hour.do(job)

if __name__ == "__main__":
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
