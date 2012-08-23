class MyReport(Report):
    template_chart = charts.TemplateChart(template="myapp/template_chart.html")

    def get_data_for_template_chart(self):
        pony_types = [
            ('Blue', 'Equus Caeruleus'),
            ('Pink', 'Equus Roseus'),
            ('Magical', 'Equus Magica')
        ]

        template_context = {
            'pony_types': pony_types
        }

        return template_context