<h1>Тестовое задание №1 Bewise.ai</h1>
  <h2>Задание</h2>
  <p>С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.</p>
  <h2>Реализовать на Python3 веб-сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:</h2>
  <ol>
    <li>В сервисе должен быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.</li>
    <li>После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) <a href="https://jservice.io/api/random?count=1">https://jservice.io/api/random?count=1</a> указанное в полученном запросе количество вопросов.</li>
    <li>Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данных можете выбрать сами, также можете добавлять свои колонки):
      <ul>
        <li>ID вопроса</li>
        <li>Текст вопроса</li>
        <li>Текст ответа</li>
        <li>Дата создания вопроса</li>
      </ul>
    </li>
    <li>В случае, если в БД уже существует такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.</li>
    <li>Ответом на запрос из п. 2 должен быть предыдущий сохраненный вопрос для викторины. В случае его отсутствия, ответ должен быть пустым объектом.</li>
  </ol>
  <h2>Технологии</h2>
  <div>
    <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white&color=9cf" alt="Postgresql Badge"/>
    <img src="https://img.shields.io/badge/FastAPI-blue?style=for-the-badge&logo=fastapi&logoColor=white&color=brightgreen" alt="FastAPI Badge"/>
    <img src="https://img.shields.io/badge/Postgres-green?style=for-the-badge&logo=postgresql&logoColor=white&color=informational" alt="Postgresql Badge"/>
    <img src="https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=blue" alt="Docker Badge"/>
  </div>
  <h2>Запуск проекта</h2>
  <ul>
  <li>Скачать и установить <a href='https://docs.docker.com/get-docker/'>Docker</a></li>
  <li>Клонировать репозиторий: <code> git clone https://github.com/KLYMENKORUS/Bewise_Test_task-1.git </code></li>
  <li>Установить зависимости: <code>pip install -r requirements.txt</code></li>
  <li>В корневой директории <code>src</code> создать файл .env и заполнить его по примеру .env.example</li>
  <li>В папке <code>src</code> выполнить команду <code>docker compose -f docker-compose.yaml up -d</code></li>
  <li>Выполнить команду <code>alembic upgrade heads</code> в папке <code>src</code></li>
  <li>Запустить сервер: <code>uvicorn main:app --reload</code></li>
  </ul>
  <h2>Пример запроса к API</h2>
  <div>
  <img src='https://github.com/KLYMENKORUS/Bewise_Test_task-1/assets/109753992/a4ca4444-9805-4e31-9222-6ddc5d77575e'></>
  <img src='https://github.com/KLYMENKORUS/Bewise_Test_task-1/assets/109753992/bf197dde-933c-4cda-a1be-ad2c39b4768b'></>
  <img src='https://github.com/KLYMENKORUS/Bewise_Test_task-1/assets/109753992/23fa70cd-9b5a-4512-a240-dc6655ad5eca'></>
  <img src='https://github.com/KLYMENKORUS/Bewise_Test_task-1/assets/109753992/cfb8a8d8-7510-48c7-8d51-60c48360059d'></>
  </div>

  
  
