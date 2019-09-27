# TPush

Telegram Push

Simple Utility to push files to telegram account from desktop.


### Setup Steps

1. Get Telegram bot token via BotFather on Telegram
2. Export it as environment variable by running: `export TPUSH_BOT_TOKEN=xxxxxx` where xxxxxx is your token. Optionally, edit python file to include bot token.
3. Export your own Telegram Chat ID as environment variable `export TPUSH_TARGET_ID=xxxxxx` where xxxxxx is your chat_id. Optionally, edit python file to include chat_id.
3. Install dependencies listed in requirements.txt via `pip install -r requirements.txt`
4. Add to path and start using.


```
    TPush ./Notes.pdf
```

With Comments:

```
    TPush ./Notes.pdf -m "Taken during meeting on 23rd September 2019"
```
