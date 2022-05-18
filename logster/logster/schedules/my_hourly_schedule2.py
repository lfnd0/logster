from dagster import schedule
from logster.jobs.say_complex import say_complex_job


@schedule(cron_schedule="0 3 * * 1-5", job=say_complex_job, execution_timezone="America/Sao_Paulo")
def my_hourly_schedule2(_context):
    """
    cron_schedule:
    At 03:00 on every day-of-week from Monday through Friday.
    """
    run_config = {}
    return run_config
