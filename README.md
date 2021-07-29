# Rick-roll

Rick-roll is a Python module for your rickrolling needs (which will never let you down). 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rick-roll.

```bash
pip install rick-roll
```

## Usage

```python
import rick_roll

# opens the classic rickroll
rick_roll.rickroll()

# opens a more subtle rickroll, chosen randomly
rick_roll.subtle_rickroll()

# prints some lyrics
print(rick_roll.rickroll_text(6))

# raises the very useful RickRollException (optionally, provide a message)
raise rick_roll.RickRollException("you've let me down")
```

## Contributing
Pull requests are welcome, but keep in mind this is mostly a joke.

## License
[MIT](https://choosealicense.com/licenses/mit/)