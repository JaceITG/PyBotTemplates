# PyBotTemplates
Some templates for creating a basic Discord bot using the Discord.py library.
Mainly designed for smaller-scale bots intended to be used primarily in a single server, but can be implemented in larger applications.

## Usage
* Change the file names according to your bot's naming scheme
  * Example: for a bot named Robot, should have files Robot.py (main script) and Robot_storage.py

* Replace the bot name placeholders in the main script (ctrl+F "BOTNAME" and replace all with your bot's name)

* Fill in the variables in the storage file with correct values

## Features
* Separate blocks to handle prefixed, implicit, and admin commands
* Variables containing frequently used message properties
* Handling of command line input (STD_IN)
* `sendMsg`, `sendEmbed`, and `sendFile` sending functions with logging and error catching
* `getLastImg(channel)` to retreive the url of the most recent image sent
* Help command embed
