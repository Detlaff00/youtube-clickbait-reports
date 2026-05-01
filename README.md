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

<img width="1043" height="351" alt="Снимок экрана 2026-05-01 в 14 11 37" src="https://github.com/user-attachments/assets/045e1da6-6f96-41c4-9a04-3112c62efc36" />


## Тесты

```bash
pytest
```
