import sublime, sublime_plugin, re, string, sys, os
sys.path.insert(0, os.path.dirname(sys.executable))
import unicodedata

def strip_accents(s):
  return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn'))

def remove_nonword_chars(s):
  return re.sub('[\W]+', '_', re.sub('[\_]{2,}', '', s))

class SnakeCaseCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    for region in self.view.sel():
      content = self.view.substr(region)

      self.view.replace(edit, region, remove_nonword_chars(strip_accents(content)).lower())
