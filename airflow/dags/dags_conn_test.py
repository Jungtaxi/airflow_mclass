import datetime
import pendulum # datetime을 쉽게 쓰기 위한 라이브러리

from airflow import DAG
from airflow.operators.empty import EmptyOperator # task id만을 인수로 받는 빈 연산자

with DAG(
    dag_id="dags_conn_test", # ui 상에 표시되는 dag 이름
    schedule=None, # 분, 시, 일, 월, 요일 (cron schedule)
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 
    catchup=False, # 누락된 기간에 대해 한번에 실행할지 여부
    # dagrun_timeout=datetime.timedelta(minutes=60), # 실행 시간 제한
    # tags=["example", "example2"], # 태그, 조회할 때 필터를 걸어서 조회 가능
    # params={"example_key": "example_value"}, # task들에 공통적으로 전달할 파라미터
) as dag:
    t1 = EmptyOperator(
        task_id="t1",
    )
    t2 = EmptyOperator(
        task_id="t2",
    )
    t3 = EmptyOperator(
        task_id="t3",
    )
    t4 = EmptyOperator(
        task_id="t4",
    )
    t5 = EmptyOperator(
        task_id="t5",
    )
    t6 = EmptyOperator(
        task_id="t6",
    )
    t7 = EmptyOperator(
        task_id="t7",
    )   
    t8 = EmptyOperator(
        task_id="t8",
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
