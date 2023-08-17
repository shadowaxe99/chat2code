from HTTPRequestHandler import HTTPRequestHandler
from ResponseHandler import ResponseHandler
from FileUploadHandler import FileUploadHandler
from PluginHandler import PluginHandler
from ui.appbody import AppBody
from ui.container import Container
from ui.filterbar import FilterBar
from ui.mainnav import MainNav
from ui.searchbar import SearchBar

if __name__ == '__main__':
    http_request_handler = HTTPRequestHandler()
response = http_request_handler.get('http://example.com')
    response_handler = ResponseHandler(response)
    file_upload_handler = FileUploadHandler()
    plugin_handler = PluginHandler()
    appbody = AppBody()
    container = Container()
    filterbar = FilterBar()
    mainnav = MainNav()
    searchbar = SearchBar()
    user_dashboard.display_message('Welcome')
    user_dashboard.get_user_input()
