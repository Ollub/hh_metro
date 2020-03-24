import os
import multiprocessing

env = os.environ

bind = '0.0.0.0:8080'

workers = multiprocessing.cpu_count() * 2 + 1

threads = int(env.get('THREADS', 10))

accesslog = '-'
access_logformat = '%t [%s] %a "%r" "%{User-Agent}i" [%b bytes %Tf s]'
timeout = int(env.get('TIMEOUT', 60))
