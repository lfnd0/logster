from dagster import job

from logster.ops.cereals import display_results, download_cereals, find_highest_calorie_cereal, find_highest_protein_cereal


@job
def say_complex_job():
    """
    A job definition. This example job has a complex op.

    For more hints on writing Dagster jobs:
    https://docs.dagster.io/tutorial/intro-tutorial/connecting-ops#a-more-complex-dag
    """
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )
