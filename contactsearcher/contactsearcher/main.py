"""Define the command-line interface for the contact searching program."""

# Add all of the required import statements to this module
from contactsearcher.search import search_for_email_given_job

# from search import search_for_email_given_job
from pathlib import Path
from typing import Optional
import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def contactsearcher(
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: Optional[Path] = typer.Option(None),
) -> None:
    """Search for either an email address of a contact who has a job in the file."""
    # declare an empty contacts_text
    contacts_text = ""
    # display details about the file provided on the command line
    # --> the file was not specified so we cannot continue using program
    if contacts_file is None:
        typer.echo("No contacts file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if contacts_file.is_file():
        contacts_text = contacts_file.read_text()
        contacts_line_count = len(contacts_text.splitlines())
        typer.echo(
            f"The contacts file contains {contacts_line_count} people in it! Let's get searching!"
        )
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not contacts_file.exists():
        typer.echo("The contacts file does not exist!")
    # display details about the search key for the job provided on the command line
    typer.echo("")
    typer.echo(
        f'  We are looking for contacts who have a job related to "{job_description}":\n'
    )
    # perform the search for all of the relevant email addresses given the job description
    matches = search_for_email_given_job(job_description, str(contacts_file))
    # we know that there are some contacts in the list, so iterate through the list of
    # the contacts and display them in the terminal window
    for i in range(len(matches)):
        typer.echo(f"{matches[i][0]} is a {matches[i][1]}")
    # display final information about the program's behavior in the terminal window;
    # this should summarize whether or not the program found any matches
    typer.echo("\nWow, we found some contacts! Email them to learn about your job!\n")
    # refer to the expected output on Discord and/or Proactive Programmers for details
