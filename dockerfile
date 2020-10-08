FROM python:3
WORKDIR /task_manager
COPY requirements.txt /task_manager/
RUN pip install -r requirements.txt
COPY . /task_manager/
# CMD ["python", "manage.py", "migrate"]

