import unittest
from app.models import Comment,User

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')

        self.new_comment = Comment(comment_content = 'I love the pitch',user = self.user_James)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,'I love the pitch')
        self.assertEquals(self.new_comment.user,self.user_James)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

   
