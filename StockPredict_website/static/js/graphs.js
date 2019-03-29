    google.charts.load('current', {'packages':['line']});
    google.charts.setOnLoadCallback(drawAppleChart);
    google.charts.setOnLoadCallback(drawXeroChart);
    google.charts.setOnLoadCallback(drawChaseChart);
    google.charts.setOnLoadCallback(drawNetflixChart);
    google.charts.setOnLoadCallback(drawNintendoChart);

    function drawAppleChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('number');
      data.addColumn('number');

      data.addRows([
        [1, 188.02],
        [2, 186.53],
        [3, 188.16],
        [4, 195.09],
        [5, 191.05],
        [6, 188.74],
        [7, 186.79],
        [8, 188.47],
        [9, 188.72],
        [10, 189.32],
        [11, {{apple}}]
      ]);

      var options = {
        chart: {
          title: 'Apple Closing Stock Chart',
          subtitle: '(USD)'
        },
        width: 500,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('applelinechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }

    function drawXeroChart() {
      var data = new google.visualization.DataTable();
      data.addColumn('number');
      data.addColumn('number');

      data.addRows([
        [1, 49.35],
        [2, 48.50],
        [3, 50.00],
        [4, 49.35],
        [5, 49.75],
        [6, 48.04],
        [7, 47.84],
        [8, 48.73],
        [9, 48.22],
        [10, 48.92],
        [11, {{xero}}]
      ]);

      var options = {
        chart: {
          title: 'Xero Closing Stock Chart',
          subtitle: '(AUD)'
        },
        width: 500,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('xerolinechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }

    function drawChaseChart() {
      var data = new google.visualization.DataTable();
      data.addColumn('number');
      data.addColumn('number');

      data.addRows([
        [1, 107.19],
        [2, 106.80],
        [3, 104.52],
        [4, 102.87],
        [5, 99.76],
        [6, 98.93],
        [7, 99.92],
        [8, 99.58],
        [9, 100.71],
        [10, 101.02],
        [11, {{chase}}]
      ]);

      var options = {
        chart: {
          title: 'Chase Bank Closing Stock Chart',
          subtitle: '(USD)'
        },
        width: 500,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('chaselinechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }

    function drawNintendoChart() {
      var data = new google.visualization.DataTable();
      data.addColumn('number');
      data.addColumn('number');

      data.addRows([
        [1, 107.19],
        [2, 106.80],
        [3, 104.52],
        [4, 102.87],
        [5, 99.76],
        [6, 98.93],
        [7, 99.92],
        [8, 99.58],
        [9, 100.71],
        [10, 101.02],
        [11, {{nintendo}}]
      ]);

      var options = {
        chart: {
          title: 'Nintendo Closing Stock Chart',
          subtitle: '(JPY)'
        },
        width: 500,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('nintendolinechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }

    function drawNetflixChart() {
      var data = new google.visualization.DataTable();
      data.addColumn('number');
      data.addColumn('number');

      data.addRows([
        [1, 363.44],
        [2, 358.78],
        [3, 375.22],
        [4, 377.87],
        [5, 361.01],
        [6, 366.23],
        [7, 359.97],
        [8, 353.37],
        [9, 354.61],
        [10, 355.27],
        [11, {{netflix}}]
      ]);

      var options = {
        chart: {
          title: 'Netflix Closing Stock Chart',
          subtitle: '(USD)'
        },
        width: 500,
        height: 500
      };

      var chart = new google.charts.Line(document.getElementById('netflixlinechart_material'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    }