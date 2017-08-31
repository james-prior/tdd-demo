tdd-demo
========

Test Driven Development (TDD) Example

Write a function in Python 3 that returns the largest factor of a number
without importing any libraries except pytest and pytest-xdist.

The following is how I did a beginning TDD demo in Python from scratch.

The order of the TDD stuff was roughly:
- (step-1) Started by creating many separate tests.
- (step-2) Created a stub function to make tests fail.
- (step-3) Put meat in the function to make all the tests pass.
That's the basics, which one repeats over and over.

Then I added some more tests and 
- (step-4) Add more tests for bad input values.
- (step-5) Change the code to make the tests pass.

## Installation

The following instructions work on Knoppix 7.7.1 live DVD.
One can boot actual media such as a DVD on an actual PC,
or boot the ISO-9660 image of the DVD in a virtual machine.
The latter is probably more practical for most people
as it allows those with various operating systems,
such as macOS, Microsoft Windows, and Linux,
to play without disturbing their host operating systems.

```
git clone https://github.com/james-prior/tdd-demo.git
tdd-demo/setup
```

## Dependencies

```
- virtualenv
- git
- Python 3 with the following packages
  - apipkg==1.4
  - execnet==1.4.1
  - pkg-resources==0.0.0
  - py==1.4.34
  - pytest==3.2.1
  - pytest-forked==0.2
  - pytest-xdist==1.20.0
- optional
  - meld
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

The following commands are handy for seeing the differences between versions.
git diff master master-without-pi
git difftool -t meld -y master master-without-pi
```

