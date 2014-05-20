from reportlab.lib.pagesizes import A4
from reportlab.rl_config import defaultPageSize #defaultPage is A4, just as we need
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame

#from ContainerDB import listSections as LS
#listSections, listSubSections, listSentences

PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]

class MyDocTemplate(BaseDocTemplate):
        
    def __init__(self, filepath, **kw):
    
        self.title = 'Title: SciCorpus'
        self.author = 'Author: SciCorpus Team'
        self.description = 'Description: This is a scientific CORPUS'
        
        for key, value in kw.items():
            if key == 'container':
                self.__container = kw['container']
        
        self.allowSplitting = 0
        apply(BaseDocTemplate.__init__, (self, filepath), kw)
        self.addPageTemplates([PageTemplate('first', [Frame(0, 0, 8.27*inch, 11.69*inch, id='F1')],
                              onPage=self.myFirstPage),
                              PageTemplate('laters', [Frame(0, 0, 8.27*inch, 11.69*inch, id='F2')], 
                              onPage=self.myLaterPages)])

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        self.__container = value

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


    def myFirstPage(self, canvas, doc):
    
        canvas.saveState()
        canvas.setFont('Helvetica-Bold',26)
        canvas.drawString(8.27*inch/2.0, 11.69*inch-108, str(self.title))
        canvas.setFont('Helvetica',16)
        canvas.drawString(8.27*inch/2.0, 11.69*inch-208, str(self.author))
        canvas.setFont('Helvetica',14)
        canvas.drawString(8.27*inch/2.0, 11.69*inch-308, str(self.description))
        canvas.line(50,50,8.27*inch-50,50)
        canvas.setFont('Helvetica',12)
        canvas.drawString(55, 40, "Created by Sci Corpus")
        canvas.restoreState()        
         
    def myLaterPages(self, canvas, doc):
        
        canvas.saveState()
        canvas.setFont('Helvetica',12)
        canvas.drawString(inch, 0.5*inch, "Created by Sci Corpus %d" % doc.page)
        canvas.restoreState()


    def exportToPDF(self, path, title,  author,  description, 
                   tmargin=30, bmargin=20, lmargin=30, rmargin=20,
                   font='Helvetica', size=12,
                   date=True, npages=True,
                   replaceText=False, dimText=False):
                       
        self.title=title
        self.author=author
        self.description=description


                               
        styles=getSampleStyleSheet()
        
        doc = MyDocTemplate(path,
                            pagesize=A4,
                            rightMargin=rmargin*mm, 
                            leftMargin=lmargin*mm,
                            topMargin=tmargin*mm,
                            bottomMargin=bmargin*mm)
                                
        #doc = SimpleDocTemplate(path,pagesize=A4,
        #                        rightMargin=rmargin*mm,leftMargin=lmargin*mm,
        #                        topMargin=tmargin*mm,bottomMargin=bmargin*mm)
        Story = []
        Story.append(NextPageTemplate('first'))
        Story.append(PageBreak())
        Story.append(NextPageTemplate('laters'))
        Story.append(PageBreak())
        
        #fontBold = font+'-Bold'
        #styles.add(ParagraphStyle(name='Justify', alignment=4, fontName='Helvetica', fontSize=10, firstLineIndent=24,leftIndent=20))
        #styles.add(ParagraphStyle(name='Section', alignment=0, fontName='Helvetica-Bold', fontSize=16, firstLineIndent=12))
        #styles.add(ParagraphStyle(name='Subsection', alignment=0, fontName='Helvetica-Bold', fontSize=14, firstLineIndent=16))
        #styles.add(ParagraphStyle(name='Function', alignment=0, fontName='Helvetica-Bold', fontSize=12, firstLineIndent=20))
    
        centered = ParagraphStyle(name = 'centered',  
                fontSize = 30,  
                leading = 16,  
                alignment = 1,  
                spaceAfter = 20) 
    
    
        toc = TableOfContents()
        toc.levelStyles = [styles["Heading1"], styles["Heading2"], styles["Heading3"]]
        #toc.levelStyles = [  
        #    ParagraphStyle(fontName='Times-Bold', fontSize=20, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=10, leading=16),  
        #    ParagraphStyle(fontSize=18, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),  
        #]  
        
        Story.append(Paragraph('<b>Table of contents</b>', centered))  
        Story.append(toc)
        Story.append(PageBreak())
        Story.append(NextPageTemplate('laters'))
                
        for snum, sec in enumerate(self.container.listSections()):
            if sec != 'Not Classified':
                Story.append(Paragraph(str(snum)+'.  '+sec,styles["Heading1"]))
                Story.append(Spacer(1, 12))
                for ssnum, subs in enumerate(self.container.listSubSections(qsections=[sec])):
                    if subs != 'Not Classified':
                        Story.append(Paragraph(str(snum)+'.'+str(ssnum)+'.  '+subs,styles["Heading2"]))
                        Story.append(Spacer(1, 12))
                        for fnum, func in enumerate(self.container.listFunctions(qsections=[sec],qsubsections=[subs])):
                            if func != 'Not Classified':
                                Story.append(Paragraph(str(snum)+'.'+str(ssnum)+'.'+str(fnum)+'.  '+func,styles["Heading3"]))
                                Story.append(Spacer(1, 12))
                                for idv, secv, subsv, funcv, sentv, refv in self.container.listSentences(section=[sec],subsection=[subs],function=[func]):
                                    if sentv != 'NULL':
                                        ptext = sentv + ' Reference: ' + refv
                                        Story.append(Paragraph(ptext,styles["Bullet"]))
                                        Story.append(Spacer(1, 12))

        print "Exporting PDF ..."
        doc.multiBuild(Story)
