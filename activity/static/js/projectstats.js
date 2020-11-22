const renderChart=(data,labels)=>{
    var ctx = document.getElementById('projectChart').getContext('2d');
    var myChart = new Chart(ctx, {
        data: {labels: labels,
        datasets:[{
            data: data,
        }],
        fillOpacity:.3,
        
        },
        type: 'polarArea',
        options: {
            

            plugins: {
        
              colorschemes: {
        
                scheme: 'brewer.PastelTwo3'
        
              }
        
            },

            config: {
                animation : {
                    animateScale : false
                }
            }
        
          }
    });
}
        


const getChartData=()=>{
    fetch('/get_data').then(res=>res.json()).then((data)=>{
        console.log('data',data)
        
        const projectdata = data.project_data

        const [projectvalues,projectkeys]=[Object.values(projectdata),Object.keys(projectdata)]

        renderChart(projectvalues,projectkeys)
    })
}
document.onload=getChartData();