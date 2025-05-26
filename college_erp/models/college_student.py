from odoo import models, fields, api, exceptions

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'

    admission_number = fields.Char(string='Admission Number', required=True, unique=True)
    admission_date = fields.Date(string='Admission Date', required=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    father_name = fields.Char(string='Father Name', required=True)
    mother_name = fields.Char(string='Mother Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    communication_address = fields.Text(string='Communication Address', required=True)
    permanent_address = fields.Text(string='Permanent Address', required=True)