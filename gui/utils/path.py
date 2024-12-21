class Path:
    _url_prefix = "/"

    def __init__(
        self,
        interface="",
        endpoint="",
    ):
        self._interface = interface
        self._endpoint = f"/{endpoint}"

    @property
    def interface(self):
        return self._interface

    @property
    def endpoint(self):
        return self._endpoint

    def url(self):
        return f"{self._interface}{self._endpoint}"

    def handle_redirect(self, message=""):
        err_msg = f"\nERROR: {message}\n"
        err_msg += f"'{self._url_prefix + self.url()}'\n"
        err_msg += f"\nRedirecting to GUI...\n"
        print(err_msg)


# MARK: GuiPath
class GuiPath(Path):
    _file_prefix = "pages/"
    _file_type = ".html"

    def __init__(
        self,
        interface="gui",
        endpoint="",
        file_name="",
    ):
        self._file_name = file_name
        super().__init__(interface, endpoint)

    @property
    def file_name(self):
        return self._file_name

    def file_path(self):
        return self._file_prefix + self._file_name + self._file_type
