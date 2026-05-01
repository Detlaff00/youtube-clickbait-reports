# YouTube Clickbait Reports

CLI-приложение для формирования отчетов по CSV-файлам с метриками YouTube-видео.

В текущей версии поддерживается отчет `clickbait`: он показывает видео, у которых одновременно высокий CTR и низкое удержание. В отчет попадают строки, где `ctr > 15` и `retention_rate < 40`, результат сортируется по убыванию `ctr`.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
```

## Пример запуска

```bash
python -m youtube_reports --files examples/stats1.csv examples/stats2.csv --report clickbait
```

Такой же запуск можно выполнить через console script:

```bash
youtube-reports --files examples/stats1.csv examples/stats2.csv --report clickbait
```

Пример вывода:

```text
| title                                   |   ctr |   retention_rate |
|-----------------------------------------|-------|------------------|
| Секрет который скрывают тимлиды         |  25.0 |             22.0 |
| Как я спал по 4 часа и ничего не понял  |  22.5 |             28.0 |
| Как я задолжал ревьюеру 1000 строк кода |  21.0 |             35.0 |
| Купил джуну макбук и он уволился        |  19.0 |             38.0 |
| Я бросил IT и стал фермером             |  18.2 |             35.0 |
```

Скриншот запуска:

<!--
Чтобы добавить скриншот и не хранить файл картинки в репозитории:
1. Открой README.md на GitHub через Edit.
2. Перетащи скриншот в это место.
3. GitHub сам вставит ссылку вида:
   ![Пример запуска](https://github.com/user-attachments/assets/...)
4. Замени строку ниже на ссылку, которую вставит GitHub.
-->

![Пример запуска](https://github.com/user-attachments/assets/PASTE_SCREENSHOT_URL_HERE)

## Тесты

```bash
pytest
```
