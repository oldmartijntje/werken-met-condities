@echo off
color a
set /p allRightsReservedToOldMartinG=[message]
if NOT %allRightsReservedToOldMartinG%=="1"(goto messageAdded)
git commit -a -m "default commit message"
git commit -a -m "default commit message"
git add --all
git commit -a -m "default commit message"
git push
set /p anwserr=[done]
exit
messageAdded:
git commit -a -m %allRightsReservedToOldMartinG%
git commit -a -m %allRightsReservedToOldMartinG%
git add --all
git commit -a -m %allRightsReservedToOldMartinG%
git push
set /p anwserr=[done]
exit