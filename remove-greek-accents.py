import sublime
import sublime_plugin


class RemoveGreekAccentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                sublime.message_dialog(u'Remove Greek Accents: Please select some text')
            else:
                myString = self.view.substr(region)
                myString = myString.replace('Ά' , 'Α')
                myString = myString.replace('Έ' , 'Ε')
                myString = myString.replace('Ή' , 'Η')
                myString = myString.replace('Ί' , 'Ι')
                myString = myString.replace('Ϊ' , 'Ι')
                myString = myString.replace('Ϊ́' , 'Ι')
                myString = myString.replace('Ό' , 'Ο')
                myString = myString.replace('Ύ' , 'Υ')
                myString = myString.replace('Ώ' , 'Ω')
                myString = myString.replace('ά' , 'α')
                myString = myString.replace('έ' , 'ε')
                myString = myString.replace('ή' , 'η')
                myString = myString.replace('ί' , 'ι')
                myString = myString.replace('ϊ' , 'ι')
                myString = myString.replace('ΐ' , 'ι')
                myString = myString.replace('ό' , 'ο')
                myString = myString.replace('ύ' , 'υ')
                myString = myString.replace('ώ' , 'ω')
                self.view.replace(edit, region, myString)