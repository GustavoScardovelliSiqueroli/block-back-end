from bloggers.api.models.post import Posts
from bloggers.api.services.posts_service import PostsService

class CommentsController():
    def __init__(self, req) -> None:
        self.req =  req

    def register_comments(self) -> dict:
        pst_service = PostsService()
        comment: Posts = pst_service.create_post(self.req.get('iduser'),self.req.get('title'),text=self.req.get('text'), idsequence=self.req.get('idsequence'))
        pst_service.add_post(comment)
        return {'message': 'comment created'}