# Fast Tweet (ftw)

### What's this?:

**In short words**: Terminal tweeting, **FTW**! :smile:.

**In long words**: A tweeting client without shiny prompts, bright letters or fireworks, just a single command for a single tweet (yeah, UNIX style!<sup>[2](#footnotes-2)</sup>).

### Includes:

- The `ftw` program.
- The `pyftw` libraries:
  - `twitter`: a wrapper around the [@sixohsix's `twitter` module](https://github.com/sixohsix/twitter).
  - `echo`: my custom modifications for the `print()` function.
  - `common`: those functions that doesn't use the `twitter` module or anything and I will use a lot.

### Dependencies:

- `twitter` from PyPI.

### Installing:

Just a `python setup.py install`.

### Running:

Simply type `ftw "tweet text"`, or `ftw "tweet text" -i file.png` if you want to add a image.

Since v1.1 you can add from 1 to 4 images<sup>[3](#footnotes-3)</sup>, how? Simply type `ftw "tweet text" -i file1.png file2.png file3.jpg`...

### TODO:

Check the [TODO.md](https://github.com/feskyde/ftw/blob/master/TODO.md) file.

### Releases:

| Status | Release | Codename | Date | Download |
|--------|---------|----------|------|----------|
| **Current** | 1.1 | "Albatross" | 04/29/2016 | [ZIP](https://github.com/feskyde/ftw/archive/ftw-1.1.zip) |
| **Development** | *Numbers...* | "Utopic Unicorn" or whatever<sup>[4](#footnotes-4)</sup> | *I don't know* | *Not available* |

### License:

**Fast Tweet** is released under the GNU General Public License version 2.

#### Footnotes<sup>[1](#footnotes-1)</sup>:

<a name="footnotes-1">1</a>: Made in the derpest way possible 'cause my dear GitHub friends does not support them.

<a name="footnotes-2">2</a>: I'm waiting for the `systemd` people creating a `systemd-tweet` module (**SPOILER ALERT**: they will do it).

<a name="footnotes-3">3</a>: Thanks to some ugly lines of code :smile:.

<a name="footnotes-4">4</a>: Not really, ugly codenames belongs only to Canonical Ltd.
