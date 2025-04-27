import pickle
import typer
from process_trie import TextProcessor

cli = typer.Typer()
text_processor = TextProcessor()

@cli.command()
def load(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    text_processor.load(text)
    typer.echo(f"Text loaded successfully")
    with open("processor_state.pkl", "wb") as q:
        pickle.dump(text_processor, q)

@cli.command()
def hints(words):
    with open("processor_state.pkl", "rb") as q:
        cur_processor = pickle.load(q)
    ans = cur_processor.get_likeliest_next_words(words)
    typer.echo(f"Here are the hints:")
    typer.echo(ans)


if __name__ == '__main__':
    cli()