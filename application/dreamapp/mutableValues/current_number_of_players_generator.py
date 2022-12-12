import random
from ..serializers.server_serializers import ServerDataSerializer
from .max_number_of_players import maxCount
from ..models import ServerData


def generate_number_of_players():
    servers = ServerData.objects.all()

    servers_with_count = []
    for server in servers:
        if server.name in maxCount:
            maximum = int(maxCount[server.name])
            current = random.randint(0, maximum)
        else:
            maximum = int(maxCount["Default"])
            current = random.randint(0, maximum)
        counter = {'maximum': maximum, 'current': current}
        server_data = ServerDataSerializer(server).data
        server_data.update(counter)
        servers_with_count.append(server_data)
    return servers_with_count

#
# def run_continuously(self, interval=1):
#     """Continuously run, while executing pending jobs at each elapsed
#     time interval.
#     @return cease_continuous_run: threading.Event which can be set to
#     cease continuous run.
#     Please note that it is *intended behavior that run_continuously()
#     does not run missed jobs*. For example, if you've registered a job
#     that should run every minute and you set a continuous run interval
#     of one hour then your job won't be run 60 times at each interval but
#     only once.
#     """
#
#     cease_continuous_run = threading.Event()
#
#     class ScheduleThread(threading.Thread):
#
#         @classmethod
#         def run(cls):
#             while not cease_continuous_run.is_set():
#                 self.run_pending()
#                 time.sleep(interval)
#
#     continuous_thread = ScheduleThread()
#     continuous_thread.setDaemon(True)
#     continuous_thread.start()
#     return cease_continuous_run
#
#
# Scheduler.run_continuously = run_continuously
