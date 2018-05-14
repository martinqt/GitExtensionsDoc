Getting Started
===============

Installation
------------

The single click Git Extensions installer can be found `here <https://github.com/gitextensions/gitextensions/releases/latest>`_.

.. image:: /images/install/install1.png

    Git Extensions depends heavily on Git for Windows.

.. image:: /images/install/install3.png

.. figure:: /images/install/install4.png

    Choose the options to install.

.. figure:: /images/install/install5.png

    Choose the SSH client to use. PuTTY is the default because it has better Windows integration.

.. image:: /images/install/install6.png

Settings
--------

All settings will be verified when Git Extensions is started for the first time. If Git Extensions requires
any settings to be changed, the Settings dialog will be shown. All incorrect settings will be marked in red.
You can ask Git Extensions to try to fix the setting for you by clicking on it.
When installing Git Extensions for the first time (and you do not have Git already installed on your system),
you will normally be required to configure your username and email address.

The settings dialog can be invoked at any time by selecting ``Settings`` from the ``Tools`` menu option.

.. image:: /images/settings/settings.png

For further information see :ref:`settings`.

.. _start-page:

Start Page
----------

The start page contains the most common tasks, recently opened repositories and favourites. The left side of the start page (Common Actions
and Recent Repositories) is static. The right side of the page is where favourite repositories can be added, grouped under Category headings.

.. image:: /images/start_page.png

Recent Repositories can be moved to favourites using the repository context menu. Choose ``Move to category / New category`` to create a new category
and add the repository to it, or you can add the repository to an existing category (e.g. 'Currents' as shown below).

.. image:: /images/move_to_category.png

A context menu is available for both the category and the repositories listed underneath it.

Entries on Category context menu

+------------------+-------------------------------------------------------------------------------------------------------+
|Move Up           | Move the category (and any repositories under it) higher on the page.                                 |
+------------------+-------------------------------------------------------------------------------------------------------+
|Move Down         | Move the category (and any repositories under it) lower on the page.                                  |
+------------------+-------------------------------------------------------------------------------------------------------+
|Remove            | Remove the category (and any repositories under it) from the page. Note: Git repositories are *not*   |
|                  | physically removed either locally or remotely.                                                        |
+------------------+-------------------------------------------------------------------------------------------------------+
|Edit              | Shows the :ref:`settings-start-page` settings window where both category and repository details       |
|                  | can be modified.                                                                                      |
+------------------+-------------------------------------------------------------------------------------------------------+

Entries on repository context menu

+------------------+-------------------------------------------------------------------------------------------------------+
|Move to category  | Move the repository to a new or existing category.                                                    |
+------------------+-------------------------------------------------------------------------------------------------------+
|Move up           | Move the repository higher (within the category).                                                     |
+------------------+-------------------------------------------------------------------------------------------------------+
|Move down         | Move the repository lower (within the category).                                                      |
+------------------+-------------------------------------------------------------------------------------------------------+
|Remove            | Remove the repository from the category. Note: the repository is *not* physically removed either      |
|                  | locally or remotely.                                                                                  |
+------------------+-------------------------------------------------------------------------------------------------------+
|Edit              | Shows the :ref:`settings-start-page` settings window where both category and repository details       |
|                  | can be modified.                                                                                      |
+------------------+-------------------------------------------------------------------------------------------------------+
|Show current      | Toggles the display of the branch name next to the repository name. This identifies the currently     |
|branch            | checked out branch for the repository.                                                                |
+------------------+-------------------------------------------------------------------------------------------------------+

To open an existing repository, simply click the link to the repository under Recent Repositories or within the Categories that you have set up, or
select Open repository (from where you can select a repository to open from your local file system).

To create a new repository, one of the following options under Common Actions can be selected.

Clone repository
----------------

You can clone an existing repository using this option. It displays the following dialog.

.. image:: /images/clone.png

The repository you want to clone could be on a network share or could be a repository that is accessed through an internet
or intranet connection. Depending on the protocol (http or ssh) you might need to load a SSH key into PuTTY. You also need to specify where
the cloned repository will be created and the initial branch that is checked out. If the cloned repository contains submodules, then these
can be initialised using their default settings if required.

There are two different types of repositories you can create when making a clone. A personal repository contains the complete
history and also contains a working copy of the source tree. A central repository is used as a public repository where
developers push the changes they want to share with others to. A central repository contains the complete history but does not
have a working directory like personal repositories.

Clone SVN repository
--------------------

You can clone an existing SVN repository using this option, which creates a Git repository from the SVN repository you specify.
For further information refer to the `Pro Git book <https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git>`_.

Clone Github repository
-----------------------

This option allows you to

1) Fork a repository on GitHub so it is created in your personal space on GitHub.
2) Clone any repositories on your personal space on GitHub so that it becomes a local repository on your machine.

You can see your own personal repositories on GitHub, and also search for repositories using the ``Search for repositories`` tab.

.. image:: /images/github_clone.png

Create new repository
---------------------

When you do not want to work on an existing project, you can create your own repository using this option.

.. image:: /images/new_repository.png

Select a directory where the repository is to be created. You can choose to create a Personal repository or a Central repository.

A personal repository looks the same as a normal working directory but has a directory named ``.git`` at the root level
containing the version history. This is the most common repository.

Central repositories only contain the version history. Because a central repository has no working directory you cannot
checkout a revision in a central repository. It is also impossible to merge or pull changes in a central repository. This
repository type can be used as a public repository where developers can push changes to or pull changes from.

