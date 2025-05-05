import datetime
import pendulum # datetime을 쉽게 쓰기 위한 라이브러리

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # ui 상에 표시되는 dag 이름
    schedule="0 0 * * *", # 분, 시, 일, 월, 요일 (cron schedule)
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 
    catchup=False, # 누락된 기간에 대해 한번에 실행할지 여부
    # dagrun_timeout=datetime.timedelta(minutes=60), # 실행 시간 제한
    # tags=["example", "example2"], # 태그, 조회할 때 필터를 걸어서 조회 가능
    params={"example_key": "example_value"}, # task들에 공통적으로 전달할 파라미터
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # ui 상에 표시되는 task 이름
        bash_command="echo hello",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2", # ui 상에 표시되는 task 이름
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
