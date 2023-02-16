# Testing

Return back to the [README.md](README.md) file.


## Code Validation
### Python

The recommended [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python file.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ogc1231/puzzle-pyramid/main/run.py) | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/CI_Python_Linter.PNG) | Pass: No Errors  |

### NOQA

`noqa` = **NO Quality Assurance**
- was used for the Puzzle Pyramid ASCII Art to remove errors.

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | Desktop | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/lighthouse.PNG) | All above 90 |
| run.py | Mobile | ![screenshot](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/lighthouse_mobile.PNG) | Performance 88 |


## Defensive Programming


Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery Page | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

## User Story Testing

Testing user stories is actually quite simple, once you've already got the stories defined on your README.


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

There are no known bugs have been found in this app, however this doesn't mean that there are none and some may appear in the future.

## Cross Browser Testing

| Browser | Image |
| ------- | ----- |
| Chrome | ![Chrome test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/chrome.PNG) |
| Firefox | ![Firefox test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/firefox.PNG) |
| Edge | ![Edge test](https://github.com/ogc1231/puzzle-pyramid/blob/main/documentation/testing/edge.PNG) |