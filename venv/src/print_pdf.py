from fpdf import FPDF
import os

pdf = FPDF(format='3x5', unit='in')
pdf.add_page()
pdf.set_font('Arial', '', 12) # pdf.set_font('Arial', 'B', 16)
effective_page_width = pdf.w - 2*pdf.l_margin


def print_juror(juror):
    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(0.0, 0.0, str(juror.trial).upper())
    pdf.ln(0.35)

    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.45, 0.0, 'Name: ')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, juror.name, ln=0)
    pdf.ln(0.25)

    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.35, 0.0, 'Age: ')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, str(juror.age))
    pdf.ln(0.25)

    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.85, 0.0, 'Occupation:')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, juror.occupation)
    pdf.ln(0.25)

    file_path = 'trials/'+juror.trial.lower().replace(" ", "_")
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    return pdf.output(file_path+"/"+juror.name+".pdf", 'F')


# def print_me(filename, content):
#     effective_page_width = pdf.w - 2 * pdf.l_margin
#
#     pdf.set_font('Times', 'B', 10.0)
#     pdf.cell(1.0, 0.0, 'Without multi_cell using effective page width:')
#     pdf.ln(0.25)
#     pdf.set_font('Times', '', 10.0)
#     # Cell is as wide as the effective page width
#     pdf.cell(effective_page_width, 0.0, loremipsum)
#     pdf.ln(0.5)
#     pdf.set_font('Times', 'B', 10.0)
#     pdf.cell(1.0, 0.0, 'Using multi_cell and effective page width:')
#     pdf.ln(0.25)
#
#     pdf.set_font('Times', '', 10.0)
#     # Cell is as wide as the effective page width
#     # and multi_cell requires declaring the height of the cell.
#     pdf.multi_cell(effective_page_width, 0.15, loremipsum)
#     pdf.ln(0.5)
#
#     pdf.output('multi_cell.pdf', 'F')
#
#     #pdf.cell(30, 10, content[1])
#     print("content is.. {}\n".format(content))
#     return pdf.output("test.pdf", 'F')


# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', '', 12) # pdf.set_font('Arial', 'B', 16)
# pdf.cell(40, 10, 'hello, me! margin test. Arial font, 12px. no bold')
# pdf.output('test3.pdf', 'F')

