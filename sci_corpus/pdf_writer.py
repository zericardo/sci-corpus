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
    def __init__(self, filename, **kw):  
        self.allowSplitting = 0  
        apply(BaseDocTemplate.__init__, (self, filename), kw)  

    def afterFlowable(self, flowable):
        "Registers TOC entries."
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
    # PDF properties
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
    canvas.saveState()
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, 'Created by Sci Corpus')
    canvas.restoreState()
 
def myLaterPages(canvas, doc):
    # Needs differentiate odd and even.
    # put the page number in the right margin
    canvas.saveState()
    canvas.line(50,50,8.27*inch-50,50)
    canvas.setFont('Helvetica',10)
    canvas.drawString(55, 40, "Created by Sci Corpus                %d" % doc.page)
    canvas.restoreState()


def exportToPDF(path, title, author, description, container,
               tmargin=30, bmargin=20, lmargin=30, rmargin=20,
               font='Helvetica', size=12,
               date=True, npages=True,
               replaceText=False, dimText=False):
                   
                           
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
                          PageTemplate('laters', frames=frameT, onPage=myLaterPages)])
                          
    Story = []
    Story.append(NextPageTemplate('laters'))
    Story.append(PageBreak())
    
    centered = ParagraphStyle(name='centered', fontSize=18, leading=26, alignment=1, spaceAfter=26) 
    Story.append(Paragraph('<b>Table of contents<\b>', centered))  
    toc = TableOfContents()
    toc.levelStyles = [styles["Heading1"], styles["Heading2"], styles["Heading3"]]
    Story.append(toc)
    
    Story.append(PageBreak())
    Story.append(NextPageTemplate('laters'))
            
    for snum, sec in enumerate(container.listSections()):
        if sec != 'Not Classified':
            Story.append(Paragraph(str(snum)+'.  '+sec,styles["Heading1"]))
            Story.append(Spacer(1, 12))
            for ssnum, subs in enumerate(container.listComponents(qsections=[sec])):
                if subs != 'Not Classified':
                    Story.append(Paragraph(str(snum)+'.'+str(ssnum+1)+'.  '+subs,styles["Heading2"]))
                    Story.append(Spacer(1, 12))
                    for fnum, func in enumerate(container.listStrategies(qsections=[sec],qsubsections=[subs])):
                        if func != 'Not Classified':
                            Story.append(Paragraph(str(snum)+'.'+str(ssnum+1)+'.'+str(fnum+1)+'.  '+func,styles["Heading3"]))
                            Story.append(Spacer(1, 12))
                            for idv, secv, subsv, funcv, sentv, refv in container.listSentences(section=[sec],subsection=[subs],function=[func]):
                                if sentv != 'NULL':
                                    ptext = sentv + ' Reference: ' + refv
                                    Story.append(Paragraph(ptext,styles["Bullet"]))
                                    Story.append(Spacer(1, 12))

    print "Exporting PDF ..."
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
