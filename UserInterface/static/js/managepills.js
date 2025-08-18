document.addEventListener('DOMContentLoaded', async() => {
    const pill_ul = document.getElementById("pill-ul")
    
    let pill_data = await fetch(`http://127.0.0.1:5000/api/get/pills`)
        .then(response => {
                    if (!response.ok) {
                        console.error(`Couldn't load pills: Network response was not ok`);
                    }
                    return response.json();
                })
                .then(data => { return data })
                .catch(console.error)

    for (let pill of pill_data) {
        if (!(pill.name == undefined)) {
            const li = document.createElement("li");
            li.innerHTML = `${pill.name} - ${pill.dosePerPill}mg per pill, ${pill.pillsPerDose * pill.dosesPerDay}x pills a day`
            pill_ul.appendChild(li)
        }
    }

    const backBtn = document.getElementById('backbutton')
    backBtn.addEventListener('click', ()=>{
        window.location = '/main';
    })
})