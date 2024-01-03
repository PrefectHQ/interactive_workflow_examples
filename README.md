# Example human-in-the-loop Prefect flow

An example of using Prefect's human-in-the-loop feature.

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

## Running the flow
Once you're either set up and pointed at an open-source Prefect server or
Prefect Cloud, you can run the example:

    $ python flow.py
    
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
│ https://app.prefect.cloud/account/6550e075-ecda-452a-bec1-6b6906696fa5/workspace/967f4e4d-5129-4e7f-8127-95074e7cc58f/deployments/deployment/4df6eed4-10b0-41f7-93 │
│ dd-35f5ab9aefa0                                                                                                                                                    │
│                                                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
1
```

Follow either of the instructions in that message to run the flow from the UI or
the CLI.

Once you run the flow, there is a 90% chance that the flow will pause and ask
you to classify an image of an intriguing dog breed. You should see a Slack
notification with links to the image of the pug and Prefect's UI.

Follow the instructions in the Slack notification to see if you can help this
flow classify whether the image is a dog or a pig. 🤔
