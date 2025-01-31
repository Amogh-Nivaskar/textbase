# Roadmap Generation Chatbot based on Textbase

It is a chatbot which generates roadmaps for any new piece of technology anyone wants to learn. It is connected to an external server hosted on render.com whos repo is at - https://github.com/Amogh-Nivaskar/roadmap-chatbot-server

Link of video demonstration on YouTube - https://www.youtube.com/watch?v=LoKx7v7MtDg

Try it out at - https://bot.textbase.ai/amoghpnivas/roadmap-chatbot-v8

# Textbase

✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py` and Textbase will take care of the rest :)

Since it is just Python you can use whatever models, libraries, vector databases and APIs you want.

_Coming soon:_

- [ ] PyPI package
- [ ] SMS integration
- [ ] Easy web deployment via `textbase deploy`
- [ ] Native integration of other models (Claude, Llama, ...)

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry shell
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

```bash
poetry run python textbase/textbase_cli.py test
```
Response:
```bash
Path to the main.py file: main.py #Type main.py here
```
Now go to the link which is shown on the CLI and you will be able to chat with your bot!

_Simpler version using PyPI package and CLI coming soon!_

## Contributions

Contributions are welcome! Please open an issue or a pull request.
