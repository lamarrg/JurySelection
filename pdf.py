from fpdf import FPDF
import os


def set_pdf():
    pdf_start = FPDF(format='3x5', unit='in')
    pdf_start.add_page()
    pdf_start.set_font('Arial', '', 12)  # pdf.set_font('Arial', 'B', 16)
    return pdf_start


def file_path_underscore(path_text):
    return path_text.lower().replace(" ", "_")


def print_juror(juror_data):
    pdf = set_pdf()
    effective_page_width = pdf.w - 2 * pdf.l_margin

    # cell for header-trial name
    pdf.set_font('Times', 'B', 12.0)
    pdf.cell(0.0, 0.0, str(juror_data.get_trial_name()).upper())
    pdf.ln(0.25)

    # cell for name
    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.45, 0.0, 'Name: ')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, juror_data.name, ln=0)
    pdf.ln(0.2)

    # cell for age
    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.35, 0.0, 'Age: ')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, str(juror_data.age))
    print("juror age {}".format(juror_data.age))
    pdf.ln(0.2)

    # cell for occupation
    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.85, 0.0, 'Occupation:')
    pdf.set_font('Times', '', 10.0)
    pdf.cell(0.0, 0.0, juror_data.occupation)
    pdf.ln(0.2)

    # cell for details. wraps data to fit width of card
    pdf.set_font('Times', 'B', 10.0)
    pdf.cell(0.0, 0.0, 'Details:')
    pdf.ln(0.10)
    pdf.set_font('Times', '', 10.0)
    pdf.multi_cell(effective_page_width, 0.15, juror_data.details)
    pdf.ln(0.15)

    trial_file_path = 'trials/'+file_path_underscore(juror_data.get_trial_name())
    juror_file_path = file_path_underscore(juror_data.name)
    if not os.path.exists(trial_file_path):
        os.makedirs(trial_file_path)

    return pdf.output(trial_file_path+"/"+juror_file_path+".pdf", 'F')


def remove_juror_pdf(juror):
    trial_file_path = 'trials/'+file_path_underscore(juror.get_trial_name())
    juror_file_path = file_path_underscore(juror.name)
    pdf_to_remove = trial_file_path+'/'+juror_file_path+".pdf"
    if os.path.exists(pdf_to_remove):
        try:
            os.remove(pdf_to_remove)
        except OSError:
            pass



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

