from report_tools import reports
from report_tools import charts
from report_tools.chart_data import ChartData


def better_reporting_view(request):
    # Gather data
    my_objects = MyObject.objects.all()

    # Generate report
    report = MyReport(my_objects)

    context = {
        'report': report
    }

    return render(request, 'mytemplate.html', context)


class MyReport(reports.Report):
    renderer = MyRenderer

    chart1 = charts.PieChart(title="A nice, simple pie chart")
    chart2 = ...
    chart3 = ...

    def __init__(self, my_objects, *args, **kwargs):
        super(MyReport, self).__init__(*args, **kwargs)
        self.my_objects = my_objects

        # Here you could do any expensive calculations that
        # are needed for multiple charts

    def get_data_for_chart1(self):
        data = ChartData()

        # TODO: Fill data

        return data
