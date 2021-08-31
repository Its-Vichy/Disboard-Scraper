<h1 align="center">Disboard-Scraper</h1>

<p align='center'>
    <b>Threaded Scraper to get discord servers from [disboard.org](https://disboard.org) written in python3.</b><br>
    <br>
    <img src='https://monashdatafluency.github.io/python-web-scraping/images/request.png'>
</p>

----

<br><br>

> # Setup.

* One thread / tag
* If you whant to look for multiple tag in same session: `tag1+tag2` (**Max: _5_**)
* You can sort by `member_count` or `bumped_at`.

```py
for keywords in ['tag1', 'tag2', 'multiple+tag']:
    # bumped_at / member_count
    threading.Thread(target= Scraper().get_redirect, args=(keywords, 'bumped_at',)).start()
``` 

<br>

> # Warning.

* ***This project was made for educational purposes only! I take no responsibility for anything you do with this program.***
* ***If you have any suggestions, problems, open a problem (if it is an error, you must be sure to look if you can solve it with [Google](https://giybf.com)!)***

<br>

> # Support me.

* Thanks for looking at this repository, if you like to press the ⭐ button!
* Made with 💖 by [Vichy](https://github.com/Its-Vichy).
* RCΛ Love u.

<p align="center"> 
    <b>Informations</b><br>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Its-Vichy/Disboard-Scraper?style=social">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Its-Vichy/Disboard-Scraper">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Its-Vichy/Disboard-Scraper">
    <img alt="GitHub" src="https://img.shields.io/github/license/Its-Vichy/Disboard-Scraper">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/Its-Vichy/Disboard-Scraper?style=social">
</p>
