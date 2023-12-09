from bloggers.api.services.posts_service import PostsService

class PostController():

    def __init__(self, req) -> None:
        self.req = req

    def register_post(self) -> dict:
        pst_service = PostsService()
        if not 'iduser' in self.req or not 'title' in self.req:
            return {'message': 'Todos os campos são obrigatórios!'}
        if self.req['iduser'] =='' or self.req['title'] == '':
            return {'message': 'Todos os campos são obrigatórios!'}
        
        try:
            pst_service.add_post(pst_service.create_post(self.req['iduser'], self.req['title'], text=self.req.get('text'), idsequence=self.req.get('idsequence')))
            return {'message': 'Post criado com sucesso!'}
        except:
            raise Exception('Error in register post')
