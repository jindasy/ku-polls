## Online Polls for Kasetsart University

An application for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial],
with additional functionality.

This application is part of the [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## How to Install and Run

1. Clone this KU-Polls repository in terminal
    ```
    git clone https://github.com/jindasy/ku-polls.git
    ```
2. Install requirement for this project by using command
    ```
    pip install -r requirement.txt
    ```
3. Create file `.env` and use example from `sample.env`
4. Start run web application by using command
   ```
   python manage.py runserver
   ```
5. Go to project urls
   ```
   http://localhost:8000/polls/
   ```

## Demo Users
| Username | Password |
|----------|----------|
| harry    | hackme22 |
| winky    | lalapo99 |

## Project Documents
All project documents are in the [Project Wiki](../../wiki/Home).
- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/2)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/3)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan) and [Task Board](https://github.com/users/jindasy/projects/2/views/4)

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
