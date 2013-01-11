Getting Started
===============

.. index::
   single: Getting Started; Installation

Installation
------------

There is a single click installer that installs MSysGit, kdif3 and Git Extensions. The installer will detect 
if 32bit and/or 64bit versions should be installed.
The installer can be found `here <http://code.google.com/p/gitextensions/>`_.

.. figure:: /images/install/install1.png

.. figure:: /images/install/install2.png

    Git Extensions depends heavily on MSysGit. When MSysGit is not installed install this first. Kdiff3 is 
    optional, but is advised as a merge tool.

.. figure:: /images/install/install3.png

.. figure:: /images/install/install4.png

    Choose the options to install.

.. figure:: /images/install/install5.png

    Choose the SSH client to use. PuTTY is the default because it has better windows integration.

.. figure:: /images/install/install6.png

Settings
--------

All settings will be verified when Git Extensions is started for the first time. If Git Extensions requires 
any settings to be changed the settings dialog will be shown. All incorrect settings will be marked red. You 
can ask Git Extensions to try to fix the setting for you by clicking on it.

.. image:: /images/settings/checklist.png

All settings that are specific to Git Extensions will be stored in the Windows registry. The settings that 
are used by Git are stored in the configuration files of Git. The global settings are stored in a file called 
``.gitconfig`` in the user directory. The local settings are stored in the .git\config file of the repository.

.. image:: /images/settings/git.png


The 'Git' tab contains the settings needed to access git repositories. The database will be accessed using external 
tools. For Windows usually msysgit or cygwin are used. Git Extensions will try to configure these settings automatically.

+-----------------------------------------+--------------------------------------------------------------------------+
|Command to run git (git.cmd or git.exe)  | Needed for Git Extensions to run Git commands. Set the full command      |
|                                         | used to run git (msysgit or cygwin).                                     |
+-----------------------------------------+--------------------------------------------------------------------------+
|Path to Linux tools                      | A few linux tools are used by Git Extensions. When msysgit is installed, |
|                                         | these tools are located in the bin directory of msysgit.                 |
+-----------------------------------------+--------------------------------------------------------------------------+

The global configuration file used by git will be put in the home directory. On some systems the home directory is not set 
or is pointed to a network drive. Git Extensions will try to detect the optimal setting for your environment. When there is 
already a global git configuration file, this location will be used. If you need to relocate the home directory for git, 
change this setting. Otherwise leave this setting on default.

.. image:: /images/settings/git_extensions.png

The ‘Git Extension’ tab contains all settings needed for Git Extension to run properly. The path to git.cmd and git.exe can 
be set here. This is only needed when these are not in the system path.

+---------------------------------------------------+----------------------------------------------------------------------------+
|Limit number of commits that will be loaded in     | Git Extensions uses lazy loading to load the commit log. Lower this number |
|list at start-up.                                  | to increase the start-up speed. Increase the number for faster scrolling.  |
|                                                   | Turn of revision graph for optimal result!                                 |
+---------------------------------------------------+----------------------------------------------------------------------------+
|Smtp server for sending patches                    | Smtp server to use for sending patches.                                    |
+---------------------------------------------------+----------------------------------------------------------------------------+
|Show current working dir changes in revision graph | When enabled, two extra revisions are added to the revision graph. The     |
|                                                   | first shows the current working directory status. The second shows the     |
|                                                   | staged files. This option can cause slowdowns when browsing large          |
|                                                   | repositories.                                                              |
+---------------------------------------------------+----------------------------------------------------------------------------+
