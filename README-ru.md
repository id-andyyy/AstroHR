![Арт](https://i.postimg.cc/yNFLmgXK/art.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/AstroHR?style=flat&color=F25430)
![Lines Of Code](https://tokei.rs/b1/github/id-andyyy/AstroHR?style=flat&category=code&color=006666)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/AstroHR?style=flat)

# AstroHR&nbsp;&#128302;

Сайт для оценивания совместимости сотрудников компании&nbsp;&#127775;. Создан в рамках хакатона [Namix Code&nbsp;&#128104;&#8205;&#128187;](https://naimixcode.ru/).

## Описание

Инструмент для HR-специалистов и рекрутеров, позволяющий оценивать совместимость кандидатов, коллег, сотрудников и подчинённых на основе астрологических данных и натальной карты.&nbsp;&#10024;

Разделы сайта:

- &#127968; Главная (вход для HR-специалистов, кнопки для перехода к другим разделам)
- &#129309; Проверка совместимости (требуется ввести свои данные, в том числе дату и место рождения для получения результата совместимости с компанией. HR-специалист может одобрить кандидата, отправив ему письмо с результатом)
- &#127775; Совместимость внутри команды (просмотр результатов совместимости между сотрудниками разных отделов)
- &#128161; Генерация рекомендаций (получение советов по улучшению взаимодействия между сотрудниками на основе результатов совместимости - доступно только HR-специалистам)

## Демонстрация

Посетите [сайт](https://astrohr.pythonanywhere.com/) или посмотрите демонстрацию (клик на картинку)&nbsp;&#128071;

[![Превью](https://i.postimg.cc/jSkbp1G2/preview.png)](https://youtu.be/2M027cCYfWM)

## Технологии и инструменты

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white&color=013b2a)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white&color=000000)
![HTML5](https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=white&color=yellow)
![YandexGPT](https://img.shields.io/badge/YandexGPT-%23F24E1E.svg?style=for-the-badge&logoColor=white&color=8B5CF6)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white&color=#6CeA8C)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white&color=f14e32)

Особенности разработки:

- Проект написан за три дня в рамках хакатона [Namix Code&nbsp;&#128104;&#8205;&#128187;](https://naimixcode.ru/)
- Использован фреймворк Django
- База данных на SQLite
- Для генерации рекомендаций использована нейросеть YandexGPT
- Адаптивная верстка
- БЭМ-методология
- Использование дополнительных библиотек для определения координат места рождения
- Настроены мета-теги и Яндекс.Метрика

## Реализация функционала

Для расчета совместимости для каждого человека вычисляется его асцендент через функцию `get_asc_num()`, используя дату, время и место рождения. Затем происходит сравнение асцендентов через `get_compatibility()`, где в матрице совместимости для каждой пары знаков заданы значения от -100 до +100. При проверке совместимости кандидата с командой система сравнивает его асцендент со всеми членами команды, вычисляя среднее значение, и на основе этого генерирует рекомендации по найму.

## Начало работы

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&background=000000&multiline=true&width=625&height=165&lines=git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FAstroHR.git;cd+AstroHR;pip+install+-r+requirements.txt;python+manage.py+migrate;python+manage.py+createsuperuser;python+manage.py+runserver)](https://git.io/typing-svg)

```sh
git clone https://github.com/id-andyyy/AstroHR.git
cd AstroHR
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Для корректной работы проекта в корне необходимо создать файл `.env` и заполнить его в соответствии с файлом `.env.example`, заменяя заглушки секретными ключами.

## Обратная связь

Буду признателен, если вы поставите звезду&nbsp;&#11088;. Если вы нашли баг или у вас есть предложения по улучшению,
используйте раздел [Issues](https://github.com/id-andyyy/AstroHR/issues).

## Авторы

Команда разработчиков [Mojarung](https://t.me/mojarung):

- [Андрей Обрезков](https://github.com/id-andyyy) (fullstack developer)
- [Владислав Полицын](https://t.me/wasbyy7) (frontend developer)
- [Ярослав Ролдугин](https://github.com/Felicuss) (backend developer)
- [Алина Зуева](https://github.com/ZuevaAlinam) (astrologist)
- [Кирилл Вериялов](https://github.com/verikirill) (deployment assistant)

Читать на [английском&nbsp;&#127468;&#127463;](README.md)