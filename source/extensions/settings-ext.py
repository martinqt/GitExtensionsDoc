# -*- coding: utf-8 -*-
"""
    settings directives
    ~~~~~~~~~~~~~~~~~~~

    Handlers for directives used to describe settings.

"""

import re

from docutils import nodes
from docutils.parsers.rst import Directive, directives, roles

from sphinx import addnodes

class SettingBaseDirective(Directive):

    option_spec = {'id': directives.unchanged}
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def compute_target_id(self):
        """
          returns absolut anchor id for this directive
        """
        
        if 'id' in self.options:
            targetid = self.options['id']
        else:
            targetid = nodes.make_id(self.arguments[0].lower())
            
        if 'setting_group' in self.env.temp_data:
            targetid = self.env.temp_data['setting_group'][-1] + '-' + targetid

        return targetid
        
    def add_label(self, targetid, label):

        labels = self.env.domaindata['std']['labels']
        anonlabels = self.env.domaindata['std']['anonlabels']
        docname = self.env.docname
        labelid = 'settings-' + targetid
        
        anonlabels[labelid] = docname, targetid
        labels[labelid] = docname, targetid, label

class SettingsPage(SettingBaseDirective):        

    objtype = 'settingpage'          # type: unicode

    def run(self):
        # type: () -> List[nodes.Node]
        """
        """
        self.env = self.state.document.settings.env  # type: BuildEnvironment
        if 'setting_group' in self.env.temp_data:
            del self.env.temp_data['setting_group']

        targetid = self.compute_target_id()
        caption = self.arguments[0]

        node = nodes.section()
        node.document = self.state.document
        node['ids']=[targetid]
        node['names']=[caption]
        # 'desctype' is a backwards compatible attribute
        node['objtype'] = node['desctype'] = self.objtype

        titlenode = nodes.title(targetid, caption)
        node += titlenode
        self.add_label(targetid, caption)
        self.env.temp_data['setting_group'] = [targetid]
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]        

        
class SettingDescription(SettingBaseDirective):
    """
    Directive to describe a setting.
    """

    # types of doc fields that this directive handles, see sphinx.util.docfields
    objtype = 'setting'          # type: unicode

    def run(self):
        # type: () -> List[nodes.Node]
        """
        """
        self.env = self.state.document.settings.env  # type: BuildEnvironment

        node = addnodes.desc()
        node.document = self.state.document
        # 'desctype' is a backwards compatible attribute
        node['objtype'] = node['desctype'] = self.objtype

        targetid = self.compute_target_id()
        caption = self.arguments[0]
        signode = addnodes.desc_signature(targetid, '')
        targetnode = nodes.target('', '', ids=[targetid], names=[caption])
        signode += targetnode 
        signode += addnodes.desc_name(caption, caption)
        node.append(signode)        
        contentnode = addnodes.desc_content()
        node.append(contentnode)
        self.add_label(targetid, caption)
        if not 'setting_group' in self.env.temp_data:
            self.env.temp_data['setting_group'] = []
        self.env.temp_data['setting_group'].append(targetid)
        self.state.nested_parse(self.content, self.content_offset, contentnode)
        self.env.temp_data['setting_group'].pop()
        return [node]        

        
class SettingsGroup(SettingDescription):
    """
    Directive to describe a setting group.
    """
    
    objtype = 'settinggroup'          # type: unicode

class SettingButton(SettingDescription):
    """
    Directive to describe a setting button.
    """
    
    objtype = 'settingbutton'          # type: unicode

    
def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    directives.register_directive('setting', SettingDescription)
    directives.register_directive('settingsgroup', SettingsGroup)
    directives.register_directive('settingspage', SettingsPage)
    directives.register_directive('settingbutton', SettingButton)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': False,
    }