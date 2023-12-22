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
        if not contents:
            return {'contents': ['']}
        for content in contents:
            post_content_created = pst_cntns_service.create_post_content(self.req['idpost'],
                 sequence, contenttext=content.get('text'), imagepath=content.get('imagepath'))
            pst_cntns_service.add_post_contents(post_content_created)
            contets_return.append(post_content_created)
            sequence =+ 1
        return {'contents': contets_return}
        
    def delete_post_content(self) -> dict:
        # if not 'idpostcontent' in self.req:
        #     return {'message': 'idpostcontent not fount.'}
        # if self.req['idpostcontent'] == '':
        #     return {'message': 'idpostcontent not fount.'}

        post_contents_service = PostContentsService()
        return {'result': post_contents_service.delete_post_content('decc3a47-6ee1-4297-816f-ba91d556d9db')}
