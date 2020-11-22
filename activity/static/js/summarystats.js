// const renderChart=(data1,data2,data3,labels)=>{
//     var ctx = document.getElementById('summaryChart').getContext('2d');
//     var myChart = new Chart(ctx, {
//         type: 'bar',
        
//         data: {
//             labels: labels,
//             datasets: [{
//                 type: 'line',
//                 label: 'Quality of Day',
//                 data: data1,
//                 fill:false,
//                 borderWidth: 0,
               
                
//             },{
//                 type: 'bar',
//                 label: 'Sleep Quality',
//                 data: data2,
//                 borderWidth: 1,
               
//             },
//             {
//                 type: 'bar',
//                 label: 'Hours of Workout',
//                 data: data3,
//                 borderWidth: 1,
               
//             },
            
//             ]
//         },
//         options: {

//             plugins: {
        
//               colorschemes: {
        
//                 scheme: 'brewer.PastelTwo3'
        
//               }
        
//             }
        
//           }
//     });
// }
const renderChart=(data,labels)=>{
    var ctx = document.getElementById('summaryChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        
        data: {
            labels:['Projects','Classes','Workout','Sleep'],
            datasets:[{
                data:data
            }]
            },
        options: {

            plugins: {
        
              colorschemes: {
        
                scheme: 'brewer.DarkTwo6'
        
              }
        
            }
        
          }
    });
}

const sleepAvg = document.getElementById('sleepavg')
const workoutAvg = document.getElementById('workoutavg')
const classAvg = document.getElementById('classavg')
const projectAvg = document.getElementById('projectavg')

const getChartData=()=>{
    fetch('/get_data').then(res=>res.json()).then((data)=>{
        console.log('data',data)
        
        const classesdata= data.classes_data
        const qdaydata=data.qday_data
        const workoutdata=data.workout_data
        const qsleepdata= data.qsleep_data
        const totaldata= data.total
        const avgdata= data.averages
        
        sleepAvg.innerHTML=avgdata.sleep;
        workoutAvg.innerHTML=avgdata.workout;
        classAvg.innerHTML=avgdata.classes;
        projectAvg.innerHTML=avgdata.project;



        const [classesvalues,qdayvalues,workoutvalues,qsleepvalues,qsleepkeys]=[Object.values(classesdata),Object.values(qdaydata),Object.values(workoutdata),Object.values(qsleepdata),Object.keys(qsleepdata)]
        const [totaldatakeys,totaldatavalues]=[Object.keys(totaldata),Object.values(totaldata)]
        renderChart(totaldatavalues,totaldatakeys);
        
    })
}
document.onload=getChartData();



