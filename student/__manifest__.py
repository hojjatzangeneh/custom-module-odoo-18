{
    'name': 'Student ERP',
    'version': '1.0',
    'author': 'Hojjat Zangeneh',
    'category': 'Education',
    'summary': 'A comprehensive ERP system for managing Student operations',
    'description': """
    This module provides a complete ERP solution for Student, including features for managing students, courses, faculty, and more.    
    It is designed to streamline Student operations and improve efficiency.
    """,
    'maintainer': 'Hojjat Zangeneh',
    # 'depends': [
    #     'base',
    #     'mail',
    #     'web',
    #     'hr',
    #     'sale_management',
    #     'account',
    #     'project',
    # ],
    'sequence': 2,
    'data': [
         'security/ir.model.access.csv',
        'views/student_view.xml',
            ],
     'installable': True,
     'application': True,    
     'auto_install': False,
     'license': 'LGPL-3',
    # 'images': [
    #     'static/description/banner.png',
    # ],
    # 'website': 'https://www.example.com',
    # 'support': ''https://www.example.com/support',
    # 'maintainer_email': 'hojjat.zangeneh@gmail.com',
    # 'currency': 'EUR',
    # 'price': 49.99,
    # 'external_dependencies': {
    #     'python': ['pandas', 'numpy'],
    #     'bin': ['wkhtmltopdf'],
    # },
    # 'demo': [
    #     'data/demo_student.xml',
    #     'data/demo_course.xml',
    #     'data/demo_faculty.xml',
    # ],
    # 'post_init_hook': '_post_init_hook',
    # 'pre_init_hook': '_pre_init_hook',
    # 'uninstall_hook': '_uninstall_hook',
    # 'qweb': [
    #     'static/src/xml/college_templates.xml',
    # ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'college_erp/static/src/js/college.js',
    #         'college_erp/static/src/css/college.css',
    #     ],
    #     'web.assets_qweb': [
    #         'college_erp/static/src/xml/college_templates.xml',
    #     ],
    # }
}