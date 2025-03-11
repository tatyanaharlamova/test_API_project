#**ПРОЕКТ АВТОМАТИЗАЦИИ API - ТЕСТОВ**

Проект тестового задания по автоматизации API-тестов для ресурса Posts на сайте https://jsonplaceholder.typicode.com/

- Язык программирования **Python**;
- Фреймворк **Pytest**; 
- Библиотека **Requests** для работы с HTTP-запросами.

**Установка и запуск**

 ***1. Клонирование репозитория***

```bash
git clone git@github.com:tatyanaharlamova/test_API_project.git
cd test_API_projec
```

 ***2. Запуск тестов с формированием отчета о покрытии***

```bash
pytest test_posts.py -v --html=report.html
```
Отчет будет сохранен в файле report.html, который можно открыть в браузере.
