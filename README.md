## Online Polls for Kasetsart University

![Unittest Workflow](https://github.com/jindasy/ku-polls/actions/workflows/python-app.yml/badge.svg)


An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial],
with additional functionality.

This application is part of the [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## How to Install

1. Clone this KU-Polls repository in terminal
    ```
    git clone https://github.com/jindasy/ku-polls.git
    ```

2. Move to project directory
   ```
    cd ku-polls
   ```

3. Create virtual environment
   ```
   python -m venv env
   ```

4. Start the virtual env in bash or zsh
   ```
   . env/bin/activate 
   ```

5. Install requirement for this project by using command
    ```
    pip install -r requirements.txt
    ```

6. Create new database
   ```
   python manage.py migrate
   ```

7. Import data
   ```
   python manage.py loaddata data/polls.json data/users.json
   ```

8. Create file `.env` and use example from `sample.env`

**Note**: To exit the virtualenv, type `deactivate`, or close the terminal window.

## How to Run

1. Start run web application by using command
   ```
   python manage.py runserver
   ```
2. Go to project urls
   ```
   http://localhost:8000/polls/
   ```

## Demo Users
| Username | Password |
|----------|----------|
| nobi     | nobita00 |
| winky    | lalapo99 |

## Project Documents
All project documents are in the [Project Wiki](../../wiki/Home).
- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/2)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/3)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/4)
- [Iteration 4 Plan](../../wiki/Iteration%204%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/6)

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
