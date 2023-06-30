import click



@click.command()
@click.argument('sets', nargs=-1)
def make_set_operations(sets):
    
    if len(sets) < 2:
        click.echo(click.style("The minimum number of sets to perform set operations is 2", fg="red"))
    
    else:
    
        ls_sets = []
        for x in sets:
            s = set((int(x) for x in x.split(",")))
            ls_sets.append(s)
            
        intersection = set.intersection(*ls_sets)
        union = set.union(*ls_sets)
        
        click.echo(click.style(f"Set operations. Sets: {ls_sets}", fg="red"))
        for op, res in zip(("intersection", "union"), (intersection, union)):
            click.echo(click.style(f"{op}: {res}", fg="blue"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    make_set_operations()

