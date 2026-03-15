from fpdf import FPDF


pdf = FPDF(orientation = 'P',unit = 'pt', format = 'A4')
pdf.add_page()
pdf.image('alex.jpg', w=144,h=108)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Alexandra Daddario',align='C',ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=0, h=25, txt='Info',align='L',ln=1)

txt1= """Alexandra Anna Daddario (born March 16, 1986) is an American actress. She had her breakthrough portraying Annabeth Chase in Percy Jackson & the Olympians: The Lightning Thief (2010) and its sequel (2013). She has since starred in Hall Pass (2011), Texas Chainsaw 3D (2013), San Andreas (2015), Baywatch (2017), and We Summon the Darkness (2019).

In 2021, she starred in the first season of the HBO satirical series The White Lotus, for which she received critical acclaim and a nomination for the Primetime Emmy Award for Outstanding Supporting Actress in a Limited or Anthology Series or Movie. In 2023, she began playing the lead role of Dr. Rowan Fielding in the AMC horror series Mayfair Witches."""

pdf.set_font(family='Times', style='I', size=14)
pdf.multi_cell(w=0, h=20, txt=txt1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=25, txt='Born')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='March 16, 1986 (age 39), New York City, U.S.',ln=1)

pdf.set_font(family='Times', style='B', size=18)
pdf.cell(w=100, h=25, txt='Occupation')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Actress',ln=1)



pdf.output('demo.pdf')