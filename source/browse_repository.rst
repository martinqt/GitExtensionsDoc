Browse Repository
=================

You can browse a repository by starting Git Extensions and select the repository to open. The main window contains 
the commit log. You could also open the ‘Browse’ window from the shell extensions and from the Visual Studio IDE.

View commit log
---------------

The full commit history can be browsed. There is a graph that shows branches and merges. You can show the difference 
between two revision by selection them using ctrl-click.

.. image:: /images/commit_diff_view.png

In the context menu of the commit log you can enable or disable the revision graph. You can also choose to only show the 
current branch instead of showing all branches. The other options will be discussed later.

.. image:: /images/commit_contextual_menu.png

Search history
--------------

The history can be searched using regular expressions are basic search terms. The quick filter in the toolbar searches in 
the commit message, the author and the committer.

.. image:: /images/quick_filter.png

In the context menu of the commit log you can open the advanced filter dialog. The advanced filter dialog allows you to 
search for more specific commits. To remove the filter either remove the filter in the toolbar and press enter or remove the 
filter in the advanced filter dialog.

.. image:: /images/advance_filter_dialog.png

Singe file history
------------------

To display the single file history, right click on a file name in the ``File tree`` or in the ``Diff`` tab and select ``blame``.

.. image:: /images/context_menu_blame.png

The single file history viewer shows all revisions of a single file. You can view the content of the file in after each 
commit in the ``View`` tab.

.. image:: /images/file_history.png

You can view the difference report from the commit in the ``Diff`` tab. 

.. note::
    Added lines are marked with a ``+``, removed lines are marked with a ``–``.

.. image:: /images/file_history_diff.png
