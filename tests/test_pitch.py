import unittest
from app.models import Pitch,User

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')

        self.new_pitch = Pitch(title = 'Love quote',content = 'I just take your heart and leave you bleeding and still asking for more',user = self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title,'Love quote')
        self.assertEquals(self.new_pitch.content,'I just take your heart and leave you bleeding and still asking for more')
        self.assertEquals(self.new_pitch.user,self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_title(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches('Love quote')
        self.assertTrue(len(got_pitches) == 1)