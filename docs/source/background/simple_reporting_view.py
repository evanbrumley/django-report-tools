def simple_reporting_view(request):
    # Gather data
    my_objects = MyObject.objects.all()

    # Generate chart 1
    chart1_data = gather_chart1_data(my_objects)
    chart1_options = {...}
    chart1_html = generate_chart_html(chart1_data, chart1_options)

    # Generate chart 2,3,4,5,6,7
    ...

    context = {
        'chart1': chart1,
        'chart2': chart2,
        ...
    }

    return render(request, 'mytemplate.html', context)
