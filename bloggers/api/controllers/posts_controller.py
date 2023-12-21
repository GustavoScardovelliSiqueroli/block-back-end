from bloggers.api.controllers.post_contents_controller import PostContentsController
from bloggers.api.services.post_contents_service import PostContentsService
from bloggers.api.services.posts_service import PostsService

class PostController():

    def __init__(self, req) -> None:
        self.req = req

    def register_post(self) -> dict:
        """register a post in db

        Raises:
            Exception: error in register post on db

        Returns:
            dict: message: post criado com sucesso!
            dict: message: todos os campos são obrigatórios!
        """
        pst_service = PostsService()
        if not 'iduser' in self.req or not 'title' in self.req:
            return {'message': 'Todos os campos são obrigatórios!'}
        if self.req['iduser'] =='' or self.req['title'] == '':
            return {'message': 'Todos os campos são obrigatórios!'}
        
        post = pst_service.create_post(self.req['iduser'], self.req['title'], text=self.req.get('text'), idsequence=self.req.get('idsequence'))
        print(post.idpost)
        print(self.req.get('contents'))
        try:
            pst_service.add_post(post)

            req_pst_content_controller = {
                'idpost': post.idpost,
                'contents': self.req.get('contents')
            }
            
            pst_content_controller = PostContentsController(req_pst_content_controller)
            pst_content_controller.register_post_contents()
            
            return {'message': 'Post criado com sucesso!'}
        except:
            raise Exception('Error in register post')

    def get_posts(self) -> dict:
        pst_service = PostsService()
        posts = pst_service.selecta_ll_posts()
        if not posts:
            return {'message': 'Sem posts para visualizar...'}
        return posts