# ftw

### What's this?:

**In short words**: Terminal tweeting, **ftw**! :smile:.

**In long words**: A Python 3 based tweeting client without shiny prompts, bright letters or fireworks, just a single command for a single tweet (yeah, UNIX style!<sup>[1](#footnotes-1)</sup>).

### Dependencies:

#### From PyPI:

- `twitter`.
- `pyshorteners`.

### Includes:

- The `pyftw` modules:
  - `twitter`: a twitter wrapper around the @sixosix API for Python.
  - `oauth`: a wrapper around the Twitter API OAuth module.
  - `program`: the program data.
  - `shortener`: a WIP wrapper for `pyshorteners`.
  - `printer`: my custom modifications for `print()` function.
- The `ftw.py` program.
- The `setup.py` script.

#### And those things:

- A `MANIFEST` file for pulling the `README` in the building.
- A `TODO` file.
- GIT-related files.
- The GPL version 2 license.
- This `README`.

### Installing:

Just a `python3 setup.py install`.

### Running:

Simply type `ftw "tweet text"`, or `ftw "tweet text" -i file.png` if you want to add a image.

Since v1.1 you can add from 1 to 4 images<sup>[2](#footnotes-2)</sup>, how? Simply type `ftw "tweet text" -i file1.png file2.png file3.jpg`...

### TODO:

Check the [TODO.md](https://github.com/feskyde/ftw/blob/master/TODO.md) file.

### Releases:

| Status | Release | Codename | Date | Release Notes | Changelog | Download |
|--------|---------|----------|------|---------------|-----------|----------|
| **Current** | 1.1 | "Albatross" | 04/29/2016 | [HERE](https://github.com/feskyde/ftw/releases/tag/v1.1) | [HERE](https://github.com/feskyde/ftw/compare/v1.1...v1.2) | [ZIP](https://github.com/feskyde/ftw/archive/ftw-1.1.zip) / [EXE](https://www.youtube.com/watch?v=oHg5SJYRHA0 "Click this without doubts, you will not get rickroll'd :)") |
| **Development** | 1.2 | "Albatross" | *I don't know* | *What?* | I have [THIS](https://github.com/feskyde/ftw/compare/v1.1...master) | *Not available* |

### License:

**FTW** is released under the GNU General Public License version 2.

#### Footnotes<sup>[3](#footnotes-3)</sup>:

<a name="footnotes-1">1</a>: I'm waiting for the `systemd` people creating a `systemd-tweet` module (**SPOILER ALERT:** they will do it).

<a name="footnotes-2">2</a>: Thanks to some ugly lines of code.

<a name="footnotes-3">3</a>: Made in the derpest way possible 'cause my dear GitHub friends does not support them.
