from pylatex import Document, Section, Command
from pylatex.utils import NoEscape

from get_user_input import schools, name


def dict_doc_append(d):
    with doc.create(Section('Experience')):
        for k, v in d.items():
            if isinstance(v, dict):
                dict_doc_append(v)
            else:
                doc.append(v)


def fill_document(doc):
    """
    Add a section, a subsection, and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    dict_doc_append(schools)


if __name__ == '__main__':
    doc = Document('basic')
    fill_document(doc)

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Resume'))
    doc.preamble.append(Command('author', name))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False)

    text = doc.dumps()
