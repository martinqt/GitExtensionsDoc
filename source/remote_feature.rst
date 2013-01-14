Remote feature
==============

Git is a distributed source control management system. This means that all changes you make are local. When you commit 
changes, you only commit them to your local repository. To publish your local changes you need to push. In order to get 
changes committed by others, you need to pull.

Manage remote repositories
--------------------------

You can manage the remote repositories in the ``Remotes`` menu.

.. image:: /images/manage_remote_repositories.png

When you cloned your repository from a public repository, this remote is already configured. You can rename each remote for 
easy recognition. The default name after cloning a remote is ``origin``. If you use PuTTY as SSH client you can also enter the 
private key file for each remote. Git Extensions will load the key when needed. How to create a private key file is described 
in the next paragraph.

.. image:: /images/remote_repositories.png

In the ``Default pull behaviour`` tab you can configure the branches that need to be pulled and merged by default. If you 
configure this correctly you will not need to choose a branch when you pull or push. There are two buttons on this dialog:

+-------------------------------+---------------------------------------------------------------------+
|Prune remote branches          | Throw away remote branches that do not exist on the remote anymore. |
+-------------------------------+---------------------------------------------------------------------+
|Update all remote branch info  | Fetch all remote branch information.                                |
+-------------------------------+---------------------------------------------------------------------+

.. image:: /images/remote_repositories2.png

After cloning a repository you do not need to configure all remote branches manually. Instead you can checkout the remote 
branch and choose to create a local tracking branch. 

Create SSH key
--------------

Git uses SSH for accessing private repositories. SSH uses a public/private key pair for authentication. This means you need 
to generate a private key and a public key. The private key is stored on your computer locally and the public key can be given 
to anyone. SSH will encrypt whatever you send using your secret private key. The receiver will then use the public key you send 
to decrypt the data. 

This encryption will not protect the data itself but it protects the authenticity. Because the private key is only available to 
the sender, the receiver can be sure about the origin of the data. In practise the key pair is only used for the authentication 
process. The data itself will be encrypted using a key that is exchanged during this initial phase.

PuTTY and github
^^^^^^^^^^^^^^^^

PuTTY is SSH client that for Windows that is a bit more user friendly then OpenSSH. Unfortunately PuTTY does not work with 
all servers. In this paragraph I will show how to generate a key for github using putty.

First make sure GitExtensions is configured to use PuTTY and all paths are correct.

.. image:: /images/github_ssh.png

.. image:: /images/generate_or_import_key.png

can choose ``Generate or import key`` to start the key generator.

+--------------------------------------------+---------------------------------------------+
|.. image:: /images/putty_key_generator1.png | .. image:: /images/putty_key_generator2.png |
+--------------------------------------------+---------------------------------------------+

PuTTY will ask you to move the mouse around to generate a more random key. When the key is generated you can save the public and 
the private key in a file. You can choose to protect the private key with a password but this is not necessary. 

Now you have a key pair you need to give github the public key. This can be done in ``Account Settings`` in the tab 
``SSH Public Keys``. You can add multiple keys here, but you only need one key for all repositories.

.. image:: /images/account_settings.png

After telling github what public key to use to decrypt, you need to tell GitExtensions what private key to use to encrypt. 
In the clone dialog there is a ``Load SSH key`` button to load the private key into the PuTTY authentication agent. This can 
also be done manually by starting the PuTTY authentication agent and choose ``add key`` in the context menu in the system tray.

.. image:: /images/putty_agent.png

GitExtensions can load the private keys automatically for you when communicating with a remote. You need to configure the 
private key for the remote.

This is done in the ``Manage remote repositories`` dialog. 

OpenSSH and github
^^^^^^^^^^^^^^^^^^

Pull changes
------------

Push changes
------------

In the browse window you can check if there are local commits that are not pushed to a remote repository yet. In the image 
below the green labels mark the position of the master branch on the remote repository. The red label marks the position of 
the master branch on the local repository. The local repository is ahead three commits.

.. image:: /images/push1.png

To push the changes press ``Push`` in the toolbar. 

.. image:: /images/push_toolbar.png

The push dialog allows you to choose the remote repository to push to. The remote repository is set to the remote of the 
current branch. You can choose another remote or choose a url to push to. You can also specify a branch to push. 

.. image:: /images/push_dialog.png

Tags are not pushed to the remote repository. If you want to push a tag you need to open the ``Tags`` tab in the dialog. You 
can choose to push a singe tag or all tags. No commits will be pushed when the ``Tags`` tab is selected, only tags. 

You can not merge your changes in the remote repository. Merging must be done locally. This means that you cannot push your 
changes before the commits are merged locally. In practice you need to pull before you can push most of the times.
