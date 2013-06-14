import xmllib, string
class QuotationParser(xmllib.XMLParser):
    def __init__(self):
        xmllib.XMLParser.__init__(self)
        self.thisquote = ''
    def handle_data(self, data):
        self.thisquote = self.thisquote + data
    def syntax_error(self, message):
        pass
    def start_quotations(self):
        print('---Begin Document---')
    def start_quotation(self, attrs):
        print('QUOTATION')
    def end_quotation(self):
        print('end')
        self.thisquote = ''
    def unknown_starttag(self, tag, attrs):
        self.thisquote = self.thisquote + '{'
    def unknown_endtag(self, tag):
        self.thisquote = self.thisquote + '}'
    def unknown_charref(self, ref):
        self.thisquote = self.thisquote + '?'
    def unknown_entityref(self, name):
        self.thisquote = self.thisquote + '#'
if __name__ == '__main__':
    pp = QuotationParser()
    for c in open('F:/student.xml').read():
        pp.feed(c)
    pp.close()
