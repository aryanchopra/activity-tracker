const searchField = document.querySelector('#searchField')
const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')
const paginationContainer= document.querySelector('.pagination-container')
const tableBody = document.querySelector('.table-body');
const noResults= document.querySelector('.no-results');
tableOutput.style.display='none';

searchField.addEventListener('keyup',(e)=>{
    const searchValue=e.target.value;
    if(searchValue.length>0){
        paginationContainer.style.display='none';
        tableBody.innerHTML='';
        console.log('search value',searchValue);
        fetch('/search-activity',{
            body: JSON.stringify({searchText:searchValue}),
            method:'POST',
        })
        .then((res)=>res.json())
        .then((data)=>{

            console.log('data',data)
            appTable.style.display='none';
            tableOutput.style.display='block';
            if(data.length===0){
                noResults.style.display='block';
                tableOutput.style.display='none';

            } else{
                data.forEach((item) => {
                    noResults.style.display='none';
                    tableBody.innerHTML+=`
                        <tr>
                            <td>${item.date} </td>
                            <td>${item.sleep}</td>
                            <td>${item.qsleep}</td>
                            <td>${item.classes}</td>
                            <td>${item.workout}</td>
                            <td>${item.qday}</td>
                            <td>${item.project}</td>
                            <td>${item.phours}</td>   
                        </tr>
                        `;
                });
            }
        }
        );
        
    }
    else{
        tableOutput.style.display='none';
        appTable.style.display='block';
        paginationContainer.style.display='block';
    }

});