# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The interface of the game ran correctly, however, I noticed that the game gave the wrong hit, instead it should be reversed. I also noticed that pressing new game does not reset the game, but the secret number does change. Overall, the game has other bugs bt these two are the main ones I noticed.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI tool used was Claude Code 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An example of a corrected suggestion was the reversed hint bug, Claude identified that check_guess returned "Go HIGHER!" when guess > secret and "Go LOWER!" when guess < secret and I verified it by running the app and confirming the hints were backwards, then fixed it and tested with pytest.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I found the new game bug, Claude suggested resetting score, history, and changing attempts to 1 in addition to status. I decided to only reset the status= "playing" since that is the only fix needed. The other esets were optional cleanup, not a required fix. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the app manually in trhe browser and the pytests too. For the hint bug, even though the pytests were passed, I ran the app and discovered the fix wasnt fully working. The tests only covered the normal path, not the TypeError fallback path.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  python -m pytest tests/test_game_logic.py -v — it showed all 7 tests passing, which confirmed the check_guess function returned correct outcomes and messages. But the manual app test revealed a second code path (the except TypeError branch) that the pytest tests didn't cover, which was still broken.
- Did AI help you design or understand any tests? How?
Yes, Claude pointed out that the existing 3 tests were broken because they compared against a plain string ("Win") but check_guess returns a tuple ("Win", "🎉 Correct!"). Claude also wrote 4 new tests specifically targeting the reversed hint bug, including regression tests that would catch the bug if it came back. However, those tests still missed the TypeError branch which I found through manual testung not Ai suggested tests.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Streamlit re-runs the entire app.py script from top to bottom on every interaction every button click, every keystroke. Without a guard, random.randint() runs again each time, producing a new number. The fix was wrapping it in if "secret" not in st.session_state, so it only generates a number the very first run, then skips it every rerun after.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine every time you click a button on a webpage, the server throws away all your code and runs it again from scratch. 
- What change did you make that finally gave the game a stable secret number?
In lines 95-95 in app.py: 
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
The first run "secret" doesn't exist yet so it generates one and saves it. Every rerun after that, the condition is False and the line is skipped. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One strategy I would reuse is to always verify a fix by running the app manually not just by running tests. Something I would do differently is before accepting an AI suggestion I need to ask "what is this actually fixing and is that the minimum change needed?" this project had a clear example where AI suggested resetting 4 things wgen only 1 was broken. Overall, this project shows how AI can generate code syntactically perfect and logically wrong at the same time, so we gotta make sure to read and understand the code so we can catch those errors. 
