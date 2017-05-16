.. _settings:

Settings
========

The settings dialog can be invoked at any time by selecting ``Settings`` from the ``Tools`` menu option.

.. image:: /images/settings/settings.png

The following buttons are always available on any page of the Settings dialog. Sometimes the ``Cancel``
button has no effect for the page - this will be noted on the page in the area next to the buttons.

.. list-table::
  :widths: 31 108
  :header-rows: 1
  
  * - Button 
    - Description
  * - ``OK``
    - Save any entered changes made in *any* settings page and close the Settings dialog.                                                  
  * - ``Cancel``
    - Any entered changes in *any* settings page are *not* saved. The Settings dialog is closed.                                                       
  * - ``Apply``
    - Any entered changes in *any* settings page are saved.

Settings that are specific to Git Extensions and apply globally will be stored in a file called ``GitExtensions.settings``
either in the user's application data path or with the program.
The location is dependant on the IsPortable setting in the ``GitExtensions.exe.config`` file that is with the program.
Settings that are specific to Git Extensions but apply to only the current repository will be stored in a file of the same
name, ``GitExtensions.settings``, but in either the root folder of the repository or the ``.git`` folder of the repository,
depending on whether or not they are distributed with that repository.
The settings that are used by Git are stored in the configuration files of Git. The global settings are stored in the file called
``.gitconfig`` in the user directory. The local settings are stored in the ``.git\config`` file of the repository.

.. settingspage:: Checklist

  This page is a visual overview of the minimal settings that Git Extensions requires to work properly. Any items highlighted in red should
  be configured by clicking on the highlighted item.

  This page contains the following settings and buttons.

  .. setting:: Check settings at startup
  
    Forces Git Extensions to re-check the minimal set of required settings the next time Git Extensions is started.
    If all settings are 'green' this will be automatically unchecked.

  .. settingbutton:: Save and rescan

    Saves any setting changes made and re-checks the settings to see if the minimal requirements are now met.

.. settingspage:: Git

  This page contains the settings needed to access git repositories. The repositories will be accessed using external
  tools. For Windows usually "Git for Windows" or Cygwin are used. Git Extensions will try to configure these settings automatically.

  .. settingsgroup:: Git

    .. setting:: Command used to run git (git.cmd or git.exe)
      :id: git-cmd
      
      Needed for Git Extensions to run Git commands. Set the full command used 
      to run git ("Git for Windows" or Cygwin). Use the ``Browse`` button to   
      find the executable on your file system.
      
    .. setting:: Path to Linux tools (sh). 
      :id: sh-path
      
      A few linux tools are used by Git Extensions. When Git for Windows is 
      installed, these tools are located in the bin directory of Git for    
      Windows. Use the ``Browse`` button to find the directory on your file 
      system. Leave empty when it is in the path.
      
  .. settingsgroup:: Environment

    .. settingbutton:: Change HOME
      
      This button opens a dialog where the HOME directory can be changed.

  The global configuration file used by git will be put in the HOME directory. On some systems the home directory is not set
  or is pointed to a network drive. Git Extensions will try to detect the optimal setting for your environment. When there is
  already a global git configuration file, this location will be used. If you need to relocate the home directory for git,
  click the ``Change HOME`` button to change this setting. Otherwise leave this setting as the default.

.. settingspage:: Git Extensions

  This page contains general settings for Git Extensions.

  .. settingsgroup:: Performance

    .. setting:: Show number of changed files on commit button
      :id: changes-no

      When enabled, the number of pending commits are shown on the toolbar as a figure in parentheses next to the Commit button.
      Git Extensions must be stopped and restarted to activate changes to this option.
      
    .. setting:: Show current working directory changes in revision graph
      :id: working-dir-changes
      
      When enabled, two extra revisions are added to the revision graph. 
      The first shows the current working directory status. The second shows the staged files.
      This option can cause slowdowns when browsing large repositories.
      
    .. setting:: Use FileSystemWatcher to check if index is changed
      :id: filesystemwatcher

      Using the FileSystemWatcher to check index state improves the performance in some cases.
      Turn this off if you experience refresh problems in commit log.
      
    .. setting:: Show stash count on status bar in browse window
      :id: stash-count

      When you use the stash a lot, it can be useful to show the number of stashed items on the toolbar.
      This option causes serious slowdowns in large repositories and is turned off by default.
      
    .. setting:: Check for uncommitted changes in checkout branch dialog
      :id: uncommitted-changes

      Git Extensions will not allow you to checkout a branch if you have uncommitted changes on the current branch.
      If you select this option, Git Extensions will display a dialog where you can decide 
      what to do with uncommitted changes before swapping branches.
      
    .. setting:: Limit number of commits that will be loaded in list at start-up
      :id: commits-limit

      This number specifies the maximum number of commits that Git Extensions will load when it is started.
      These commits are shown in the Commit Log window. To see more commits than are loaded,
      then this setting will need to be adjusted and Git Extensions restarted.
      
  .. settingsgroup:: Behaviour

    .. setting:: Close Process dialog when process succeeds	
      :id: close-process-dlg
    
      When a process is finished, close the process dialog automatically.
      Leave this option off if you want to see the result of processes.
      When a process has failed, the dialog will automatically remain open.
      
    .. setting:: Show console window when executing git process
      :id: show-console

      Git Extensions uses command line tools to access the git repository.
      In some environments it might be useful to see the command line dialog when a process is executed.
      An option on the command line dialog window displayed allows this setting to be turned off.
      
    .. setting:: Use patience diff algorithm
      :id: patience-diff
   
      Use the Git ‘patience diff’ algorithm instead of the default. 
      This algorithm is useful in situations where two files have diverged significantly and the default algorithm
      may become ‘misaligned’, resulting in a totally unusable conflict file.
      
    .. setting:: Include untracked files in stash	
      :id: stash-untracked
    
      If checked, when a stash is performed as a result of any action except a manual stash request,
      e.g. checking out a new branch and requesting a stash then any files not tracked by git will also be saved to the stash.
      
    .. setting:: Follow renames in file history (experimental)
      :id: follow-renames

      Try to follow file renames in the file history.
      
    .. setting:: Follow exact renames and copies only
      :id: follow-exact-renames

      Follow file renames and copies for which similarity index is 100%. That is when a file
      is renamed or copied and is commited with no changes made to its content.

    .. setting:: Open last working dir on startup
      :id: open-last-repo

      When starting Git Extensions, open the last used repository (bypassing the Start Page).
      
    .. setting:: Play Special Startup Sound
      :id: startup-sound
    
      Play a sound when starting Git Extensions. It will put you in a good moooooood!
      
    .. setting:: Default clone destination
      :id: default-clone-dst

      Git Extensions will pre-fill destination directory input with value of this setting on any form used to perform repository clone.
      
    .. setting:: Revision grid quick search timeout [ms]
      :id: quick-search-timeout

      The timeout (milliseconds) used for the quick search feature in the revision graph. 
      The quick search will be enabled when you start typing and the revision graph has the focus.
      
  .. settingsgroup:: Email settings for sending patches
    :id: patches-email

    .. setting:: SMTP server name
      :id: server-name
    
      SMTP server to use for sending patches.
      
    .. setting:: Port

      SMTP port number to use.
      
    .. setting:: Use SSL/TLS
      :id: ssl-tls

      Check this box if the SMTP server uses SSL or TLS.

.. settingspage:: Commit dialog

  This page contains settings for the Git Extensions Commit dialog.

  .. settingsgroup:: Behaviour

    .. setting:: Show errors when staging files
      :id: staging-errors
    
      If an error occurs when files are staged (in the Commit dialog),
      then the process dialog showing the results of the git command is shown if this setting is checked.
      
    .. setting:: Compose commit messages in Commit dialog 
      :id: compose-message
    
      If this is unchecked, then commit messages cannot be entered in the commit dialog.
      When the ``Commit`` button is clicked, a new editor window is opened where the commit message can be entered.
      
    .. setting:: Number of previous messages in commit dialog
      :id: prev-messages
    
      The number of commit messages, from the top of the current branch,
      that will be made available from the ``Commit message`` combo box on the Commit dialog.
      
    .. setting:: Show additional buttons in commit button area
      :id: additional-buttons

      Tick the boxes in this sub-group for any of the additional buttons that you wish
      to have available below the commit button. These buttons are considered additional 
      to basic functionality and have consequences if you should click them accidentally,
      including resetting unrecorded work.

.. settingspage:: Appearance

  This page contains settings that affect the appearance of the application.

  .. settingsgroup:: General

    .. setting:: Show relative date instead of full date
      :id: relative-date
    
      Show relative date, e.g. 2 weeks ago, instead of full date.    
      Displayed on the ``commit`` tab on the main Commit Log window. 
      
    .. setting:: Show current branch in Visual Studio
      :id: show-current-branch-vs
      
      Determines whether or not the currently checked out branch is displayed on
      the Git Extensions toolbar within Visual Studio.                          
    
    .. setting:: Auto scale user interface when high DPI is used
      :id: auto-scale
      
      Automatically resize controls and their contents according to the current system resolution of the display, measured in dots per inch (DPI).
      
    .. setting:: Truncate long filenames              
      :id: truncate-long-filenames
      
      This setting affects the display of filenames in a component of a window 
      e.g. in the Diff tab of the Commit Log window. The options that can be   
      selected are:                                                            
                                                                               
      - ``None`` - no truncation occurs; a horizontal scroll bar is used to see the whole filename.                                                    
      - ``Compact`` - no horizontal scroll bar. Filenames are truncated at both start and end to fit into the width of the display component.          
      - ``Trimstart`` - no horizontal scroll bar. Filenames are truncated at the start only.                                                            
      - ``FileNameOnly`` - the path is always removed, leaving only the name of the file, even if there is space for the path.                         
        
  .. settingsgroup:: Author images
    :id: author-images
    
    .. setting:: Get author image from gravatar.com
      :id: gravatar
      
      If checked, `gravatar <http://gravatar.com/>`_ will be accessed to      
      retrieve an image for the author of commits. This image is displayed on 
      the ``commit`` tab on the main Commit Log window.                       
    
    .. setting:: Image size
    
      The display size of the user image.
      
    .. setting:: Cache images
    
      The number of days to elapse before gravatar is checked for any changes to an authors image.
      
    .. setting:: No image service
    
      If the author has not set up their own image, then gravatar can return an image based on one of these services.
      
    .. settingbutton:: Clear image cache
      
      Clear the cached avatars.
    
  .. settingsgroup:: Fonts

    .. setting:: Code font

      Change the font used for the display of file contents.
      
    .. setting:: Application font
      :id: app-font

      Change the font used on Git Extensions windows and dialogs.
      
    .. setting:: Commit font

      Change the font used for entering a commit message in the Commit dialog.
      
  .. settingsgroup:: Language

    .. setting:: Language (restart required)
      :id: language
    
      Choose the language for the Git Extensions interface.
      
    .. setting:: Dictionary for spelling checker
      :id: dictionary

      Choose the dictionary to use for the spelling checker in the Commit dialog.    
    
.. settingspage:: Revision Links

  You can configure here how to convert parts of a revision data into clickable links. These links will be located under the commit message on the ``Commit``
  tab in the ``Related links`` section.

  .. image:: /images/settings/related_links_location.png

  The most common case is to convert an issue number given as a part of commit message into a link to the coresponding issue-tracker page.
  The screenshot below shows an example configuration for GitHub issues.

  .. image:: /images/settings/revision_links.png

  .. setting:: Categories

    Lists all the currently defined Categories. Click the ``Add`` button to   
    add a new empty Category. The default name is 'new'.  To remove a Category
    select it and click the ``Remove`` button.                                
    
  .. setting:: Name

    This is the Category name used to match the same categories defined on
    different levels of the Settings.                                     
    
  .. setting:: Enabled

    Indicates whether the Category is enabled or not. Disabled categories are  
    skipped while creating links.                                            

  .. settingsgroup:: Remote data

    It is possible to use data from remote's URL to build a link. This way, links can be defined globally for all repositories sharing the same URL schema.

    .. setting:: Use remotes
        
      Regex to filter which remotes to use. Leave blank to create links not depending on remotes.
      If full names of remotes are given then matching remotes are sorted by its position in the given Regex.
      
    .. setting:: Only use the first match
      :id: only-use-first-match
      
      Check if you want to create links only for the first matching remote.

    .. setting:: Search in
      
      Define whether to search in ``URL``, ``Push URL`` or both.

  .. settingsgroup:: Revision data
    
    .. setting:: Search in
      
      Define which parts of the revision should be searched for matches.

    .. setting:: Search pattern 
      
      Regular expression used for matching text in the chosen revision parts.        
      Each matched fragment will be used to create a new link. More than one     
      fragment can be used in a single link by using a capturing group.
      Matches from the Remote data group go before matches from the Revision data group.
      A capturing group value can be passed to a link by using zero-based indexed
      placeholders in a link format definition e.g. {0}.
      
    .. setting:: Nested pattern
      
      ``Nested pattern`` can be used when only a part of the text matched by the `Search pattern <#revision-links-revision-search-in>`_
      should be used to format a link. When the ``Nested pattern`` is empty,
      matches found by the `Search pattern <#revision-links-revision-search-in>`_ are used to create links.          

    .. setting:: Links: Caption/URI
      :id: revision-links
      
      List of links to be created from a single match. Each link consists of     
      the ``Caption`` to be displayed and the ``URI`` to be opened when the link 
      is clicked on. In addition to the standard zero-based indexed placeholders,
      the ``%COMMIT_HASH%`` placeholder can be used to put the commit's hash into
      the link. For example: ``https://github.com/gitextensions/gitextensions/commit/%COMMIT_HASH%``

.. settingspage:: Colors

  This page contains settings to define the colors used in the application.
  
  .. settingsgroup:: Revision graph
    
    .. setting:: Multicolor branches

      Displays branch commits in different colors if checked. 
      If unchecked, all branches are shown in the same color. 
      This color can be selected.
      
    .. setting:: Striped branch change
    
      When a new branch is created from an existing branch, the common part of the history is shown in a ‘hatch’ pattern.
      
    .. setting:: Draw branch borders
    
      Outlines branch commits in a black border if checked.
      
    .. setting:: Draw non relatives graph gray
      
      Show commit history in gray for branches not related to the current branch.
    
    .. setting:: Draw non relatives text gray

      Show commit text in gray for branches not related to the current branch.
      
    .. setting:: Color tag

      Color to show tags in.
      
    .. setting:: Color branch
      
      Color to show branch names in.
    
    .. setting:: Color remote branch

      Color to show remote branch names in.
    
    .. setting:: Color other label

      Color to show other labels in.
    
  .. settingsgroup:: Application Icon

    .. setting:: Icon style

      Change icons. Useful for recognising various open instances.
    
    .. setting:: Icon color

      Changes color of the selected icons.
    
  .. settingsgroup:: Difference View

    .. setting:: Color removed line

      Highlight color for lines that have been removed.
      
    .. setting:: Color added line

      Highlight color for lines that have been added.
    
    .. setting:: Color removed line highlighting

      Highlight color for characters that have been removed in lines.
    
    .. setting:: Color added line highlighting

      Highlight color for characters that have been added in lines.
    
    .. setting:: Color section

      Highlight color for a section.  
    
.. settingspage:: Start Page

  This page allows you to add/remove or modify the Categories and repositories that will appear on the Start Page when Git Extensions is
  launched. Per Category you can either configure an RSS feed or add repositories. The order of both Categories, and repositories within
  Categories, can be changed using the context menus in the Start Page. See :ref:`start-page` for further details.

  .. setting:: Categories	
  
    Lists all the currently defined Categories. Click the ``Add`` button to add a new empty Category. 
    The default name is ‘new’. To remove a Category select it and click Remove. 
    This will delete the Category and any repositories belonging to that Category.
    
  .. setting:: Caption

    This is the Category name displayed on the Start Page.
  .. setting:: Type
  
    Specify the type: an RSS feed or a repository.
    
  .. setting:: RSS Feed
  
    Enter the URL of the RSS feed.
    
  .. setting:: Path/Title/Description
    
    For each repository defined for a Category, shows the path, title and    
    description. To add a new repository, click on a blank line and type the 
    appropriate information. The contents of the Path field are shown on the 
    Start Page as a link to your repository *if* the Title field is blank. If
    the Title field is non-blank, then this text is shown as the link to your
    repository. Any text in the Description field is shown underneath the    
    repository link on the Start Page.                                       


  An RSS Feed can be useful to follow repositories on GitHub for example. See this page on GitHub: https://help.github.com/articles/about-your-profile/.
  You can also follow commits on public GitHub repositories by

  1) In your browser, navigate to the public repository on GitHub.
  2) Select the branch you are interested in.
  3) Click on the Commits tab.
  4) You will find a RSS icon next to the words "Commit History".
  5) Copy the link
  6) Paste the link into the RSS Feed field in the Settings - Start Page as shown above.

  Your Start Page will then show each commit - clicking on a link will open your browser and take you to the commit on GitHub.


.. _settings-global-settings:
.. _settings-local-settings:
.. settingspage:: Git Config

  This page contains some of the settings of Git that are used by and therefore can be changed from within Git Extensions.

  If you change a Git setting from the Git command line using ``git config`` then the same change in setting can be seen inside
  Git Extensions. If you change a Git setting from inside Git Extensions then that change can be seen using ``git config --get``.

  Git configuration can be global or local configuration. Global configuration applies to all repositories. Local configuration overrides
  the global configuration for the current repository.

  .. setting:: User name

    User name shown in commits and patches.

  .. setting:: User email

    User email shown in commits and patches.

  .. setting:: Editor

    Editor that git.exe opens (e.g. for editing commit message). 
    This is not used by Git Extensions, only when you call git.exe from the command line. 
    By default Git will use the built in editor.

  .. setting:: Mergetool

    Merge tool used to solve merge conflicts. Git Extensions will search for common merge tools on your system.

  .. setting:: Path to mergetool

    Path to merge tool. Git Extensions will search for common merge tools on your system.

  .. setting:: Mergetool command

    Command that Git uses to start the merge tool. Git Extensions will try to set this automatically when a merge tool is chosen.
    This setting can be left empty when Git supports the mergetool (e.g. kdiff3).

  .. setting:: Keep backup (.orig) after merge
    :id: keep-backup

    Check to save the state of the original file before modifying to solve merge conflicts. Refer to Git configuration setting ```mergetool.keepBackup```.

  .. setting:: Difftool

    Diff tool that is used to show differences between source files. Git Extensions will search for common diff tools on your system.

  .. setting:: Path to difftool

    The path to the diff tool. Git Extensions will search for common diff tools on your system.

  .. setting:: DiffTool command

    Command that Git uses to start the diff tool. This setting should only be filled in when Git doesn’t support the diff tool.

  .. setting:: Path to commit template

    A path to a file whose contents are used to pre-populate the commit message in the commit dialog.

  .. settingsgroup:: Line endings

    .. setting:: Checkout/commit radio buttons

      Choose how git should handle line endings when checking out and checking in files.
      Refer to https://help.github.com/articles/dealing-with-line-endings/#platform-all


  .. setting:: Files content encoding

    The default encoding for file contents.  

.. settingspage:: Build server integration

  This page allows you to configure the integration with build servers. This allows the build status of each commit
  to be displayed directly in the revision log, as well as providing a tab for direct access to the Build Server
  build report for the selected commit.

  .. settingsgroup:: General

    .. setting:: Enable build server integration

      Check to globally enable/disable the integration functionality.

    .. setting:: Show build status summary in revision log

      Check to show a summary of the build results with the commits in the main revision log.

    .. setting:: Build server type

      Select an integration target.

  .. settingsgroup:: Jenkins

    .. setting:: Jenkins server URL

      Enter the URL of the server (and port, if applicable).

    .. setting:: Project name

      Enter the name of the project which tracks this repository in Jenkins.

  .. settingsgroup:: TeamCity
  
    .. setting:: TeamCity server URL

      Enter the URL of the server (and port, if applicable).

    .. setting:: Project name

      Enter the name of the project which tracks this repository in TeamCity. Multiple project names can be entered separated by the | character.

    .. setting:: Build Id Filter

      Enter a regexp filter for which build results you want to retrieve in the case that your build project creates multiple builds. For example, if your project includes both devBuild and docBuild you may wish to apply a filter of “devBuild” to retrieve the results from only the program build.

  .. settingsgroup:: Team Foundation

    .. setting:: Tfs server (Name or URL)

      Enter the URL of the server (and port, if applicable).

    .. setting:: Team collection name

    .. setting:: Project name

      Enter the name of the project which tracks this repository in Tfs.

    .. setting:: Build definition name

      Use first found if left empty.

.. settingspage:: SSH

  This page allows you to configure the SSH client you want Git to use. Git Extensions is optimized for PuTTY. Git Extensions
  will show command line dialogs if you do not use PuTTY and user input is required (unless you have configured SSH to use authentication
  with key instead of password). Git Extensions can load SSH keys for PuTTY when needed.

  .. settingsgroup:: Specify which ssh client to use
  
    .. setting:: PuTTY

      Use PuTTY as SSH client.

    .. setting:: OpenSSH

      Use OpenSSH as SSH client.

    .. setting:: Other ssh client

      Use another SSH client. Enter the path to the SSH client you wish to use.

  .. settingsgroup:: Configure PuTTY

    .. setting:: Path to plink.exe

      Enter the path to the plink.exe executable.

    .. setting:: Path to puttygen

      Enter the path to the puttygen.exe executable.

    .. setting:: Path to pageant

      Enter the path to the pageant.exe executable.

    .. setting:: Automatically start authentication

      If an SSH key has been configured, then when accessing a remote repository the key will automatically be used by the SSH client if this is checked.

.. settingspage:: Scripts

  This page allows you to configure specific commands to run before/after Git actions or to add a new command to the User Menu.
  The top half of the page summarises all of the scripts currently defined. If a script is selected from the summary, the bottom
  half of the page will allow modifications to the script definition.

  A hotkey can also be assigned to execute a specific script. See :ref:`settings-hotkeys`.

  .. settingbutton:: Add

    Adds a new script. Complete the details in the bottom half of the screen.

  .. settingbutton:: Remove

    Removes a script.

  .. settingbutton:: Up/Down Arrows

    Changes order of scripts.

  .. setting:: Name

    The name of the script.

  .. setting:: Enabled

    If checked, the script is active and will be performed at the appropriate time (as determined by the On Event setting).

  .. setting:: Ask for confirmation

    If checked, then a popup window is displayed just before the script is run to confirm whether or not the script is to be run.
    Note that this popup is *not* displayed when the script is added as a command to the User Menu (On Event setting is ShowInUserMenuBar).

  .. setting:: Run in background

    If checked, the script will run in the background and Git Extensions will return to your control without waiting for the script to finish.

  .. setting:: Add to revision grid context menu

    If checked, the script is added to the context menu that is displayed when right-clicking on a line in the Commit Log page.

  .. setting:: Command

    Enter the command to be run. This can be any command that your system can run e.g. an executable program,
    a .bat script, a Python command, etc. Use the ``Browse`` button to find the command to run.

  .. setting:: Arguments

    Enter any arguments to be passed to the command that is run. 
    The ``Help`` button displays items that will be resolved by Git Extensions before 
    executing the command e.g. {cBranch} will resolve to the currently checked out branch, 
    {UserInput} will display a popup where you can enter data to be passed to the command when it is run.

  .. setting:: On Event

    Select when this command will be executed, either before/after certain Git commands, or displayed on the User Menu bar.

.. settingspage:: Hotkeys

  This page allows you to define keyboard shortcuts to actions when specific pages of Git Extensions are displayed.
  The HotKeyable Items identifies a page within Git Extensions. Selecting a Hotkeyable Item displays the list of
  commands on that page that can have a hotkey associated with them.

  The Hotkeyable Items consist of the following pages

  1) Commit: the page displayed when a Commit is requested via the ``Commit`` User Menu button or the ``Commands/Commit`` menu option.
  2) Browse: the Commit Log page (the page displayed after a repository is selected from the Start Page).
  3) RevisionGrid: the list of commits on the Commit Log page.
  4) FileViewer: the page displayed when viewing the contents of a file.
  5) FormMergeConflicts: the page displayed when merge conflicts are detected that need correcting.
  6) Scripts: shows scripts defined in Git Extensions and allows shortcuts to be assigned. Refer :ref:`settings-scripts`.

  .. setting:: Hotkey

    After selecting a Hotkeyable Item and the Command, the current keyboard shortcut associated with the command is displayed here.
    To alter this shortcut, click in the box where the current hotkey is shown and press the new keyboard combination.

  .. settingbutton:: Apply

    Click to apply the new keyboard combination to the currently selected Command.

  .. settingbutton:: Clear

    Sets the keyboard shortcut for the currently selected Command to 'None'.

  .. settingbutton:: Reset all Hotkeys to defaults

    Resets all keyboard shortcuts to the defaults (i.e. the values when Git Extensions was first installed).

.. settingspage:: Shell Extension

  When installed, Git Extensions adds items to the context menu when a file/folder is right-clicked within Windows Explorer. One of these items
  is ``Git Extensions`` from which a further (cascaded) menu can be opened. This settings page determines which items will appear on that cascaded
  menu and which will appear in the main context menu. Items that are checked will appear in the cascaded menu.

  To the right side of the list of check boxes is a preview that shows you how the Git Extensions menu items will be arranged with
  your current choices.

  By default, what is displayed in the context menu also depends on what item is right-clicked in Windows Explorer; a file or a folder
  (and whether the folder is a Git repository or not). If you want Git Extensions to always include all of its context menu items,
  check the box ``Always show all commands``.

.. settingspage:: Advanced

  This page allows advanced settings to be modified. Clicking on the '+' symbol on the tree of settings will display further settings.
  Refer :ref:`settings-confirmations`.

  .. settingsgroup:: Checkout

    .. setting:: Always show checkout dialog
    
      Always show the Checkout Branch dialog when swapping branches.
      This dialog is normally only shown when uncommitted changes exist on the current branch
          
    .. setting:: Use last chosen "local changes" action as default action.
      :id: local-changes
      
      This setting works in conjunction with the 'Git Extensions/Check for uncommitted changes in checkout branch dialog' setting. 
      If the 'Check for uncommitted changes' setting is checked, then the Checkout Branch dialog is shown only if this setting is unchecked.
      If this setting is checked, then no dialog is shown and the last chosen action is used.
          
  .. settingsgroup:: General
    
    .. setting:: Don’t show help images
    
      In the Pull, Merge and Rebase dialogs, images are displayed by default to explain what happens 
      with the branches and their commits and the meaning of LOCAL, BASE and REMOTE (for resolving merge conflicts)
      in different merge or rebase scenarios. If checked, these Help images will not be displayed.
          
    .. setting:: Always show advanced options
    
      In the Push, Merge and Rebase dialogs, advanced options are hidden by default and shown only after you click a link or checkbox. 
      If this setting is checked then these options are always shown on those dialogs.
          
    .. setting:: Remember the ignore-white-space preference
    
      If checked, the diff views will be able to remember the ignore-white-spaces preference.
          
.. settingspage:: Confirmations

  This page allows you to turn off certain confirmation popup windows.
  
  .. settingsgroup:: Don’t ask to confirm to
    
    .. setting:: Amend last commit
    
      If checked, do not display the popup warning about 
      the rewriting of history when you have elected to amend the last committed change.
          
    .. setting:: Apply stashed changes after successful pull

      In the Pull dialog, if ``Auto stash`` is checked, then any changes will be stashed before the pull is performed.
      Any stashed changes are then re-applied after the pull is complete. 
      If this setting is checked, the stashed changes are applied with no confirmation popup.

    .. setting:: Apply stashed changes after successful checkout
    
      In the Checkout Branch dialog, if ``Stash`` is checked, then any changes will be stashed before the branch is checked out.
      If this setting is checked, then the stashed changes will be automatically re-applied
      after successful checkout of the branch with no confirmation popup.
          
    .. setting:: Add a tracking reference for newly pushed branch
    
      When you push a local branch to a remote and it doesn’t have a tracking reference,
      you are asked to confirm whether you want to add such a reference. If this setting is checked,
      a tracking reference will always be added if it does not exist.
          
    .. setting:: Push a new branch for the remote
    
      When pushing a new branch that does not exist on the remote repository, 
      a confirmation popup will normally be displayed. If this setting is checked, 
      then the new branch will be pushed with no confirmation popup.
          
    .. setting:: Update submodules on checkout
    
      When you check out a branch from a repository that has submodules,
      you will be asked to update the submodules. If this setting is checked,
      the submodules will be updated without asking.  
          
.. settingspage:: Plugins

  Plugins provide extra functionality for Git Extensions.

  .. settingspage:: Auto compile SubModules
  
    This plugin proposes (confirmation required) that you automatically build submodules after they are updated via the GitExtensions Update submodules command.
    
    .. setting:: Enabled
    
      Enter true to enable the plugin, or false to disable.

    .. setting:: Path to msbuild.exe
      
      Enter the path to the msbuild.exe executable.

    .. setting:: msbuild.exe arguments
      
      Enter any arguments to msbuild.

  .. settingspage:: Periodic background fetch
  
    	This plugin keeps your remote tracking branches up-to-date automatically by fetching periodically.
    
    .. setting:: Arguments of git command to run

      Enter the git command and its arguments into the edit box. 
      The default command is ``fetch --all``, which will fetch all branches from all remotes.
      You can modify the command if you would prefer, for example, to fetch only a specific remote, e.g. ``fetch upstream``.

    .. setting:: Fetch every (seconds)

      Enter the number of seconds to wait between each fetch. Enter 0 to disable this plugin.

    .. setting:: Refresh view after fetch

      If checked, the commit log and branch labels will be refreshed after the fetch. 
      If you are browsing the commit log and comparing revisions you may wish 
      to disable the refresh to avoid unexpected changes to the commit log.

    .. setting:: Fetch all submodules

      If checked, also perform ``git fetch –all`` recursively on all configured
      submodules as part of the periodic background fetch.

  .. settingspage:: Create local tracking branches

    This plugin will create local tracking branches for all branches on a remote repository.
    The remote repository is specified when the plugin is run.
    
  .. settingspage:: Delete obsolete branches
  
    This plugin allows you to delete obsolete branches i.e. those branches 
    that are fully merged to another branch. 
    It will display a list of obsolete branches for review before deletion.
    
    .. setting:: Delete obsolete branches older than (days)

      Select branches created greater than the specified number of days ago.

    .. setting:: Branch where all branches should be merged

      The name of the branch where a branch must have been merged into to be considered obsolete.

  .. settingspage:: Find large files
  
    Finds large files in the repository and allows you to delete them.
    
    .. setting:: Find large files bigger than (Mb)

      Specify what size is considered a 'large' file.

  .. settingspage:: Gerrit Code Review

    The Gerrit plugin provides integration with Gerrit for GitExtensions.
    This plugin has been based on the git-review tool.

    For more information see: https://www.gerritcodereview.com/

  .. settingspage:: GitFlow

    The GitFlow plugin provides high-level repository operations for Vincent Driessen’s branching model

    For more information see: https://github.com/nvie/gitflow

  .. settingspage:: Github

    This plugin will create an OAuth token so that some common GitHub actions can be integrated with Git Extensions.

    For more information see: https://github.com/

    .. setting:: OAuth Token

      The token generated and retrieved from GitHub.

  .. settingspage:: Impact Graph
  
    This plugin shows in a graphical format the number of commits and counts of changed
    lines in the repository performed by each person who has committed a change.
    
  .. settingspage:: Statistics
  
    This plugin provides various statistics (and a pie chart) about the current Git repository.
    For example, number of commits by author, lines of code per language.
    
    .. setting:: Code files

      Specifies extensions of files that are considered code files.

    .. setting:: Directories to ignore (EndsWith)

      Ignore these directories when calculating statistics.

    .. setting:: Ignore submodules

      Ignore submodules when calculating statistics (true/false).

  .. settingspage:: Gource	

    Gource is a software version control visualization tool.

    For more information see: http://gource.io/

    .. setting:: Path to "gource"

      Enter the path to the gource software.

    .. setting:: Arguments

      Enter any arguments to gource.

  .. settingspage:: Proxy Switcher
  
    This plugin can set/unset the value for the http.proxy git config file key as per the settings entered here.

    .. setting:: Username

      The user name needed to access the proxy.

    .. setting:: Password

      The password attached to the username.

    .. setting:: HttpProxy

      Proxy Server URL.

    .. setting:: HttpProxyPort

      Proxy Server port number.

  .. settingspage:: Release Notes Generator
  
    This plugin will generate 'release notes'.
    This involves summarising all commits between the specified from and to commit expressions
    when the plugin is started. This output can be copied to the clipboard in various formats.
    
  .. settingspage:: Create Stash Pull Request

    If your repository is hosted on Atlassian Bitbucket Server (Stash)
    then this plugin will enable you to create a pull request for Stash from Git Extensions

    For more information see: https://www.atlassian.com/software/bitbucket/server

    .. setting:: Stash Username

      The username required to access Stash.

    .. setting:: Stash Password

      The password required to access Stash.

    .. setting:: Specify the base URL to Stash

      The URL from which you will access Stash.

    .. setting:: Disable SSL verification

      Check this option if you do not require SSL verification to access Bitbucket Server (Stash).
      