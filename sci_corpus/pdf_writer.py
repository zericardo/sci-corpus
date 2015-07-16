"""
.. module:: pdf_writer
   :platform: Unix, Windows
   :synopsis: functions to write a pdf file with all the phrases

.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>
.. moduleauthor:: Tiago de Campos <tiago.campos@usp.br>

"""

from reportlab.lib.pagesizes import A4
from reportlab.rl_config import defaultPageSize #defaultPage is A4, just as we need
from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.enums import TA_JUSTIFY

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles=getSampleStyleSheet()


class MyDocTemplate(BaseDocTemplate): 
    """
    Creates the basic file template

    Parameters:
    -----------
    parent class: BaseDocTemplate

           class that contain the file basics definitions

    """
    
    def __init__(self, filename, **kw):
        """
        Initialize the file

        Parameters:
        -----------
        string: filename 

               name of the final pdf file
               
        kwargs: kw
 
        Returns:
        --------
        A doc template with our preferences
        
        """
        self.allowSplitting = 0  
        apply(BaseDocTemplate.__init__, (self, filename), kw)  

    def afterFlowable(self, flowable):
        """
        This function scans the pdf file and produce a toc.
        
        Parameters:
        -----------
        flowable: 
        
        Returns:
        --------
        Modified pdf with toc
        
        """
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'heading_1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'heading_2':
                self.notify('TOCEntry', (1, text, self.page))
            if style == 'heading_3':
                self.notify('TOCEntry', (2, text, self.page))
        
def myFirstPage(canvas, doc):
    """
    Generate the file's first page static.
    
    Parameters:
    -----------
    canvas:
    
    doc:
    
    Returns:
    --------
    First page of pdf.
    
    """
    canvas.saveState()
    canvas.setTitle(doc.title)
    canvas.setAuthor(doc.author)
    
    canvas.setCreator('Sci Corpus')
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, 'Created by Sci Corpus - https://github.com/zericardo182/sci-corpus')
    canvas.restoreState()
 
def myTOCPages(canvas, doc):
    # Needs differentiate odd and even.
    """
    Generate the static style for TOC pages
    
    Parameters:
    -----------
    canvas:
    
    doc:
    
    Returns:
    --------
    TOC pages
    
    """
    canvas.saveState()
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, 'Created by Sci Corpus')
    canvas.restoreState()
 
def myLaterPages(canvas, doc):
    # Needs differentiate odd and even.
    # put the page number in the right margin
    """
    Generate the static style for all other pages.
    
    Parameters:
    -----------
    canvas:
    
    doc:
    
    Returns:
    --------
    other pages
    
    """
    canvas.saveState()
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, "Created by Sci Corpus")
    canvas.drawString(PAGE_WIDTH-65, 40, "%d" % doc.page)
    canvas.restoreState()


def exportToPDF(path, title, author, description, container,
               marker_beg, marker_end, replace_where, replace_by,
               tmargin=30, bmargin=20, lmargin=30, rmargin=20,
               font='Helvetica', size=12,
               mode='Bold'):
    """
    This function produce the pdf itself with all the preferences 
    
    Parameters:
    -----------
    string: path
        Where it will be save
        
    string: title
        Document's title
        
    string: author
        Document's author
    
    string: description
        A short description of the file
        
    class: container
        Instance of the program
        
    integer: *margin
        The top, bottom, left and right margin
        
    string: font
        Font name
        
    integer: size
        Basic size of the text.
        
    string: mode
        Modes: Bold, Replace, Raw
        
    string: marker_beg, marker_end, replace_where, replace_by
        Strip sentence variables
    
    Returns:
    --------
    other pages
    
    """               
    
    if font == 'Times-Roman':
		fontbold = 'Times-Bold'
    if font == 'Courier':
		fontbold = 'Courier-Bold'
    if font == 'Helvetica':
		fontbold = 'Helvetica-Bold'

    phrase_base = ParagraphStyle(name='phrase_base', fontName=font, fontSize=size, alignment=TA_JUSTIFY, leftIndent=0.5*inch)
    heading_1 = ParagraphStyle(name='heading_1', fontName=fontbold, fontSize=size+4, leading=22, spaceBefore=12, spaceAfter=6)
    heading_2 = ParagraphStyle(name='heading_2', fontName=fontbold, fontSize=size+2, leading=18, spaceBefore=6, spaceAfter=6)
    heading_3 = ParagraphStyle(name='heading_3', fontName=font, fontSize=size+1, leading=14, spaceBefore=6, spaceAfter=6)
    centered = ParagraphStyle(name='centered', fontName=font, fontSize=18, leading=26, alignment=1, spaceAfter=26) 
    desc_style = ParagraphStyle(name='desc_style', fontName=font, fontSize=size+2)
    title_style = ParagraphStyle(name='title_style', fontName=font, fontSize=size+12)
    author_style = ParagraphStyle(name='author_style', fontName=font, fontSize=size+3)
    
    doc = MyDocTemplate(path, 
                          pagesize=A4,
                          rightMargin=rmargin*mm, 
                          leftMargin=lmargin*mm,
                          topMargin=tmargin*mm,
                          bottomMargin=bmargin*mm)
    doc.title = title
    doc.author = author
    doc.description = description

    frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    
    doc.addPageTemplates([PageTemplate('first', frames=frameT, onPage=myFirstPage),
                          PageTemplate('toc', frames=frameT, onPage=myTOCPages),
                          PageTemplate('laters', frames=frameT, onPage=myLaterPages)])
                          
    Story = []
    Story.append(Spacer(1, 12))
    Story.append(Paragraph(title, title_style))
    Story.append(Spacer(1, 50))
    Story.append(Paragraph(author, author_style))
    Story.append(Spacer(1, 150))
    Story.append(Paragraph(description, desc_style))
    Story.append(NextPageTemplate('toc'))
    Story.append(PageBreak())
    
    Story.append(Paragraph('Table of contents', centered))  
    toc = TableOfContents()
    toc.levelStyles = [heading_1, heading_2, heading_3]
    Story.append(toc)
    
    Story.append(NextPageTemplate('laters'))
    Story.append(PageBreak())
            
            
    sections = container.listSections()
    if "Not Classified" in sections:
        sections.remove("Not Classified")
    
    for snum, sec in enumerate(sections):
        Story.append(Paragraph(str(snum+1)+'.  '+sec,heading_1))
        Story.append(Spacer(1, 12))
        
        components = container.listComponents(qsections=[sec])
        if "Not Classified" in components:
            components.remove("Not Classified")
            
        for compnum, comp in enumerate(components):
            Story.append(Paragraph(str(snum+1)+'.'+str(compnum+1)+'.  '+comp,heading_2))
            Story.append(Spacer(1, 12))
            
            strategies = container.listStrategies(qsections=[sec],qsubsections=[comp])
            if "Not Classified" in strategies:
                strategies.remove("Not Classified")
                
            nummenos = 0
            
            for stranum, stra in enumerate(strategies):
                
                Story.append(Paragraph(str(snum+1)+'.'+str(compnum+1)+'.'+str(stranum-nummenos+1)+'.  '+stra,heading_3))
                Story.append(Spacer(1, 12))
                lista = container.listSentences(section=[sec],subsection=[comp],function=[stra])

                if lista == []:
                    Story.pop()
                    Story.pop()
                    nummenos+=1
                
                for lista in container.listSentences(section=[sec],subsection=[comp],function=[stra]):
                    if lista != []:
                        idv, secv, subsv, funcv, sentv, refv = lista
                        if sentv != 'NULL':
                            if mode!='Raw':
                                sentv = container.adjustSentence(sentv, marker_beg, marker_end, replace_where, replace_by,  mode)                                
                            if refv == 'NULL':
                                refv = 'None'
                            ptext = sentv + ' Reference: ' + refv
                            Story.append(Paragraph(ptext,phrase_base))
                            Story.append(Spacer(1, 12))


    doc.multiBuild(Story)
