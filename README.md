tdd-demo
========

Test Driven Development (TDD) Demo

This repo has the files for demonstrating
[Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development).
Test Driven Development is a process. It is often abbreviated TDD.
This repo has the files, but not the explanation of how and why
TDD works. That explanation, that narrative, is saved for live
presentations.

## prerequisites

You will need to know

- how to create and use virtual machines
- how to use bash
- how to use git
- how to use an editor
- how to use live DVDs

## the process

The TDD process is roughly as follows.

1. Add a test.
2. Run all tests and see if the new tests fails. (The new tests must fail).
3. Write the code to fail the tests and run all tests. The tests
   must fail. If the tests do not fail, then either the test
   code, the code to test, or both are bad.
4. Write the code to pass the tests, then run all tests.
   The tests should all pass, now. If they do not all pass, then
   debug and fix the code, the tests, or both, until all the
   tests pass. (If one changes the tests, one should probably go
   back to step 3)
5. Refactor code.
6. Repeat steps 4 through 5 or 1 through 5.

This demo uses the example of writing a function in Python that returns the
largest factor of a number. It avoids importing any libraries except pytest and
pytest-xdist. This repo has files at various stages of the TDD process.

Some of the numbers of the steps above match those of the git tags below,
and some of the numbers of the steps above do _not_ match those of the git tags
below.

step-0, step-1, step-2, step-3, step-4, and step-5
are names of git tags of various versions of the files.

The order of the TDD stuff was roughly:
- (step-0 tag) Begin with no code.

    py.test is running, but there are no tests to run
    so py.test says that there is nothing to do.

- (step-1 tag) Create tests.

    py.test finds the tests and runs them.

    The tests fail because the code to test does not exist and so
    fails when the test code tries to import the code to test.

- (step-2 tag) Created a stub function that deliberately fails tests.

    py.test find the tests and the code to test and runs the
    tests.
    
    The tests fail because the code to test deliberately does
    what is necessary to fail the tests.
    
    For many beginners, it is counter-intuitive that one would
    deliberately fail the tests. The point of this is so that
    when one writes code to pass the tests in the next step, and
    the tests pass, one knows that it is because of the changes
    one made, and not because of bugs in the tests themselves.

    In other words, the point of writing code to fail the tests
    is to avoid future false positive test results.
    More succinctly, the point is to test the tests.

- (step-3 tag) Write code to make all tests pass.

    Since the tests were failing in the previous step, one knows
    that passing results are due to the changes in the code.

Those are the basics, which one repeats over and over. 
Then I added some more tests.
- (step-4 tag) Add more tests for bad input values.
- (step-5 tag) Change the code to make the tests pass.

One of the subtleties of TDD is how big or small each change is.
When things are going well, larger changes is OK. When progress
is tough, make small changes.

## installation

The following instructions work on Knoppix 7.7.1 live DVD.
One can boot actual media such as a DVD on an actual PC,
or boot the ISO-9660 image of the DVD in a virtual machine.
See footnote.

```
git clone https://github.com/james-prior/tdd-demo.git
tdd-demo/setup-everything
```

## exploration

tdd-demo/setup-everything above will create three terminal windows,
"testing", "git status", and "explore".
Move the windows so that they do not overlap.

- "testing" window shows output of pytest.
  The tests run automatically each time a file is changed.
- "git status" window shows output of git status
- "explore" window
  This is the window you will type commands in.
  Do a mix of vi and git commands

  ```
  git checkout step-0 ;# Watch no tests run.
  git checkout step-1 ;# Watch tests fail in "testing" window.
  git checkout step-2 ;# Watch tests fail in "testing" window.
  git checkout step-3 ;# Watch tests pass in "testing" window.
  git checkout step-4 ;# Watch tests fail in "testing" window.
  git checkout step-3 ;# Watch tests pass in "testing" window.
  ```

  The following commands are handy for seeing the differences between versions.
  The gy program shows the differences graphically.

  ```
  git diff step-1 step-2
  gy step-1 step-2
  ```

To learn how to install everything,
study tdd-demo/setup-everything and the scripts that it uses.

## dependencies

```
- git
- Python 3 with the following packages
  - apipkg==1.4
  - execnet==1.5.0
  - pkg-resources==0.0.0
  - py==1.4.34
  - pytest==3.2.3
  - pytest-forked==0.2
  - pytest-xdist==1.20.1
- venv module for Python 3
- optional
  - meld
```

## footnote

There are many little differences between different operating systems
for setting everything up. It is very difficult for beginners to resolve those
differences, so one particular operating system was chosen so that the setup
could be automated, so that beginners can be successful.

Knoppix 7.7.1 was chosen because it is the granddaddy of live media Linux
distributions. It can be booted directly on a PC,
or run in a virtual machine on many different computers.
The latter is probably more practical for most people as it allows those with
various operating systems, such as macOS, Microsoft Windows, and Linux, to play
without disturbing their host operating systems.
Explaining how to create and use virtual machines is beyond the scope of these
instructions.
