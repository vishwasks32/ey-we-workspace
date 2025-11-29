import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import date

def generate_themed_pdf(template_filename="report_theme.html", output_filename="themed_report.pdf"):
    """
    Renders an HTML template with data (Jinja2) and converts it to a PDF (WeasyPrint).
    """
    
    # 1. Prepare Dynamic Data
    deliverables_data = [
        {'id': 1, 'description': 'Database schema design', 'hours': 80},
        {'id': 2, 'description': 'Frontend dashboard implementation', 'hours': 120},
        {'id': 3, 'description': 'API integration and testing', 'hours': 95}
    ]
    
    df = pd.DataFrame(deliverables_data)

    # 2. Context Data for the Template
    template_context = {
        'project_name': 'Phoenix Core V2',
        'status': 'Completed and Deployed',
        'completion_date': '2025-11-29',
        'total_items_completed': len(deliverables_data),
        'deliverables': deliverables_data,
        'today_date': date.today().strftime("%Y-%m-%d %H:%M:%S")
    }

    # 3. Setup Jinja2 Environment and Load Template
    # Loads templates from the directory where the script is run
    env = Environment(loader=FileSystemLoader('.')) 
    template = env.get_template(template_filename)

    # 4. Render Template to HTML String
    # This step replaces all the {{ variables }} with the actual data
    html_output = template.render(template_context)
    
    # 5. Convert HTML to PDF using WeasyPrint
    # WeasyPrint handles the CSS styling (the "theme") automatically
    HTML(string=html_output).write_pdf(output_filename)
    
    print(f"Themed PDF Report generated successfully: {output_filename}")

# Run the generation
generate_themed_pdf()