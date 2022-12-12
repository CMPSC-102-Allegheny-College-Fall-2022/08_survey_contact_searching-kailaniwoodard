"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # create an empty list of the contacts
    contacts_list = []
    # create an empty current line
    current_line = 0
    # iterate through the file, parsing it line by line
    if type(contacts) is not str:
        with open(contacts, "r") as input_file:
            reader = csv.reader(input_file)
            # refer to the file called input/contacts.txt to learn more about
            # the format of the comma separated value (CSV) file that we must parse
            # iterate through each line of the file and extract the current job
            for i in reader:
                current_line = i
                # ---> extract the current job for the contact on this line of the CSV
                # ---> the job description matches and thus we should save it in the list
                if job_description in str(current_line[1]).lower():
                    contacts_list.append(current_line)
        # return the list of the contacts who have a job description that matches
    elif type(contacts) is str:
        contacts_str = contacts.split("\n")
        for i in contacts_str:
            current_line = i
            line_job_desc = current_line.split(",")
            if job_description in line_job_desc[1]:
                contacts_list.append(current_line)

    return contacts_list
