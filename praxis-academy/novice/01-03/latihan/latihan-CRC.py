# Class Responsibilities Colaborator (CRC) Card
# dibuat ketika akan melakukan sebuah tugas dengan membagi tugas (responsibilities) kepada
# class utama dan class collaborator untuk membantu menyelesaikan responsibilities

# contoh 
class HtmlToMarkdown(object):
    '''
    @colaborator : ImageUploader
    @responsibilities: convert html 
    '''
    def __init__(self, image_uploader):
        self.image_uploader = image_uploader

    
class ImageUploader(object):
    '''
    @responsibility : upload image to cloud
    '''
    pass

# class html akan berupaya men-convert html kode ke markdown file
# karena tidak mampu mengubah gambar ke md file, maka butuh bantuan kolaborator
# ImageUploader untuk mengupload gambar ke cloud 