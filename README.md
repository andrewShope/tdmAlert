# Alert Bot

This is a bot that will alert users of Quake Live pickup games when their games have begun. When the game gets enough players, this bot will send a text message to any players who are in that particular game and have given their contact info.

### How It Works

1. Connect to the channel.
2. Listen for messages from the pickup bot alerting that a game has begun.
3. Break the message down into a list of players that are in the game.
4. For each player in the game, check to see if their contact info is stored.
5. If so, send a text to that player.

To send texts, the bot sends out emails using SMS gateways.