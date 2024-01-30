# Examples of Interactive Workflows with Prefect

This repository contains examples of using Prefect's Interactive Workflows
feature.

**Want to learn more about Interactive Workflows?** Check out the following resources:
- [Unveiling Interactive Workflows](https://www.prefect.io/blog/unveiling-interactive-workflows)
- [Creating Interactive Workflows](https://docs.prefect.io/latest/guides/creating-interactive-workflows/)

## Installing dependencies

Before you use this flow, you'll need to install its dependencies. Using
Python 3.10 or later with access to `pip`, run this code in your terminal:

    $ pip install -r requirements.txt
    
## Creating a Slack webhook block

This example uses a Slack webhook block to notify humans that we need them in
the loop. Follow the instructions in the [prefect-slack
repository](https://prefecthq.github.io/prefect-slack/) to create a webhook in
Slack and configure a Slack webhook block in Prefect that uses your new webhook.

**NOTE:** Make sure you name the Slack block `help-us-humans` because this code
will look for a block with that name.

## Signing in to Prefect

You can run this example flow using either an open-source Prefect
server or Prefect Cloud.

Using Prefect Cloud is faster. With Prefect installed, you can use the following
command to log in or sign up for a free trial:

    $ prefect cloud login

## Running the flows

Once you're either set up and pointed at an open-source Prefect server or
Prefect Cloud, you can run the examples.

### Human-in-the-loop machine learning

Our first example is a fake pig/dog image classifier that uses a human in the
loop. Learn more about this example in our blog post: [Unveiling Interactive Workflows](https://www.prefect.io/blog/unveiling-interactive-workflows?utm_campaign=Full+Broadcast+1%2F30&utm_content=Cloud+Broadcast&utm_medium=email_action&utm_source=email).

You can run the example like this:

    $ python human_in_the_loop.py
    
You'll see output like the following:

```
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Your flow 'classify-image' is being served and polling for scheduled runs!                                                                                         │
│                                                                                                                                                                    │
│ To trigger a run for this flow, use the following command:                                                                                                         │
│                                                                                                                                                                    │
│         $ prefect deployment run 'classify-image/guessing-classifier'                                                                                              │
│                                                                                                                                                                    │
│ You can also run your flow via the Prefect UI:                                                                                                                     │
│ https://app.prefect.cloud/account/<your URL>                                                                                                                       │
│                                                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Follow either of the instructions in that message to run the flow from the UI or
the CLI.

Once you run the flow, there is a 90% chance that the flow will pause and ask
you to classify an image of an intriguing dog breed. You should see a Slack
notification with links to the image of the pug and Prefect's UI.

Follow the instructions in the Slack notification to see if you can help this
flow classify whether the image is a dog or a pig. 🤔


### Pydantic models and validation

Similar to the human-in-the-loop flow, you can run an example that shows how to
use Pydantic models and validation to define flow run inputs like this:

    $ python pydantic_models_and_validation.py

This example is all about seeing the complex UI form that Prefect generates,
so follow the instruction to run the flow, then visit the flow run page in
Prefect's UI and click the Resume button to see the form.

### Sending and receiving input

We've included an example of interactive flows that send and receive input
data at runtime in the file `sending_and_receiving.py`. This example is
from our [Guide to Creating Interactive Flows](https://www.askmarvin.ai/welcome/tutorial/#getting-an-openai-api-key),
so check out that page to learn more about it.

You can run it by opening two terminals. In one terminal run:

    $ python sending_receiving.py greeter
    
In the other terminal run:

    $ python sending_receiving.py sender

### An LLM-powered chatbot

Our most advanced example of Interactive Workflows creates an interactive
terminal session that continuously sends questions to a GPT Assistant.
We don't have a write-up on this one, so check the module docstring in
the file `llm_chatbot.py`, read the code, try it out.

Instructions for running this example are in the file, but a summary is
much the same as the sending and receiving example -- mostly because this
example uses a similar producer/consumer setup with two flows.

In one terminal run:

    $ python sending_receiving.py answerer
    
In the other terminal run:

    $ python sending_receiving.py chat
