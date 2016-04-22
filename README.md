# Fast Tweet (ftw)

### What's this?:

**In short words**: Terminal tweeting, **FTW**! :smile:.

**In long words**: A tweeting client without shiny prompts, bright letters or fireworks, just a single command for a single tweet (yeah, UNIX style![^1]).

### Includes:

- The `ftw` program.
- The `fastw` libraries:
  - `twitter`: a wrapper around the @sixohsix's `twitter` module.
  - `echo`: my custom modifications for the `print()` function.

### Dependencies:

- `twitter` from PyPI.

### Installing:

Just a `python setup.py install`.

### Running:

Simply type `ftw "tweet text"`, or `ftw "tweet text" --image /file.png` if you want to add a image.

### TODO:

Check the [TODO.md](https://github.com/feskyde/ftw/blob/master/TODO.md) file.

### Releases:

| Status | Release | Date | Download |
|--------|---------|------|----------|
| **Current** | 1.0 | 04/21/2016 | [ZIP](https://github.com/feskyde/ftw/archive/ftw-1.0.zip) |
| **Development** | 1.1 | *I don't know* | *Not available* |

### License:

**Fast Tweet** is released under the GNU General Public License version 2.

[^1]: I'm waiting for `systemd` creating a `tweetctl`/`systemd-tweet` module (**spoilers**: they will do it).
