

function drawBasic(chartData) {
      var data = google.visualization.arrayToDataTable(chartData);

      var options = {
        hAxis: {
          title: 'Datetime'
        },
        vAxis: {
          title: 'Temperature (ºC)'
        },
        legend: {
            position: 'bottom'
            }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

      chart.draw(data, options);
    }