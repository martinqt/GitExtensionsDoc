Submodules
==========

Remove submodule
----------------

It is currently not possible to remove a submodule using the Git Extensions user interface. To remove a submodule you need to manually:

* Delete the relevant line from the ``.gitmodules`` file.
* Delete the relevant section from ``.git/config``.
* Run ``git rm --cached path_to_submodule`` (no trailing slash).
* Commit and delete the now untracked submodule files.
