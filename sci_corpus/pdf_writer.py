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
            if style == 'Heading1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Heading2':
                self.notify('TOCEntry', (1, text, self.page))
            if style == 'Heading3':
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
    canvas.setSubject(doc.description)
    canvas.setAuthor(doc.author)
    
    canvas.setCreator('Sci Corpus')
    canvas.setFont('Helvetica-Bold',26)
    canvas.drawString(8.27*inch/3.0, 11.69*inch-108, doc.title)
    canvas.setFont('Helvetica',16)
    canvas.drawString(8.27*inch/3.0, 11.69*inch-208, doc.author)
    canvas.setFont('Helvetica',14)
    canvas.drawString(8.27*inch/3.0, 11.69*inch-308, doc.description)
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, 'Created by Sci Corpus')
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
               replaceText=False, dimText=False):
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
        
    boolean: replaceText
        If true, replace the marker if ...
        
    boolean: dimTex
        If true, change text color inside the markers
        
    string: marker_beg, marker_end, replace_where, replace_by
        Strip sentence variables
    
    Returns:
    --------
    other pages
    
    """               
                           
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
    Story.append(NextPageTemplate('toc'))
    Story.append(PageBreak())
    
    centered = ParagraphStyle(name='centered', fontSize=18, leading=26, alignment=1, spaceAfter=26) 
    Story.append(Paragraph('<b>Table of contents<\b>', centered))  
    toc = TableOfContents()
    toc.levelStyles = [styles["Heading1"], styles["Heading2"], styles["Heading3"]]
    Story.append(toc)
    
    Story.append(NextPageTemplate('laters'))
    Story.append(PageBreak())
            
            
    sections = container.listSections()
    if "Not Classified" in sections:
        sections.remove("Not Classified")
    
    for snum, sec in enumerate(sections):
        Story.append(Paragraph(str(snum+1)+'.  '+sec,styles["Heading1"]))
        Story.append(Spacer(1, 12))
        
        components = container.listComponents(qsections=[sec])
        if "Not Classified" in components:
            components.remove("Not Classified")
            
        for compnum, comp in enumerate(components):
            Story.append(Paragraph(str(snum+1)+'.'+str(compnum+1)+'.  '+comp,styles["Heading2"]))
            Story.append(Spacer(1, 12))
            
            strategies = container.listStrategies(qsections=[sec],qsubsections=[comp])
            if "Not Classified" in strategies:
                strategies.remove("Not Classified")
            
            for stranum, stra in enumerate(strategies):
                Story.append(Paragraph(str(snum+1)+'.'+str(compnum+1)+'.'+str(stranum+1)+'.  '+stra,styles["Heading3"]))
                Story.append(Spacer(1, 12))
                for idv, secv, subsv, funcv, sentv, refv in container.listSentences(section=[sec],subsection=[comp],function=[stra]):
                    if sentv != 'NULL':
                        if replaceText:
                            sentv = container.adjustSentence(sentv, marker_beg, marker_end, replace_where, replace_by)
                        if dimText:
                            sentv = container.adjustSentence(sentv, marker_beg, marker_end, "dim", replace_by)
                            
                        ptext = sentv + ' Reference: ' + refv
                        Story.append(Paragraph(ptext,styles["Bullet"]))
                        Story.append(Spacer(1, 12))

    doc.multiBuild(Story)
    
    #fontBold = font+'-Bold'
    #styles.add(ParagraphStyle(name='Justify', alignment=4, fontName='Helvetica', fontSize=10, firstLineIndent=24,leftIndent=20))
    #styles.add(ParagraphStyle(name='Section', alignment=0, fontName='Helvetica-Bold', fontSize=16, firstLineIndent=12))
    #styles.add(ParagraphStyle(name='Subsection', alignment=0, fontName='Helvetica-Bold', fontSize=14, firstLineIndent=16))
    #styles.add(ParagraphStyle(name='Function', alignment=0, fontName='Helvetica-Bold', fontSize=12, firstLineIndent=20))
    #toc.levelStyles = [  
    #    ParagraphStyle(fontName='Times-Bold', fontSize=20, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=10, leading=16),  
    #    ParagraphStyle(fontSize=18, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),  
    #]  
