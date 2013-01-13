Commit
======

A commit is a set of changes with some extra information. Every commit contains the follow information:

* Changes
* Committer name and email
* Commit date
* Commit message
* Cryptographically strong SHA1 hash

Each commit creates a new revision of the source. Revisions are not tracked per file; each change creates a new 
revision of the complete source. Unlike most traditional source control management systems, revisions are not named 
using a revision number. Each revision is named using a SHA1, a 41 long characters cryptographically strong hash. 

Commit changes
--------------

Changes can be committed to the local repository. Unlike most other source control management systems you do not need to 
checkout files before you start editing. You can just start editing files, and review all the changes you made in the commit 
dialog later. When you open de commit dialog, all changes are listed in the top-left. 

.. image:: /images/commit_dialog.png

There are three kinds of changes:

+----------+----------------------------------------------------------------------------------------------------------------+
|Untracked | This file is not yet tracked by Git. This is probably a new file, or a file that has not been committed to Git |
|          | before.                                                                                                        |
+----------+----------------------------------------------------------------------------------------------------------------+
|Modified  | This file is modified since the last commit.                                                                   |
+----------+----------------------------------------------------------------------------------------------------------------+
|Deleted   | This file has been deleted.                                                                                    |
+----------+----------------------------------------------------------------------------------------------------------------+

When you rename or move a file Git will notice that this file has been moved, but currently Git Extensions does not show 
this in the commit dialog. Occasionally you will need to undo the file change. This can be done in the context menu of any 
unstaged file.

.. image:: /images/reset_changes.png

During your initial commit there are probably lots of files you do not want to be tracked. You can ignore these files by not 
staging them, but they will show every time. You could also add them to the .gitignore file of you repository. Files that are 
in the ``.gitignore`` file will not show up in the commit dialog again. You can open the ``.gitignore`` editor from the menu 
``Working dir changes``.

.. image:: /images/show_untracked.png

You need to stage the changes you want to commit by pressing the ‘Stage selected files’ button. You also need to stage deleted 
files because you stage the change and not the file. When all the changes you want to commit are staged, enter a commit message 
and press the commit button.

.. image:: /images/commit_dialog_commit.png

It is also possible to add files to you last commit using the ``Amend to last commit`` button. This can be very useful when you 
forgot some changes. This function rewrites history; it deletes the last commit and commits it again including the added 
changes. Make sure you only use ‘Amend to last commit’ when the commit is not yet published to other developers.

There is a build in spelling checker that checks the commit message. Incorrect spelled words are underlined with a red wave line. 
By right-clicking on the misspelled word you can choose the correct spelling or one of the other options.

.. image:: /images/commit_dialog_spellchecker.png

Git Extensions installs a number of dictionaries by default. You can choose another language in the context menu of the 
spelling checker or in the settings dialog. To add a new spelling dictionary add the dictionary file to the ``Dictionaries`` 
folder inside the Git Extensions installation folder.

.. image:: /images/commit_dialog_language.png

Cherry pick commit
------------------

Revert commit
-------------

Stash changes
-------------
