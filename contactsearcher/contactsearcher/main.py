"""Define the command-line interface for the contact searching program."""

# TODO: Add all of the required import statements to this module

# TODO: create a Typer object to support the command-line interface


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
        f'  We are looking for contacts who have a job related to "{job_description}":'
    )
    # TODO: perform the search for all of the relevant email addresses given the job description
    # TODO: we know that there are some contacts in the list, so iterate through the list of
    # the contacts and display them in the terminal window
    # TODO: display final information about the program's behavior in the terminal window;
    # this should summarize whether or not the program found any matches
    # TODO: refer to the expected output on Discord and/or Proactive Programmers for details
