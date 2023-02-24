from package.packagedjintegration import models
from celery import shared_task
from package.packagedjintegration.utils import empty_contextmanager


def test_db_conn_simple() -> None:
    models.CeleryDebugObject.objects.update_or_create(
        workflow_id="123",
        state="SUCCESS",
        err="",
        tasks=[],
    )


@shared_task()  # type: ignore[misc]
def check_conn1(workflow_id: str) -> str:
    models.CeleryDebugObject.objects.update_or_create(
        data="123",
    )

    return workflow_id


def test_db_conn_in_celery1(celery_app, celery_worker) -> None:  # type: ignore[no-untyped-def]
    result = check_conn1.delay("123").get(timeout=10)
    models.CeleryDebugObject.objects.update_or_create(
        data="123",
    )
    print(f"{result=}")
    assert result == "123"


@shared_task()  # type: ignore[misc]
def check_conn2(workflow_id: str) -> str:
    with empty_contextmanager():
        models.CeleryDebugObject.objects.update_or_create(
            data="123",
        )

    return workflow_id


def test_db_conn_in_celery2(celery_app, celery_worker) -> None:  # type: ignore[no-untyped-def]
    result = check_conn2.delay("123").get(timeout=10)
    with empty_contextmanager():
        models.CeleryDebugObject.objects.update_or_create(
            data="123",
        )
    print(f"{result=}")
    assert result == "123"
