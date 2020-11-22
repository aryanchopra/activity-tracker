const renderChart=(data1,data2,data3,labels)=>{
    var ctx = document.getElementById('dayChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        
        data: {
            labels: labels,
            datasets: [{
                type: 'line',
                label: 'Quality of Day',
                data: data1,
                fill:false,
                borderWidth: 0,
               
                
            },{
                type: 'bar',
                label: 'Sleep Quality',
                data: data2,
                borderWidth: 1,
               
            },
            {
                type: 'bar',
                label: 'Hours of Workout',
                data: data3,
                borderWidth: 1,
               
            },
            
            ]
        },
        options: {

            plugins: {
        
              colorschemes: {
        
                scheme: 'brewer.PastelOne3'
        
              }
        
            }
        
          }
    });
}

const getChartData=()=>{
    fetch('/get_data').then(res=>res.json()).then((data)=>{
        console.log('data',data)
        
        const classesdata= data.classes_data
        const qdaydata=data.qday_data
        const workoutdata=data.workout_data
        const qsleepdata= data.qsleep_data


        const [classesvalues,qdayvalues,workoutvalues,qsleepvalues,qsleepkeys]=[Object.values(classesdata),Object.values(qdaydata),Object.values(workoutdata),Object.values(qsleepdata),Object.keys(qsleepdata)]
       
        renderChart(qdayvalues,qsleepvalues,workoutvalues,qsleepkeys);
        
    })
}
document.onload=getChartData();