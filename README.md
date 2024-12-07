![Art](https://i.postimg.cc/yNFLmgXK/art.png)

![GitHub Created At](https://img.shields.io/github/created-at/id-andyyy/AstroHR?style=flat&color=F25430)
![Lines Of Code](https://tokei.rs/b1/github/id-andyyy/AstroHR?style=flat&category=code&color=006666)
![Top Language](https://img.shields.io/github/languages/top/id-andyyy/AstroHR?style=flat)

# AstroHR&nbsp;&#128302;

A tool for analyzing employee compatibility in a company based on a natal chart&nbsp;&#127775;. Created as part of the [Namix Code&nbsp;&#128104;&#8205;&#128187;](https://naimixcode.ru/) hackathon.

## Description

A tool for HR specialists and recruiters that allows evaluating the compatibility of candidates, colleagues, employees, and subordinates based on astrological data and natal charts.&nbsp;&#10024;

Website sections:

- &#127968; Home (login for HR specialists, buttons to navigate to other sections)
- &#129309; Compatibility Check (requires entering personal data, including date and place of birth to get compatibility results with the company. HR specialist can approve a candidate by sending them an email with the result)
- &#127775; Team Compatibility (view compatibility results between employees from different departments)
- &#128161; Recommendation Generation (get advice on improving interaction between employees based on compatibility results - available only to HR specialists)

## Demo

Visit the [website](https://astrohr.pythonanywhere.com/) or watch the demo (click on the image)&nbsp;&#128071;

[![Preview](https://i.postimg.cc/jSkbp1G2/preview.png)](https://youtu.be/2M027cCYfWM)

## Technologies and Tools

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white&color=013b2a)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white&color=000000)
![HTML5](https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=white&color=yellow)
![YandexGPT](https://img.shields.io/badge/YandexGPT-%23F24E1E.svg?style=for-the-badge&logoColor=white&color=8B5CF6)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white&color=#6CeA8C)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white&color=f14e32)

Development features:

- Project was written in three days during the [Namix Code&nbsp;&#128104;&#8205;&#128187;](https://naimixcode.ru/) hackathon
- Django framework used
- SQLite database
- YandexGPT neural network used for recommendation generation
- Responsive design
- BEM methodology
- Additional libraries used for determining birthplace coordinates
- Meta tags and Yandex.Metrica configured

## Functionality Implementation

To calculate compatibility, each person's ascendant is calculated through the `get_asc_num()` function using date, time, and place of birth. Then ascendants are compared through `get_compatibility()`, where compatibility matrix has values from -100 to +100 for each pair of signs. When checking candidate's compatibility with the team, the system compares their ascendant with all team members, calculating the average value, and generates hiring recommendations based on this.

## Getting Started

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&duration=2500&color=F7F7F7&background=000000&multiline=true&width=625&height=165&lines=git+clone+https%3A%2F%2Fgithub.com%2Fid-andyyy%2FAstroHR.git;cd+AstroHR;pip+install+-r+requirements.txt;python+manage.py+migrate;python+manage.py+createsuperuser;python+manage.py+runserver)](https://git.io/typing-svg)

For the project to work correctly, you need to create a `.env` file in the root directory and fill it according to the `.env.example` file, replacing placeholders with secret keys.

## Feedback

I would appreciate if you could give a star&nbsp;&#11088;. If you found a bug or have suggestions for improvement, please use the [Issues](https://github.com/id-andyyy/AstroHR/issues) section.

## Authors

Development team [Mojarung](https://t.me/mojarung):

- [Andrey Obrezkov](https://github.com/id-andyyy) (fullstack developer)
- [Vladislav Politsyn](https://t.me/wasbyy7) (frontend developer)
- [Yaroslav Roldugin](https://github.com/Felicuss) (backend developer)
- [Alina Zueva](https://github.com/ZuevaAlinam) (astrologist)
- [Kirill Veriyalov](https://github.com/verikirill) (deployment assistant)

Read in [Russian&nbsp;&#127479;&#127482;](README-ru.md)