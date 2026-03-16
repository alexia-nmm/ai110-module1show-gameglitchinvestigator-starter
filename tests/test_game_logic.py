from logic_utils import check_guess

# --- existing tests (fixed: check_guess returns a tuple) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: reversed hint messages ---
# Before the fix, "Go HIGHER!" was shown when guess was too high (wrong direction),
# and "Go LOWER!" was shown when guess was too low (also wrong direction).

def test_too_high_message_says_lower():
    # Guess is above the secret — player should be told to go LOWER
    _, message = check_guess(80, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: '{message}'"

def test_too_low_message_says_higher():
    # Guess is below the secret — player should be told to go HIGHER
    _, message = check_guess(20, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: '{message}'"

def test_too_high_message_does_not_say_higher():
    # Regression: the old bug was returning "Go HIGHER!" when guess > secret
    _, message = check_guess(80, 50)
    assert "HIGHER" not in message, f"Bug regressed: got 'HIGHER' when guess was too high"

def test_too_low_message_does_not_say_lower():
    # Regression: the old bug was returning "Go LOWER!" when guess < secret
    _, message = check_guess(20, 50)
    assert "LOWER" not in message, f"Bug regressed: got 'LOWER' when guess was too low"
