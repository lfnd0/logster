from dagster import repository
from logster.jobs.say_complex import say_complex_job
from logster.jobs.say_hello import say_hello_job
from logster.schedules.my_hourly_schedule1 import my_hourly_schedule1
from logster.schedules.my_hourly_schedule2 import my_hourly_schedule2
from logster.sensors.my_sensor import my_sensor


@repository
def logster():
    """
    The repository definition for this logster Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job, say_complex_job]
    schedules = [my_hourly_schedule1, my_hourly_schedule2]
    sensors = [my_sensor]

    return jobs + schedules + sensors
