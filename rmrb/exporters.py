from scrapy.exporters import BaseItemExporter
from scrapy.utils.python import to_bytes

class HtmlItemExporter(BaseItemExporter):
    """Save crawled data into HTML file."""

    def __init__(self, file, **kwargs):
        self._configure(kwargs, dont_fail=True)
        self.file = file

    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass

    def export_item(self, item):
        # self.file.write(b'DEBUG')
        self.file.write(to_bytes(item['text']))
