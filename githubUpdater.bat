@echo off
color a
set /p anwser=[message]
git commit -a -m %anwser%
git commit -a -m %anwser%
git add --all
git commit -a -m %anwser%
git push
set /p anwserr=[done]