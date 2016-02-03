from unittest import TestCase
from plugins.ReqTracer import story
from source.job_story_end import check_current_time, fiboncci_number, check_n_pi, conversion_func, ask_user, \
    ten_conversions
from source.main import Interface, QA


class TestJobStory(TestCase):
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_check_current_time(self):
        QA('what time is it?', check_current_time())

    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I do not have to figure it\
                out myself')
    def test_check_nDigit_Fiboncci(self):
        QA('What is the 7TH digit of fibonacci', fiboncci_number(n=7))

    @story(
        'When I ask "What is the n digit of pi" I want to receive the answer so I do not have to figure it out myself')
    def test_check_nDigit_Pi(self):
        QA('What is the 2ND digit of pi', check_n_pi(2))

    @story(
        'When I ask "Please clear memory" I want the application to clear user set questions and answers\
         so I can reset the application')
    def test_check_memory_cleared(self):
        x = Interface()
        result = x.delete()
        self.assertEqual(result, x.checkdelete())
        QA('Please clear memory', x.checkdelete())

    @story('When I say "Open the door hal", I want the application to say "I m afraid I can not do that <user name> \
    so I know that is not an option')
    def test_ask_buttler(self):
        QA('Open the door hal', ask_user('john'))

    @story(
        'When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can\
         know the answer')
    def test_convert_unit(self):
        QA('What is the conversion of 1 cm to meter?', conversion_func(1, 'cm', 'm'))
        result = conversion_func(1, 'cm', 'm')
        self.assertEqual(result, 0.01)

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_ten_numeric(self):
        QA('What are 10 conversions of one cm ?', ten_conversions(1, 'cm', 'm', 'mm', 'km', 'in', 'ft', 'yd', 'mi',
                                                                  'micron', 'micrometer'))

