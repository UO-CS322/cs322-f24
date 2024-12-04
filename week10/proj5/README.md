[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nnlYpTPe)
# Project 5: Brevet time calculator with Ajax and MongoDB

Simple list of controle times from Project 4 stored in MongoDB database.

## What is in this repository

You have a minimal implementation of Docker comppose in DockerMongo folder, using which you can connect the flask app to MongoDB. Refer to the lecture slide `05a-Table-driven.pdf` and `05b-Docker-Compose.pdf` and this [example](https://github.com/UO-CS322/cs322-f24/tree/main/week7/duckies). You also have MongoCommands.txt (on Canvas and the lecture code repo).

### Functionality you'll add

You will reuse *your* code from  Project 4. Recall: you created a list of open and close controle times using AJAX. In this project, you will create the following functionalities.

1. Create two buttons "Submit" and "Display" in the page where you have controle times. Optionally, create a Clear button to clear previously displayed information.
2. On clicking the "Submit button", the control times should be entered into the database.
3. On clicking the Display button, all the entries from the database should be displayed on a new page.
4. Optionally (up to +20 extra points), implement a delete function (e.g., having "Delete" buttons next to data rows on the display page).

Handle error cases appropriately. For example, "Submit" should return an error if there are no controle times. One can imagine many such cases: you'll come up with as many cases as possible.

## Tasks

* Produce a working application (`app.py` and `app.ini`)
* A `README.md` file that includes not only identifying information (your name) but but also a revised, clear specification of the brevet controle time calculation rules.
* Selenium test cases for the two buttons in `test_buttons.py`
* `Dockerfile`  (update as needed)
* `docker-compose.yml` (update as needed)

### Testing

You are primarily responsible for ensuring your application works. You can test by running locally, but make sure your application also works with docker-compose. To test with docker-compose,

```bash
docker-compose up --build
python app.py
```

In a different terminal, you can run your selenium tests with `python test_buttons.py`  (ensure your flask app is running first). Also interactively test your app from a browser as usual.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
  * AJAX in the frontend. That is, open and close times are automatically populated,
  * Frontend to backend interaction (with correct requests/responses),
  * README is updated with your name and email.

Scores: 

* a) HTML/Ajax present and working (20)
* b) Database logic (20)
* c) At least two Selenium test cases present and working,  `test_buttons.py` (20)
* d)  `Dockerfile` (10)
* e)  `docker-compose.yml` builds and works (20)
* f) README updated (10)

For this project, most of the grading will be manual.
