Branches
--------

.. image:: /images/branch.png
    :align: right

Branches are used to commit changes separate from other commits. It is very common to create a branch when you 
start working on a feature and you are not sure if this feature will be finished in time for the next release. The 
image on the right illustrates a branch created on top of commit B. 

In Git branches are created very often. Creating a branch is very easy to do and it is recommended to create a branch 
very often. In fact, when you make a commit to a cloned repository you start a new branch. I will explain this in the 
pull chapter.

You can check on what branch you are working in the toolbar.

.. image:: /images/branch_name.png

Create branch
-------------

In Git Extensions there are multiple ways to create a new branch. In the image below I create a new branch from the 
context menu in the commit log. This will create a new branch on the revision that is selected.

.. image:: /images/new_branch.png

I will create a new branch called ``Refactor``. In this branch I can do whatever I want without considering others. 
In the ``Create branch`` dialog there is a checkbox you can check if you want to checkout this branch immediate after 
the branch is created.

.. image:: /images/create_branch_dialog.png

When the branch is created you will see the new branch ``Refactor`` in the commit log. If you chose to checkout this 
branch the next commit will be committed to the new branch. 

.. image:: /images/refactor_branch.png

Creating branches in Git requires only 41 bytes of space in the repository. Creating a new branch is very easy and is 
very fast. The complete work flow of Git is optimized for branching and merging.
