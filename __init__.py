from mycroft import MycroftSkill, intent_file_handler


class EventPlanner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('planner.event.intent')
    def handle_planner_event(self, message):
        self.speak_dialog('planner.event')


def create_skill():
    return EventPlanner()

