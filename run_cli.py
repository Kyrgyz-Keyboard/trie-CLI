import pickle
import typer
from typing import List
from process_trie import TextProcessor

cli = typer.Typer()

@cli.command()
def load(file_path):
    typer.echo(f"Text loaded successfully")
    with open("text_state.pkl", "wb") as q:
        pickle.dump(file_path, q)

@cli.command()
def hints(words: List[str] = typer.Argument(..., show_default=False)):
    with open("text_state.pkl", "rb") as q:
        file = pickle.load(q)
    with open(file, "r") as f:
        text = f.read()
    cur_processor = TextProcessor()
    cur_processor.load(text)
    ans = cur_processor.get_likeliest_next_words(' '.join(words))
    typer.echo(f"Here are the hints:")
    typer.echo(ans)


if __name__ == '__main__':
    cli()