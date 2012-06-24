======================
GoogleChart関連
======================

HTML埋め込み
---------------

アンケート結果は昨年(2011年4月5日)開催の神戸ITフェスティバル( http://s2011.kobe-it-fes.org/ )の回答から。

今年の神戸ITフェスティバルは10月5日、6日の2日間( http://kobe-it-fes.org/ )

.. raw:: html

    2011年神戸ITフェスアンケート結果<br />
    Googlechart
    <p>
      年代<br />
      <div id="chart_div_age" style="width: 450px; height: 300px;"></div>
    </p>
    <p>
      住所<br />
      <div id="chart_div_site" style="width: 450px; height: 300px;"></div>
    </p>
    <p>
      職業<br />
      <div id="chart_div_job" style="width: 450px; height: 300px;"></div>
    </p>

    または Google Charts で画像にするなど<br />
    <p>
      年代<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:6,81,67,36,18,4&chs=450x200&chl=10代|20代|30代|40代|50代|60代以上&chtt=年代&chco=00ff00"  alt="" />  
    </p>

    <p>
      住所<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:92,22,34,5&chs=450x200&chl=神戸市内|他兵庫県内|大阪府|京都府&chtt=住所&chco=0000ff"  alt="" />  
    </p>

    <p>
      職業<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:6,81,67,36,18,4&chs=450x200&chl=学生|IT系企業'|非IT系企業|その他企業、団体、個人&chtt=職業&chco=ff0000"  alt="" />  
    </p>

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
      
        var data_age = google.visualization.arrayToDataTable([
          ['年代', '回答数'],
          ['10代', 6],
          ['20代',     81],
          ['30代',      67],
          ['40代',  36],
          ['50代', 18],
          ['60代以上',    4]
        ]);

        var options_age = {
          title: 'あなたの年齢は'
        };

        var data_site = google.visualization.arrayToDataTable([
          ['住所', '回答数'],
          ['神戸市内', 92],
          ['他兵庫県内',     22],
          ['大阪府',      34],
          ['京都府',  5]
        ]);

        var options_site = {
          title: 'どこから来られましたか'
        };

        var data_job = google.visualization.arrayToDataTable([
          ['項目', '回答数'],
          ['学生',54],
          ['IT系企業', 75],
          ['非IT系企業', 32],
          ['その他企業、団体、個人', 59]
        ]);

        var options_job = {
          title: 'あなたの職業は'
        };


        var chart_age = new google.visualization.PieChart(document.getElementById('chart_div_age'));
        chart_age.draw(data_age, options_age);

        var chart_site = new google.visualization.PieChart(document.getElementById('chart_div_site'));
        chart_site.draw(data_site, options_site);

        var chart_job = new google.visualization.PieChart(document.getElementById('chart_div_job'));
        chart_job.draw(data_job, options_job);
        
      }
    </script>

.. code-block:: html

    2011年神戸ITフェスアンケート結果<br />
    Googlechart
    <p>
      年代<br />
      <div id="chart_div_age" style="width: 450px; height: 300px;"></div>
    </p>
    <p>
      住所<br />
      <div id="chart_div_site" style="width: 450px; height: 300px;"></div>
    </p>
    <p>
      職業<br />
      <div id="chart_div_job" style="width: 450px; height: 300px;"></div>
    </p>

    または Google Charts で画像にするなど<br />
    <p>
      年代<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:6,81,67,36,18,4&chs=450x200&chl=10代|20代|30代|40代|50代|60代以上&chtt=年代&chco=00ff00"  alt="" />  
    </p>

    <p>
      住所<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:92,22,34,5&chs=450x200&chl=神戸市内|他兵庫県内|大阪府|京都府&chtt=住所&chco=0000ff"  alt="" />  
    </p>

    <p>
      職業<br />
      <img src="http://chart.apis.google.com/chart?cht=p&chd=t:6,81,67,36,18,4&chs=450x200&chl=学生|IT系企業'|非IT系企業|その他企業、団体、個人&chtt=職業&chco=ff0000"  alt="" />  
    </p>

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
      
        var data_age = google.visualization.arrayToDataTable([
          ['年代', '回答数'],
          ['10代', 6],
          ['20代',     81],
          ['30代',      67],
          ['40代',  36],
          ['50代', 18],
          ['60代以上',    4]
        ]);

        var options_age = {
          title: 'あなたの年齢は'
        };

        var data_site = google.visualization.arrayToDataTable([
          ['住所', '回答数'],
          ['神戸市内', 92],
          ['他兵庫県内',     22],
          ['大阪府',      34],
          ['京都府',  5]
        ]);

        var options_site = {
          title: 'どこから来られましたか'
        };

        var data_job = google.visualization.arrayToDataTable([
          ['項目', '回答数'],
          ['学生',54],
          ['IT系企業', 75],
          ['非IT系企業', 32],
          ['その他企業、団体、個人', 59]
        ]);

        var options_job = {
          title: 'あなたの職業は'
        };


        var chart_age = new google.visualization.PieChart(document.getElementById('chart_div_age'));
        chart_age.draw(data_age, options_age);

        var chart_site = new google.visualization.PieChart(document.getElementById('chart_div_site'));
        chart_site.draw(data_site, options_site);

        var chart_job = new google.visualization.PieChart(document.getElementById('chart_div_job'));
        chart_job.draw(data_job, options_job);
        
      }
    </script>
