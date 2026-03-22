## 1. What was broken when you started?

The game ran successfully, but I noticed several issues when I started playing. The interface worked, but the behavior of the game was inconsistent and sometimes incorrect.

Bug 1:
Expected: The secret number should always be between 1 and 100.
Actual: The game generated a secret number outside the range (for example, -15), which breaks the game rules.

Bug 2:
Expected: The hints should correctly tell me if my guess is too high or too low.
Actual: Sometimes the hints did not match the guess and seemed incorrect or confusing.

Bug 3:
Expected: The attempts counter should decrease correctly with each guess.
Actual: The attempts did not always behave as expected and could be inconsistent and give me the secreat number while i have one more chance .

## 2. How did you use AI as a teammate?

I used Claude as my AI assistant to guide me through the debugging process and help me understand what steps to take. It helped me set up the project.

One correct suggestion from AI was helping me run the Streamlit app and install the required dependencies. I verified this by successfully launching the game in my browser.

One incorrect or less helpful suggestion was when AI gave very general advice about debugging without focusing on the exact issue. I verified this by testing the game myself and finding the actual bugs through playing the game.

## 3. Debugging and testing your fixes

I decided whether a bug was fixed by running the game again and checking if the behavior changed. I tested the game manually by entering different guesses and observing how the hints and attempts responded.

One test I ran was entering multiple guesses to see if the attempts counter decreased correctly and if the hints matched my guesses. This helped me understand whether the logic was working properly.

AI helped me understand how to test the game step-by-step, but I verified everything by running the game myself.

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script every time the user interacts with the app, such as clicking a button or entering input. Because of this, you need to use session state to keep track of important values like the secret number or attempts.

I would explain it to a friend like this: Streamlit refreshes the app every time you do something, so session state is used to remember things between those refreshes.

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing my code step-by-step instead of assuming it works. Playing the game and observing behavior helped me find real bugs.

Next time, I would be more specific when asking AI for help so I can get more accurate suggestions.

This project showed me that AI-generated code is not always correct, and I need to carefully test and verify everything instead of trusting it blindly.