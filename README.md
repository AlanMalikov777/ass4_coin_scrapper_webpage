# ASS4_coin_scrapper_webpage
Program that scraps information about specific cryptocurrenct in web page. Data will be saved in PostgreSQL table.
# Team

All changes was done by one account.
Asanuly Alikhan - main role in creating web-server.py and news.py 

Malikov Alan - connection to database and test folder creating, supporting to Alikhan with news.py

Kurmangali Sanzhar - template folder creating, supporting to Alikhan with web-server.py and news.py

# Installation
You need to download this libraries: 'Flask', 'Flask-SQLAlchemy', 'requests', 'beautifulSoup'.
With using this codes:
```bash
pip install Flask
```
```bash
pip install Flask-SQLAlchemy
```
```bash
pip install requests 
```
```bash
pip install beautifulsoup4
```
# Usage
Run test.py from test folder, use a direcory to the folder test and run it with this command in cmd or other termianls (src and test folders should be lockated in one package)
``` bash
python test.py
```
Alternative is taking python files from src and use it by your own or copy code and use it.
# Examples
You need to enter a coin into search block and program will give you a list of paragraphs.
For example, 'dogecoin':
![Снимок экрана (1175)](https://user-images.githubusercontent.com/77801087/141104875-31d55dc7-fd02-4d13-b0fc-08770b763190.png)
and after that click find:
![photo_2021-11-10_17-27-46](https://user-images.githubusercontent.com/77801087/141105125-d4fadb72-b39b-4282-9809-7243c89924ef.jpg)
it will give a result as 10 paragraphs.

Results in PostrgeSQL table:
![Снимок экрана (1177)](https://user-images.githubusercontent.com/77801087/141105677-06dda7a9-0a87-46b6-a0d0-8f2d595feb50.png)
# License
[MIT](https://choosealicense.com/licenses/mit/)
