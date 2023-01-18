import os
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

class GeneratePDF:
    def __init__(self, html, pdf, base_url=None, margin_x=2, margin_y=30):
        self.html = html
        self.pdf = pdf
        self.margin_x = margin_x
        self.margin_y = margin_y

    def render_pdf(self):
        margin = '{margin_y}px {margin_x}'.format(
            margin_x=f'{self.margin_x}cm',
            margin_y=self.margin_y
        )
        layout = '@page {size: A4 portrait; margin: %s;}' % margin;
        html = HTML(
            self.html
        )
        document = html.render(stylesheets=[CSS(string=layout)])
        pdf = document.copy(document.pages[::]).write_pdf(self.pdf)
        
        return pdf

generator = GeneratePDF(
    f'{os.getcwd()}/resume/html/index.html',
    f'{os.getcwd()}/resume/pdf/aaronmarr_cv.pdf',
    None,
    1,
    40
)

generator.render_pdf()
