# PUZZLE PYRAMID

Puzzle Pyramid is Python terminal adventure game, It follows the story of a person who arrives in Cairo to explore a mysterious pyramid. The game contains storyline narrative, [Quiz](https://en.wikipedia.org/wiki/Quiz) questions and the game of [Rock, Paper, Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors). The game contains many opportunities for the player enter inputs and make choices on what option they would like to choose or which direction to take.

The game was made for those who enjoy the mythology of Ancient Egypt, quiz questions based on the mythology of Ancient Egypt, rock, paper, scissors and a story narrative. The contain has permadeath, so when you die you must restart from the beginning again.

[Live Link - Puzzle Pyramid](https://puzzle-pyramid.herokuapp.com/)

![App preview](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/mockup.PNG)

## UX & Design

## User Stories

- As a user, I would like to input my own name, so that I can have a more personalised experience.
- As a user, I would like to experience an interesting narrative, so that I can become immersed in the story.
- As a user, I would like to answer ancient Egyptian based questions, so that I can have fun while testing my knowledge.
- As a user, I would like to play game against interesting enemies, so that I can have fun and learn about the lore of the game universe.
- As a user, I would like to make meaningful choices, so that I can reply the game multiple times to experience all the paths.
- As a user, I would like to choose items, so that I explore multiple routes through the story.
- As a user, I would like to know the score during rock, paper, scissors so that I know if I am winning or losing.
- As a user, I would like to a smooth, coherent story that makes sense and flows correctly.
- As a user, I would like to get feedback if my inputs are incorrect, so that I know what is required to fulfil the validator.

## Flowchart

This flowchart gives an overview of the multiple paths, inputs and decision that can be made throughout the game. A rough version was drawn up in the planning stage before any code was typed, however as the game developed the flowchart also changed and morphed as new ideas were added and others removed.

![Flowchart](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/flowchart/flowchart.png)

## Favicon

The favicon used is a pyramid similar to those found it Egypt, it was chosen as it fits with the theme of the game.
![Favicon](https://github.com/ogc1231/puzzle-pyramid/blob/main/views/favicon/pyramid.png)

## Features

Below are the main features of the game with screenshots to give reference.

### Existing Features

- **Start Screen**

    - This the screen that greets the player when the first run the game. It shows the PUZZLE Pyramid ASCII Art and asks the user to enter their name.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/start_screen.PNG)

- **After Entering Name**

    - Player will be asked if they want to enter the pyramid or not.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/after_entering_name.PNG)

- **Invalid Name**

    - If an invalid name is entered (letters only and must at least two characters long) player will asked to enter another name that is valid.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/invalid_name.PNG)

- **Enter the Pyramid - No**

    - Player with be thanked for playing and program will exit.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/enter_no.PNG)

- **Enter the Pyramid - Yes**

    - Player will brought to the game story intro.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/enter_yes.PNG)

- **Arrive in Cairo  - Story Intro**

    - Story intro sets the setting and purpose of the story for the player.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/enter_yes.PNG)

- **Go to Shop - No**

    - Player will be asked if they want to go to the shop, if no they will go straight to bed and journey to the pyramid will being.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/go_to_shop_no.PNG)

- **Go to Shop - Yes**

    - Player heads to the in game shop. Player can choose between the rope or the torch to bring with them on their journey.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/go_to_shop_yes.PNG)

- **Choose Rope**

    - Player chooses the rope.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/chose_rope.PNG)

- **Choose Torch**

    - Player chooses the torch.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/chose_torch.PNG)

- **Entrance Question**

    - Journey to pyramid and first quiz question to open main entrance doors. Questions asks player what mythical creature has the head of a human and the body of a lion.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/go_to_shop_no.PNG)


- **Entrance Question - Wrong**

    - If wrong player will be told answer is in invalid and prompted to try again.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/q1_wrong_answer.PNG)

- **Entrance Question - Correct**

    - If correct the doors will open and player enters the pyramid.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/yes_rope.PNG)

- **If Rope Not Chosen**

    - If rope was NOT chosen player can choose to go left or right.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/no_rope.PNG)

- **If Rope Chosen**

    - If rope was chosen player can choose to use the rope or go left or right.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/yes_rope.PNG)

- **Use Rope**

    - If rope is used player skips to Rock, Paper, Scissors game with the Mummy.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/use_rope.PNG)

- **Direction 1 - Go Left**

    - Player goes left and dies. Game exits.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/d1_left.PNG)

- **Direction 1 - Go Right**

    - Player goes right and reaches another junction and choice to go left or right.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/d1_right.PNG)

- **Direction 2 - Go Right**

    - Player goes right and dies. Game exits.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/d2_right.PNG)

- **Direction 2 - Go Left**

    - Player goes left, goes up the starts and reaches Rock, Paper, Scissors game with the Mummy. 

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/d2_left.PNG)

- **Mummy Challenges You to Rock, Paper, Scissors**

    - Player plays Rock, Paper, Scissors game with the Mummy.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/use_rope.PNG)

- **Rock, Paper, Scissors - Mummy Wins Round**

    - If Mummy wins a round: "Bahahaha! I won that round."

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/mummy_wins_round.PNG)

- **Rock, Paper, Scissors - Player Wins Round**

    - If player wins a round: rock - Mummy: "You're better than you look!", paper - Mummy "How did you beat me!" scissors - Mummy: "Arrhh, not possible". 

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/player_wins_round.PNG)

- **Rock, Paper, Scissors - Round Tie**

    - If player and Mummy tie a hand: Mummy: "It's a tie, again human!".

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/round_tie.PNG)

- **Rock, Paper, Scissors - Mummy Wins Game**

    - If Mummy wins three rounds first: Mummy "You're Mine! Bahahaha!". Player dies. Game Exits.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/mummy_wins_game.PNG)

- **Rock, Paper, Scissors - Player Wins Game**

    - Player defeats the Mummy by winning three rounds first, player heads to next door.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/player_wins_game.PNG)

- **Post Mummy Door Question**

    - Second door asks player who is the Egyptian Sun God.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/player_wins_game.PNG)

- **Post Mummy Door Question - Wrong**

    - If wrong player will be told answer is in invalid and prompted to try again.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/q1_wrong_answer.PNG)

- **Post Mummy Door Question - Correct No Torch**

    - Doors open, however only darkness lays ahead, if player does NOT have the torch all they can do is enter.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/q2_correct_answer.PNG)

- **Post Mummy Door Question - Correct with Torch**

    - Doors open, however only darkness lays ahead, if player does have the torch all they can do is use the torch.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/yes_torch.PNG)

- **Use Torch**

    - Player uses torch which illuminates the path ahead. Thanks for playing. Game Exits.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/use_torch.PNG)

- **Enter Passage - No Torch**

    - The player enters the dark passage blindly. Thanks for playing. Game Exits.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/passage_enter.PNG)


### Future Features

- Move Levels
    - Add more levels to make a longer game

- More Items in Shop
    - Any additional notes about this feature.

- More Bosses
    - Add Anubis endgame boss and mini bosses

- Checkpoints/Save Game feature
    - So player can return later without losing progress

- More Games and Puzzles
    - Add multiple choice quiz game, riddles, Noughts & crosses game.

## Tools & Technologies Used

Below are the technologies used to built this app. The main technology used was Python.

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the favicon.
- [JavaScript](https://www.javascript.com) The script used to run the ock terminal.
- [Python](https://www.python.org) used as the main programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) used to help generate the Markdown files.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.


## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding, however some changes occurred during development.
[Draw.io](https://www.draw.io).

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/flowchart/flowchart.png)

### Classes & Functions

- `if __name__ == "__main__":`
    `clear()`
    `title()`
    `player_name()`
    `enter_pyramid()`
    - Used to ensure correct order of functions when called.
    
The primary functions used on this application are:

- `Clear()`
    - Clear function to clean-up the terminal, to increase readability.

- `exit_game()`
    - Function to exit game fully and not just current loop.

- `validate_choice(user_input, choices)`
    - Reusable function validate player inputs.

- `title()`
    - Prints Puzzle Pyramid ASCII text.

- `game_intro()`
    - Function to call game intro text.

- `player_name()`
    -  Function to validate input of player's name.

- `enter_pyramid()`
    - Function to start game or exit game.

- `game_shop()`
    - Function to go to the shop in game.

- `game_0()`
    - Function to call the first quiz question to open entrance door.

- `game_main()`
    - Function to start main game.

- `shopping()`
    - Function to choose to go shopping or not.

- `item_choice()`
    - Function to choose ITEM from shop.

- `level_1()`
    - Function to choose direction inside pyramid.

- `entrance_open`
    - Function to enter pyramid after correct answer is entered at entrance door.

- `door_open()`
    - Function to call door_open after correctly answering second question.

- `level_2()`
    - Function to call level_2 after beating the Mummy.

- `game_1`
    - Function to run first game: rock, paper, scissors.


### Imports

The following external imported packages were used.

- `os`: used for adding a `clear()` function
- `sys`: used for creating `exit_game()` function
- `random`: used to get a random choice from a list

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://puzzle-pyramid.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ogc1231/puzzle-pyramid) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ogc1231/puzzle-pyramid.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ogc1231/puzzle-pyramid)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ogc1231/puzzle-pyramid)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits
Links to tools, media and tutorials that were used during this project or inspired the gameplay.

### Credits and Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [YouTube](https://www.youtube.com/watch?v=fn68QNcatfo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=29) | Code for Rock, Paper, Scissors Game | Rock, Paper, Scissors tutorial in Python |
| [Asciiart](https://www.asciiart.eu/buildings-and-places/monuments/pyramids) | ASCII | Pyramid ASCII used in project|

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Icons8](https://icons8.com/icons/set/pyramid) | entire site | image | favicon on all pages |

### Acknowledgements

I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.

