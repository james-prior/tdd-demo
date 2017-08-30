tdd-demo
========

Test Driven Development (TDD) Example

Write a function in Python 3 that returns the largest factor of a number
without importing any libraries except pytest and pytest-xdist.

The following is how I did a beginning TDD demo in Python from scratch.

The order of the TDD stuff was roughly:
- (step1) Started by creating many separate tests.
- (step2) Created a stub function to make tests fail.
- (step3) Put meat in the function to make all the tests pass.
- (step4) Refactored the function.

## Dependencies

```
git
Python 3 with the following packages
- apipkg==1.4
- execnet==1.4.1
- pkg-resources==0.0.0
- py==1.4.34
- pytest==3.2.1
- pytest-forked==0.2
- pytest-xdist==1.20.0
```

## Setup

```
# Use three terminal emulators.

# in terminal emulator 0:
virtualenv env -p `which python3`
source env/bin/activate
pip freeze >requirements.original
pip install pytest
pip install pytest-xdist
pip freeze >requirements.txt
git init
git ci --allow-empty -m 'Start with empty commit.'

# in terminal emulator 1:
# This pane shows results of tests that are run each time a file is changed.
source env/bin/activate
py.test -f .

# in terminal emulator 2:
watch 'git status'

# in terminal emulator 0:
# Now do a mix of vi, git add, git commit, and git status commands.
```
