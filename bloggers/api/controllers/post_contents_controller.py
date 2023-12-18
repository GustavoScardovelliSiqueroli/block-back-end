from bloggers.api.services.post_contents_service import PostContentsService
class PostContentsController():
    def __init__(self, req) -> None:
        self.req = req

    def teste(self) -> dict:
        pst_cntnts_service = PostContentsService()
        return {'teste': pst_cntnts_service.teste()}

    def register_post_contents(self):
        pst_cntns_service = PostContentsService()
        if not 'idpost' in self.req:
            return {'message': 'idpost required.'}
        if not 'contents' in self.req:
            return {'message': 'contents list required.'}

        contents: list = self.req.get('contents')
        contets_return = [] 
        sequence = 0
        for content in contents:
            sequence =+ 1
            post_content_created = pst_cntns_service.create_post_content(self.req['idpost'],
                 sequence, contenttext=content.get('text'), imagepath=content.get('imagepath'))
            pst_cntns_service.add_post_contents(post_content_created)
            contets_return.append(post_content_created)
        return {'contents': contets_return}
