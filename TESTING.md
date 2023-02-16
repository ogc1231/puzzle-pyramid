# Testing

Return back to the [README.md](README.md) file.

Below is all the testing carried out on this application to find any bugs, errors or performance issues.

## Code Validation
### Python Validator - PEP8

The recommended [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python file, no errors were returned.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/puzzle-pyramid/main/run.py) | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/CI_Python_Linter.PNG) | Pass: No Errors  |

### NOQA

`noqa` = **NO Quality Assurance**
- Noqa was used for the Puzzle Pyramid ASCII Art to remove errors.

## Lighthouse Audit

Deployed app was tested using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | Desktop | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/lighthouse.PNG) | All above 90 |
| run.py | Mobile | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/lighthouse_mobile.PNG) | Performance 88 |


## Defensive Programming - Input Testing & Validation 


Defensive programming - Input Testing & Validation was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Enter Name | | | | |
| | Input: "a" | Invalid: Enter a name containing at least 2 letters!, enter name | Pass | As expected |
| | Input: "1" | Invalid: Enter a name containing at least 2 letters!, enter name | Pass | As expected |
| | Input: "sam" | Moves onto - Do you wish to enter the pyramid and capitalises | Pass | As expected |
| | Input: "pizza" | Moves onto - Do you wish to enter the pyramid and capitalises | Pass | As expected |
| | Input: "12223" | Invalid: Enter a name containing at least 2 letters!, enter name | Pass | As expected |
| Enter the Pyramid? | | | | |
| | Input: "Yes" | Moves onto - Go shopping?| Pass | As expected |
| | Input: "No" | Thanks for playing!, Game Exits | Pass | As expected |
| | Input: "yeah" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Go shopping? | | | | |
| | Input: "yes" | Moves onto - Choose rope or torch | Pass | As expected |
| | Input: "No" | Moves onto - Entrance question | Pass | As expected |
| | Input: "yeah" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Rope or Torch? | | | | |
| | Input: "torch" | Rope is chosen, Moves onto - Entrance question | Pass | As expected |
| | Input: "rope" | Torch is chosen, Moves onto - Entrance question | Pass | As expected |
| | Input: "Yes" | Not valid enter to try again | Pass | As expected |
| | Input: "No" | Not valid enter to try again | Pass | As expected |
| | Input: "yeah" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Entrance Question | | | | |
| | Input: "sphinx" | Entrance opens move direction1 choice | Pass | As expected |
| | Input: "No" | Not valid enter to try again | Pass | As expected |
| | Input: "yeah" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Direction 1 Choice - rope chosen | | | | |
| | Input: "rope" | If rope was chosen, use rope and move onto RPS with Mummy | Pass | As expected |
| | Input: "left" | If rope was chosen, uses rope and move onto RPS with Mummy | Fail | Not as expected |
| | Input: "right" | If rope was chosen, uses rope and move onto RPS with Mummy | Fail | Not as expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Direction 1 Choice - rope NOT chosen | | | | |
| | Input: "left" | Go left and die, game exits | Pass | As expected |
| | Input: "right" | Go right and move onto direction 2 choice | Pass | As expected |
| | Input: "rope" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Direction 2 Choice | | | | |
| | Input: "left" | Go left and move onto RPS with Mummy | Pass | As expected |
| | Input: "right" | Go right and die, game exits | Pass | As expected |
| | Input: "rope" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Direction 2 Choice | | | | |
| | Input: "left" | Go left and move onto RPS with Mummy | Pass | As expected |
| | Input: "right" | Go right and die, game exits | Pass | As expected |
| | Input: "rope" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Rock, Paper, Scissors | | | | |
| | Input: "rock" | Player uses rock | Pass | As expected |
| | Input: "paper" | Player uses paper | Pass | As expected |
| | Input: "scissors" | Player uses scissors | Pass | As expected |
| | Input: "pizza" | Not valid, chose a hand Rock, Paper or Scissors | Pass | As expected |
| | Input: "1" | Not valid, chose a hand Rock, Paper or Scissors  | Pass | As expected |
| Post Mummy Door Question | | | | |
| | Input: "ra" | Entrance opens move direction1 choice | Pass | As expected |
| | Input: "RA" | Entrance opens move direction1 choice | Pass | As expected |
| | Input: "sphinx" | Not valid enter to try again | Pass | As expected |
| | Input: "No" | Not valid enter to try again | Pass | As expected |
| | Input: "yeah" | Not valid enter to try again | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again | Pass | As expected |
| | Input: "1" | Not valid enter to try again | Pass | As expected |
| Dark Passage, torch NOT chosen | | | | |
| | Input: "enter" | Player enters dark passage, thanks for playing, exits game | Pass | As expected |
| | Input: "torch" | Not valid enter to try again  | Pass | As expected |
| | Input: "scissors" | Not valid enter to try again  | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again  | Pass | As expected |
| | Input: "1" | Not valid enter to try again  | Pass | As expected |
| Dark Passage, torch chosen | | | | |
| | Input: "torch" | Player turns on torch illuminating the passage, thanks for playing, exits game | Pass | As expected |
| | Input: "enter" | Not valid enter to try again  | Pass | As expected |
| | Input: "scissors" | Not valid enter to try again  | Pass | As expected |
| | Input: "pizza" | Not valid enter to try again  | Pass | As expected |
| | Input: "1" | Not valid enter to try again  | Pass | As expected |

## User Story Testing

Testing user stories with screenshots to show they have been fulfilled.

| User Story | Screenshot |
| --- | --- |
| As a user, I would like to input my own name, so that I can have a more personalised experience. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/start_screen.PNG) |
| As a user, I would like to experience an interesting narrative, so that I can become immersed in the story. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/enter_yes.PNG) |
| As a user, I would like to answer ancient Egyptian based questions, so that I can have fun while testing my knowledge. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/go_to_shop_no.PNG) |
| As a user, I would like to play game against interesting enemies, so that I can have fun and learn about the lore of the game universe. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/use_rope.PNG) |
| As a user, I would like to make meaningful choices, so that I can reply the game multiple times to experience all the paths. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/yes_rope.PNG) |
| As a user, I would like to choose items, so that I explore multiple routes through the story. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/go_to_shop_yes.PNG) |
| As a user, I would like to know the score during rock, paper, scissors so that I know if I am winning or losing. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/mummy_wins_round.PNG) |
| As a user, I would like to a smooth, coherent story that makes sense and flows correctly. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/passage_enter.PNG) |
| As a user, I would like to get feedback if my inputs are incorrect, so that I know what is required to fulfil the validator. | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/invalid_name.PNG) |


## Bugs

### Bug 1 - NOT fixed!
If the rope was chosen in the shop, when the player comes to the direction 1 choice, they will able to choose left, right or rope. However when you have the rope all of the options with use the rope even if you type in left or right. 

Bug was discoverd during input & validation testing, so was not fixed.

## Cross Browser Testing

| Browser | Image |
| ------- | ----- |
| Chrome | ![Chrome test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/chrome.PNG) |
| Firefox | ![Firefox test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/firefox.PNG) |
| Edge | ![Edge test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/edge.PNG) |