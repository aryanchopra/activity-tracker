const renderChart=(data,data2,labels)=>{
    var ctx = document.getElementById('sleepChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Hours of Sleep',
                data: data,
                
                borderWidth: 0,
                fill:false
                
            },{
                label: 'Sleep Quality',
                data: data2,
                borderWidth: 1,
                fill:false
            }
            ]
        },
        options: {

            plugins: {
        
              colorschemes: {
        
                scheme: 'brewer.PastelTwo3'
        
              }
        
            }
        
          }
    });
}

const getChartData=()=>{
    fetch('/get_data').then(res=>res.json()).then((data)=>{
        const sleepdata=data.sleep_data;
        const qsleepdata=data.qsleep_data;
        const [sleepvalues,qsleepvalues,sleeplabels]=[Object.values(sleepdata),Object.values(qsleepdata),Object.keys(sleepdata)]
        renderChart(sleepvalues,qsleepvalues,sleeplabels);
    })
}
document.onload=getChartData();
