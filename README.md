# Contact Searching

## Assigned: Friday, November 11, 2022
## Due: Monday, November 14, 2022 by midnight

## Project Goals

This programming project invites you to implement a program called
`contactsearcher`. This program takes as input a comma separate value (CSV) file
that contains the email address and job description of a person and a string
that describes a specific job. After reading in and parsing the CSV file, the
`contactsearcher` program will find the email addresses of all the people who
have a job description that contains the provided description. Along with adding
documentation to the provided source code, you will create your own Python
functions that uses iteration constructs and conditional logic to implement a
correct program that passes the test suite and all of the checks.

## Project Access

You can access this assignment by clicking the link provided to you in Discord.
Once you click this link it will create a GitHub repository that you can clone
to your computer. Specifically, you
will need to use the `git clone` command to download the project from GitHub to
your computer. Now you are ready to add source code and documentation to the
project!

## Expected Output

This project invites you to implement a CSV file parsing and searching program
called `contactsearcher`. The program accepts through its command-line interface
the name of a file, in this case `input/contacts.txt`, that contains the contact
information and job title descriptions for some people. For instance, here are
the first lines of this file:

```
tylernelson@gmail.com,Careers adviser
gregory02@medina-mayer.com,"Accountant, chartered management"
jonesmiguel@hotmail.com,Health and safety inspector
rsanchez@yahoo.com,"Surveyor, planning and development"
hillfrank@ward-wood.com,"Scientist, physiological"
aaronhunter@gmail.com,"Surveyor, insurance"
kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer
bakererin@morales.com,"Programmer, multimedia"
```

It is worth noting that the `input/contacts.txt` file contains synthetic data
that the [Faker](https://github.com/joke2k/faker) program automatically
generated. With that said, after you have correctly implemented all of the
required features, running the program with the command `poetry run
contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
will produce the following output:

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

  joe70@yahoo.com is a Network engineer
  torresjames@white.info is a Electrical engineer
  grahamjoel@castillo-gilbert.net is a Engineer, technical sales
  gsutton@miller.com is a Engineer, maintenance
  gharris@villarreal-snow.com is a Water engineer
  williamsondavid@lopez.com is a Automotive engineer
  ronald83@yahoo.com is a Maintenance engineer
  zmarshall@yahoo.com is a Control and instrumentation engineer
  christopher35@yahoo.com is a Civil engineer, consulting
  jacquelinedavid@hotmail.com is a Engineer, electronics
  espinozadaryl@hill-maddox.com is a Engineering geologist
  edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

Notice that the output confirms that there are `100` rows inside of the CSV file
called `input/contacts.txt` and that you instructed the program to return all of
the email addresses for people whose job description contains the word
`engineer`. For the current version of the CSV file, there are twelve people who
have `engineer` in their job description, including `edwardsjacob@gmail.com` who
is a `Chemical engineer` and `joe70@yahoo.com` who is a `Network engineer`.
Since the `contactsearcher` program should return the contact information for
every person who has the provided job description in their job title, searching
for `engin` instead of `engineer` should also return details about
`edwardsjacob@gmail.com` and `joe70@yahoo.com`. To learn more about how to run
this program, you can type the command `poetry run contactsearcher --help` to
see the following output showing how to use `contactsearcher`:

```
Usage: contactsearcher [OPTIONS]

  Search for either an email address of a contact who has a job in the
  file.

Options:
  --job-description TEXT  [required]
  --contacts-file PATH
  --install-completion    Install completion for the current shell.
  --show-completion       Show completion for the current shell, to copy
                          it or customize the installation.

  --help                  Show this message and exit.
```

Please note that the provided source code does not contain all of the
functionality needed to produce this output. As explained in the next section,
you are invited to add all of the missing features to ensure that
`contactsearcher` produces the expected output. Once you finish the program, it
should produce all of the expected output.

    Recall that if you want to run `contactsearcher` you must use your terminal
    window to first go into the GitHub repository containing this project and
    then go into the `contactsearcher` directory that contains the project's
    source code. Remember that before running the program you must run `poetry
    install` to add the dependencies!

## Adding Functionality

If you study the file called `contactsearcher/contactsearcher/main.py` you will
see that it has many `TODO` markers that designate the parts of the program that
you need to implement before `contactsearcher` will produce correct output.
Along with adding requested source code to the `main` module, you should
implement the function in the `convert` module called
`search_for_email_given_job(job_description: str, contacts: str) ->
List[List[str]]`. This function takes as input two `str` variables called
`job_description` and `contacts`, with the first of these containing, for
instance, `engineer`, and the second containing all of the contents of the
provided CSV file. The `search_for_email_given_job` function should use the
`csv` package's `reader` function to input the CSV file on a row-by-row basis,
and then check each row to see if its job description contains the contents of
the `job_description` variable. If the job description on a specific line has
within it the provided `job_description`, then the function should record the
email address and continue processing the remainder of the file.

## Running Checks

If you study the source code in the `pyproject.toml` file you will see that
it includes the following section that specifies different executable tasks:

```toml
[tool.taskipy.tasks]
black = { cmd = "black contactsearcher tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 contactsearcher tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy contactsearcher", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle contactsearcher tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint contactsearcher tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

This section makes it easy to run commands like `poetry run task lint` to
automatically run all of the linters designed to check the Python source code in
your program and its test suite. You can also use the command `poetry run task
black` to confirm that your source code adheres to the industry-standard format
defined by the `black` tool. If it does not adhere to the standard then you can
run the command `poetry run black contactsearcher tests` and it will automatically
reformat the source code.

If your program has all of the anticipated functionality, you can run the
command `poetry run task test` and see that the test suite produces the
following output. As you finish your implementation of the
`search_for_email_given_job` function you can use this test suite to confirm
that it is working correctly. If one of the test cases fails, you can use its
output to help you understand what is not yet working in the function under
test. After all of the test cases pass, you can use the command `poetry run task
all` to confirm that other aspects of your source code and
technical writing are correct.

```
tests/test_search.py .....

============================ 5 passed in 0.02s =============================
```

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block and explain the meaning of the Python source code segments that you
implemented and tested. As you answer the reflection's questions, take
particular care as you explain every computational step that occurs when running
the program with a command like `poetry run contactsearcher --job-description
"engineer" --contacts-file input/contacts.txt`.

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.

## Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the repository associated
with this assignment students will receive a checkmark grade if their last before-the-deadline
build passes. This is only checking some baseline writing and commit requirements as well as correct
running of the program. An additional reduction will be given if the commit log shows a cluster
of commits at the end clearly used just to pass this requirement. An addition reduction
will also be given if there is no commit during work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark
grade when the responses to the writing questions presented in the `reflection.md` reveal
a proficiency of both writing skills and technical knowledge. To receive a checkmark grade,
the submitted writing should have correct spelling, grammar, and punctuation in addition
to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion
of their assignment grade when their program implementation reveals that they have mastered
all of the technical knowledge and skills developed during the completion of this assignment.
As a part of this grade, the instructor will assess aspects of the programming including,
but not limited to, the completeness and the correctness of the program and the use of
effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the class or lab times are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
