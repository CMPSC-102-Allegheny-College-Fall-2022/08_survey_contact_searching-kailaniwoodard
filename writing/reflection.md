# Contact Searching

TODO: Make sure that you delete all of the TODO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Kai'lani Woodard

## Program Output

### What is the output from running the following commands?

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```Output
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

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```Output

  We are looking for contacts who have a job related to "neer":

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

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```Python
from contactsearcher.search import search_for_email_given_job
```

This line makes it possible to be able to use the `search` module within 
`main` because it imports from the `search.py` file the function 
`search_for_email_given_job`. I utilize the keywords `from` and `import` 
to perform this action, `from` specifying where to pull the function 
"from" and `import` is enacting the ability to import the specific 
function `search_for_email_given_job`. `contactsearcher.search` is 
referring to the package and the filename while `search_for_email_given_job` 
refers to the function we want to pull, as we mentioned before.

#### The source code statement that extracts the current job description for a contact

```Python
if job_description in str(current_line[1]).lower():
                contacts_list.append(current_line)
```

These two lines refer to the portions within the source code that 
extract the current job description for a contact. The variable 
`current_line` is a list type variable that is continually reassigned 
the value of the current given line while reading the file. I elected 
to use conditional logic in the form of an `if` statement checking 
if `job_description` is found within the contents of `current_line`.
When referring to `current_line` within the `if` statement, I elected 
to convert the second element of `current_line` to a string to convert 
the entire line into lowercase to ensure that it will indicate a match 
and add that to the list of contacts even if there is a difference in 
capitalization. From there, if the conditions of the `if` statement are 
fulfilled, the entire current line will be appended onto the end of 
`contacts_list` for later use for job description extraction.

#### Invocation of the function called `search_for_email_given_job`

```Python
    matches = search_for_email_given_job(job_description, contacts_file)
```

I feel at this point that I have implemented this source code survey in 
a way that would not involve invocation, because I am directly calling 
this function rather invoking it. However, I do want to call attention 
to the possibility that within this context, the terms may be currently 
being used with similar defintions. I personally have seen instances in 
where the terms are used interchangably, so from here on out I will be 
referring to them as so: please do not punish my grade too harshly for 
this, and I hope you understand.

The function by the name of `search_for_email_given_job` is first invoked 
when being assigned to the `matches` variable, it is called with the 
arguments `job_description` and `contacts_file`. This will assign whatever 
the `search_for_email_given_job` function returns as the value of `matches`. 
This function call is essential here because it will perform all of the actions 
within the function to return a value, which in this instance is a nested list 
with emails and job descriptions for potential contacts.

#### Test case for the function called `search_for_email_given_job`

```Python
def test_find_multiple_matching_result():
    """Check to ensure that search for contacts works for multiple matches."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engineer", contacts_database)
    assert len(contacts_list) == 2
```

Above is one of the test cases ensuring the functionality of `search_for_email_given_job` 
is working correctly. This specific test case is ensuring that there are multiple 
matching results for the keyword "engineer" within a sample contact list. The other test 
cases that invoke the function `search_for_email_given_job` check varying lengths of 
`contacts_list` variables after entering input that should have a specified answer in 
regards to length.

#### Execute trace of the `contactsearcher` program

TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`


1. `contactsearcher`

The `contactsearcher` function is the first function we invoke within our code. This function 
has CLI capabilities, enabling us to invoke this function when we run the above `poetry` command. 
This function takes in two arguments and returns nothing, as specified by the type annotation for 
the `NoneType` variable. From here, the program begins its execution. It declares empty variables 
and performs a series of checks to create informative dialog output to inform the user of where 
they are at in the process until we approach the assignment of the `matches` variable.

2. `search_for_email_given_job`

The `search_for_email_given_job` function is the second function that we have written that we move 
into the value of the variable `matches` on line 44 of our code within our `contactsearcher` 
function. From here, we elect to import the functionality of our written function from the `search.py` file. 
When we do this, we are enabling our abilities to search the contacts file for matching contacts. 
This function is intended to return a list of potential contacts that may be determined to be useful based on whether or not 
they contact the entered keyword. For this run, we entered "engineer", so when parsing through the 
file, we elect to convert the element within the nested list that contains the job description to 
lowercase to ensure we do not miss matches. This will in turn return a nested list with 12 elements 
containing 2 elements each for us to return to the terminal.

3. `contactsearcher`
After the conclusion of the duties of the `search_for_email_given_job` function, we return back 
into `contactsearcher` to complete the actions required for this program's purpose. We display 
the found contact matches in an orderly fashion and inform the user of the programs conclusion. 
We take the 12 elements we found and split the contact information, separating it from its job 
description using "is a" to present the information to the user. We then, again, gently remind 
the user to email their contacts.

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

One area that I struggled in was working with test cases that are already written and 
figuring out how to reconfigure those if my implementation of the source code may not be 
what the instructor exactly had in mind. This however, is always a good exercise, because 
I feel that test cases fall under my weaknesses within computer science.

### Based on your experiences with this project, what is one way in which you want to improve?

One way I would like to improve is my work with test cases. I rather understand test cases in 
a somewhat alright sense currently, perhaps that is a little humble, but I would like to continue 
to improve my understanding of test cases. Test cases were a topic that was covered for me during 
the Covid-19 pandemic and frankly I feel that my understanding was therefore weakened because of that. Therefore, I would like to improve my comfort level and knowledge of test cases.
