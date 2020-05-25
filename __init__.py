from mycroft import MycroftSkill, intent_file_handler


class TestPadatious(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('padatious.test.intent')
    def handle_padatious_test(self, message):
        self.speak_dialog('padatious.test')


def create_skill():
    return TestPadatious()

