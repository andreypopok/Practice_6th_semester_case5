"""Кейс № 5. Создание страницы МДА в шести вариантах шрифта."""
from html import escape
from pathlib import Path

# Montserrat указан в CSS текста сайта МДА на предоставленном скриншоте.
MAIN_FONT = '"Montserrat", sans-serif'

# Имя файла, название варианта, значение CSS font-family.
FONTS = [
    ("index.html", "Montserrat — основной", MAIN_FONT),
    ("variant_1.html", "Arial", "Arial, sans-serif"),
    ("variant_2.html", "Verdana", "Verdana, sans-serif"),
    ("variant_3.html", "Tahoma", "Tahoma, sans-serif"),
    ("variant_4.html", "Georgia", "Georgia, serif"),
    ("variant_5.html", "Times New Roman", '"Times New Roman", serif'),
]


def main() -> None:
    # HTML-файлы сохраняются в папке output рядом с программой.
    output = Path(__file__).resolve().parent / "output"
    output.mkdir(exist_ok=True)

    for filename, name, font in FONTS:
        # Фиксированное подключение Montserrat; стили сайта не считываются.
        # Браузер загружает шрифт при просмотре основной страницы с интернетом.
        font_link = (
            '<link rel="stylesheet" '
            'href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&amp;display=swap">'
            if filename == "index.html" else ""
        )
        # Переход между вариантами — обычные ссылки, без JavaScript.
        links = []
        for target, label, _ in FONTS:
            current = ' aria-current="page"' if target == filename else ""
            links.append(f'<a href="{target}"{current}>{escape(label)}</a>')

        page = f'''<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Международный деловой альянс</title>
    {font_link}
    <style>
        * {{ box-sizing: border-box; }}
        body {{ margin: 0; padding: 24px; background: #f3f6f7;
               color: #444444; font-family: {font};
               font-size: 16px; line-height: 1.7; }}
        main {{ max-width: 920px; margin: auto; padding: 32px;
               background: white; border: 1px solid #dbe3e7; }}
        h1 {{ margin: 12px 0 24px; font-size: 2em; line-height: 1.2; }}
        h2 {{ margin-top: 28px; font-size: 1.3em; }}
        a {{ color: #087c87; }}
        nav {{ display: flex; flex-wrap: wrap; gap: 8px; }}
        nav a {{ padding: 6px 12px; border: 1px solid #b5c9ce;
                 text-decoration: none; }}
        nav a[aria-current] {{ background: #087c87; color: white; }}
        a:focus-visible {{ outline: 3px solid #087c87; outline-offset: 3px; }}
        footer {{ margin-top: 28px; padding-top: 16px;
                  border-top: 1px solid #dbe3e7; font-size: 0.85em; }}
        @media (max-width: 600px) {{
            body {{ padding: 12px; }}
            main {{ padding: 20px; }}
            h1 {{ font-size: 1.6em; }}
        }}
    </style>
</head>
<body>
<main>
    <p>Кейс-задача № 5 · Учебная страница</p>
    <h1>Международный деловой альянс</h1>
    <p><strong>ЗАО «Международный деловой альянс»</strong> — белорусская
       ИТ-компания, основанная в 1993 году и расположенная в Минске.</p>
    <p>Компания разрабатывает программное обеспечение, внедряет
       информационные системы и автоматизирует бизнес-процессы.</p>
    <h2>Основные направления деятельности</h2>
    <ul>
        <li>Разработка программного обеспечения.</li>
        <li>Автоматизация бизнес-процессов.</li>
        <li>Системный и бизнес-анализ, работа с данными.</li>
        <li>Сопровождение информационных систем.</li>
    </ul>
    <p>Официальный сайт: <a href="https://www.mdait.by/">www.mdait.by</a>.</p>
    <h2>Варианты шрифтов</h2>
    <p>Выбран вариант: <strong>{escape(name)}</strong>.</p>
    <nav aria-label="Выбор шрифта">{" ".join(links)}</nav>
    <footer>
        <p>Основной шрифт — Montserrat, как в CSS текста сайта МДА
           на предоставленном скриншоте. Для его загрузки через Google Fonts
           нужен интернет; без загрузки или локально установленного Montserrat
           браузер применит резервный шрифт. Дополнительные варианты
           используют шрифты, установленные на устройстве.</p>
    </footer>
</main>
</body>
</html>'''
        (output / filename).write_text(page, encoding="utf-8")

    print(f"Создано {len(FONTS)} HTML-страниц. Откройте: {output / 'index.html'}")


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        raise SystemExit(f"Не удалось сохранить HTML-файлы: {error}") from error
