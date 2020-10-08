0. Локальный запуск: docker-compose up --build

1. Регистрация: POST http://localhost:8080/register body={'username': value_1, 'password': value_2}
2. Login: POST http://localhost:8080/register body={'username': value_1, 'password': value_2} -> {'token': value}
3. Создание таски: POST http://localhost:8080/tasks/create body={'name': value_1, 'description': value_2, 'finish_time': date} -> Task
4. Изменение параметров таски (все параметры в теле необязательны): POST http://localhost:8080/tasks/change/{name} body={'name': value_1, 'description': value_2, 'finish_time': date, 'state': value_3} -> Task
5. Показать таски (все параметры в теле необязательны, фильтров может быть столько, сколько есть аттрибутов у сущности task): POST http://localhost:8080/tasks/show body={'finish_time': date, 'state': value_2} -> List(Task)
6. Показать историю таски: POST http://localhost:8080/tasks/{name} -> Task.state_history, Task.description_history, Task.name_history, Task.finish_time_history
