<!-- omit in toc -->
# Contributing to TXT to HTML Converter

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [Setup](#setup)
  - [For Contributors](#for-contributors-)
    - [IDE Integration](#ide-integration)
  - [For Regular Users](#for-regular-users)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)


## Setup
To run TXT to HTML, make sure you are running the latest version of [Python](https://www.python.org/downloads/). 
Once installed, open the folder that the program is located in.

### For Contributors: 
Open the folder with your IDE of choice, and contribute away. 
When contributing, make sure that you leave comments explaining your code where it matters.
They don't need to be super descriptive if you're variable names and/or function names explain the logic behind what's being done. 
So even comments with a short description or simple walk through of certain steps would be appreciated. 

For code formatting, please install [Black](https://pypi.org/project/black/) to format your code, and follow their setup.
However, here is a quick overview, use `pip install black`. Then run Black on the file or directory you want to format. If you want to change how Black formats files, go to the pyproject.toml file. 
You can read more about configuring the way black formats code [here](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file).

For linting, please use [Ruff](https://docs.astral.sh/ruff/). 
**Note:** While Ruff also acts as a formatter, it will currently be used only for linting purposes.
Quick overview on how to download and use Ruff. Run `pip install ruff` on your CLI **for Windows**.
Installation for **other OSs** can be found [here](https://docs.astral.sh/ruff/installation/).
Run `ruff check <filename>` to lint the files you're working on, and it'll tell you what to fix.
There are [other arguments](https://docs.astral.sh/ruff/linter/) such as fix and watch.
Configuration works similar to Black, i.e. they use the pyproject.toml file. To learn more about configuration read [here](https://docs.astral.sh/ruff/configuration/).

#### IDE Integration
If you're using PyCharm, then Black is automatically integrated, once you download it, and can be configured by going to `Preferences or Settings -> Tools -> Black`.
From there you can enable Black to run on save and when you reformat a file (ctrl + shift + l). Ruff has an [unofficial plugin](https://plugins.jetbrains.com/plugin/20574-ruff) you can use, but it seems to be normally updated.
To download it, go to `Preferences or Settings -> Plugins` then search for Ruff. After you install the plugin, go to `Preferences or Settings -> Tools -> Ruff`. 
From there you can configure it to run when a Python file is saved or reformatted. Since we already made Black run when a file is reformatted. We'll make Ruff run only when it saves.

Ideally, this is what the settings for Black and Ruff should look like for their integration.

Black:
![img.png](Black%20formatter%20setup%20comparison.png)

Ruff:
![img.png](Ruff%20setup%20comparison.png)

### For Regular Users
If you want to use the program, and are on Windows, you can type powershell or cmd into the top bar and start the program that way. 
You can then call on the program in your terminal or command line by doing so `python txt_to_html.py filename.txt` or `python txt_to_html.py foldername`. 
**Note**: Running this program will delete the output folder, so it can be recreated with updated files.
So please make sure you are backing up any html files you may not want deleted in the specified output folder.

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://github.com/Pasqua101/txt-to-HTML-converter#readme).

Before you ask a question, it is best to search for existing [Issues](https://github.com/Pasqua101/txt-to-HTML-converter/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/Pasqua101/txt-to-HTML-converter/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

<!--
You might want to create a separate issue tag for questions and include it in this description. People should then tag their issues accordingly.

Depending on how large the project is, you may want to outsource the questioning, e.g. to Stack Overflow or Gitter. You may add additional contact and information possibilities:
- IRC
- Slack
- Gitter
- Stack Overflow tag
- Blog
- FAQ
- Roadmap
- E-Mail List
- Forum
-->

## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://github.com/Pasqua101/txt-to-HTML-converter#readme). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Pasqua101/txt-to-HTML-converterissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <>.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/Pasqua101/txt-to-HTML-converter/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

<!-- You might want to create an issue template for bugs and errors that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for TXT to HTML Converter, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/Pasqua101/txt-to-HTML-converter#readme) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Pasqua101/txt-to-HTML-converter/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Pasqua101/txt-to-HTML-converter/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most TXT to HTML Converter users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

<!-- You might want to create an issue template for enhancement suggestions that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->

### Your First Code Contribution
<!-- TODO
include Setup of env, IDE and typical getting started instructions?

-->

### Improving The Documentation
<!-- TODO
Updating, improving and correcting the documentation

-->

## Styleguides
### Commit Messages
<!-- TODO

-->

## Join The Project Team
<!-- TODO -->

<!-- omit in toc -->
## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!