## Work in progress

Readme will be updated over the period

# To start working, fork this repository, clone your fork and do the following:

    git branch <Your Name>
    git switch <Your Name>
    git push --set-upstream origin <Your Name>

# Create a virtual environment and handle requirements    

    python -m venv freelance
    ./freelance/Script/Activate.ps1
    pip install -r requirements.txt
    

# Migrate databases  

    cd giggity
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

# Additional stuff
 We need to setup these folders which are not tracked by git because we are ignoring their contents

    mkdir templates/Messaging templates/Orders templates/Portfolio templates/Services media


# To push your changes:
    git add -A
    git commit -a -m "A message describing your commit" --author="Name <email>"
    git push origin

# To pick changes from this repo:
    git fetch https://github.com/Varad-13/django-freelance
    git cherry-pick <commit hash>