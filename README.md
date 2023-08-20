## Work in progress

Readme will be updated in a while

# To start working, fork this repository, clone your fork and do the following:

    git branch <Your Name>
    git switch <Your Name>
    git push --set-upstream origin <Your Name>
    pip install -r requirements.txt
    cd giggity
    python manage.py migrate
    python manage.py createsuperuser

# To push your changes:
    git add -A
    git commit -a -m "A message describing your commit" --author="Name <email>"
    git push origin

# To pick changes from this repo:
    git fetch https://github.com/Varad-13/django-freelance
    git cherry-pick <commit hash>