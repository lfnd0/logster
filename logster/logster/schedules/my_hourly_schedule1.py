from dagster import schedule

from logster.jobs.say_hello import say_hello_job


@schedule(cron_schedule="*/5 * * * *", job=say_hello_job, execution_timezone="America/Sao_Paulo")
def my_hourly_schedule1(_context):
    """
    A schedule definition. This example schedule runs once each hour.

    For more hints on running jobs with schedules in Dagster, see our documentation overview on
    schedules:
    https://docs.dagster.io/overview/schedules-sensors/schedules

    For cron schedule:
    https://crontab.guru/

    cron_schedule:
    At every 5th minute.
    """
    run_config = {}
    return run_config
