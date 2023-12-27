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

    def delete_comment(self) -> dict:
        if not 'idcomment' in self.req:
            return {'message': 'idcomment not found'}
        if self.req.get('idcomment') == '':
            return {'message': 'idcomment not found'}

        try:
            pst_service = PostsService()
            pst_service.delete_post(self.req.get('idcomment'))
            return {'message': 'comment deleted'}
        except:
            return {'message': 'error in delete comment'}

    def update_comments(self) -> dict:
        pst_service = PostsService()
        pst_service.update_post('243fe9ff-82f4-4adf-a867-232afaee8295')
        return{'teste':'teste'}