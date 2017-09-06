# Import FPDF class
from fpdf import FPDF

# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf = FPDF(format='3x5', unit='in')

# Add new page. Without this you cannot create the document.
pdf.add_page()

# Remember to always put one of these at least once.
pdf.set_font('Times', '', 10.0)

# Long meaningless piece of text
loremipsum = """Lorem ipsum dolor sit amet, vel ne quando dissentias. \
Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi \
ut. At mea wisi dolorum contentiones, in malis vitae viderer mel.

Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te \
augue summo vis. An vim quas torquatos, electram posidonium eam ea, eros \
blandit ea vel. Reque summo assueverit an sit. Sed nibh conceptam cu, pro \
in graeci ancillae constituto, eam eu oratio soleat instructior. No deleniti \
quaerendum vim, assum saepe munere ea vis, te tale tempor sit. An sed debet \
ocurreret adversarium, ne enim docendi mandamus sea.
"""

effective_page_width = pdf.w - 2 * pdf.l_margin

pdf.set_font('Times', 'B', 10.0)
pdf.cell(1.0, 0.0, 'Without multi_cell using effective page width:')
pdf.ln(0.25)
pdf.set_font('Times', '', 10.0)
# Cell is as wide as the effective page width
pdf.cell(effective_page_width, 0.0, loremipsum)
pdf.ln(0.5)
pdf.set_font('Times', 'B', 10.0)
pdf.cell(1.0, 0.0, 'Using multi_cell and effective page width:')
pdf.ln(0.25)

pdf.set_font('Times', '', 10.0)
# Cell is as wide as the effective page width
# and multi_cell requires declaring the height of the cell.
pdf.multi_cell(effective_page_width, 0.15, loremipsum)
pdf.ln(0.5)


pdf.output('multi_cell.pdf', 'F')