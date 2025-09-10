var data;
let pills, global_schedule;
const requester = new Requester();


// async function main() {
//     pills = await getDataByType("pills")
//     global_schedule = await getDataByType("schedule");
// }

// main();

async function generateSchedule() {
    const toMinutes = (timeStr) => {
        const [h, m] = timeStr.split(":").map(Number);
        return h * 60 + m;
    };

    const toTimeString = (mins) => {
        const h = Math.floor(mins / 60);
        const m = mins % 60;
        return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
    };

    const user_preferences = await requester.getDataByType("user_preferences");
    const pill_data = await requester.getDataByType("pills")

    const start = toMinutes(user_preferences.ActiveHoursAM);
    const end = toMinutes(user_preferences.ActiveHoursPM);

    const totalActiveMinutes = end - start;

    const allDoses = [];
    const skippedPills = [];

    for (const pill of pill_data) {
        const {
            slotId, // <-- new
            name,
            dosePerPill,
            pillsPerDose,
            dosesPerDay,
            minHoursBetweenDoses
        } = pill;

        const minInterval = minHoursBetweenDoses * 60;
        const requiredTime = minInterval * (dosesPerDay - 1);

        // Human-friendly time format
        const readableRequiredTime = requiredTime >= 60
            ? `${(requiredTime / 60).toFixed(1)} hour${requiredTime >= 120 ? 's' : ''}`
            : `${requiredTime} minute${requiredTime > 1 ? 's' : ''}`;

        if (requiredTime > totalActiveMinutes) {
            skippedPills.push({
                name,
                reason: `Need ${readableRequiredTime} between ${dosesPerDay} doses, but only ${totalActiveMinutes} minutes available.`
            });
            continue;
        }

        // Schedule doses starting at active period start, spaced by minInterval
        let currentTime = start;
        for (let i = 0; i < dosesPerDay; i++) {
            if (currentTime > end) break;

            allDoses.push({
                time: currentTime,
                id: slotId,
                pill: name,
                amount: pillsPerDose
            });

            currentTime += minInterval;
        }
    }

    // Sort doses chronologically
    allDoses.sort((a, b) => a.time - b.time);

    // Group doses within timeThreshold minutes
    const groupedSchedule = [];
    const timeThreshold = 10; //minutes

    for (const dose of allDoses) {
        const lastGroup = groupedSchedule[groupedSchedule.length - 1];

        if (
            lastGroup &&
            Math.abs(lastGroup.time - dose.time) <= timeThreshold
        ) {
            const existing = lastGroup.pills.find(p => p.name === dose.pill);
            if (existing) {
                existing.amount += dose.amount;
            } else {
                lastGroup.pills.push({ id: dose.id, name: dose.pill, amount: dose.amount });
            }
        } else {
            groupedSchedule.push({
                time: dose.time,
                pills: [{ id: dose.id, name: dose.pill, amount: dose.amount }], //<- new
                taken: false
            });
        }
    }

    let schedule = groupedSchedule.map(entry => ({
        time: toTimeString(entry.time),
        pills: entry.pills,
        taken: entry.taken
    }))


    await requester.saveDataByType("schedule", schedule)
    await requester.saveDataByType("failed_schedule", skippedPills)
    
    return {
        schedule: groupedSchedule.map(entry => ({
            time: toTimeString(entry.time),
            pills: entry.pills,
            taken: entry.taken
        })),
        skippedPills
    }

}
  
// function loadData() {
//     fetch('http://localhost:5000/load_data/pills')
//     .then(response => response.json())
//     .then(data => {fillSlots(data)});
// }


// async function getDataByType(type) {
//     const response = await fetch(`http://localhost:5000/api/get/${type}`);
//     const data = await response.json();
//     return data;
// }



function getData(_data) {
   data = _data;
}

document.addEventListener('DOMContentLoaded', async() => {

    await fillSlots();

    const editBtn = document.getElementById('edit_btn');
    const pillDiv = document.getElementById('pill_div');
    const settingsBtn = document.getElementById('settings_btn')

    editBtn.addEventListener('click', () => {
        pillDiv.classList.toggle('editing');
        editBtn.textContent = pillDiv.classList.contains('editing') ? 'DONE' : 'EDIT';
        
    });

    settingsBtn.addEventListener('click', () => {
        window.location = "/settings" 
    });

    

    // This needs to be made specific for each info button
    document.querySelectorAll('.info_btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const pills = await requester.getDataByType('pills');
            let id = parseInt(btn.id[btn.id.length - 1]);
            if (!(pills[id].name == undefined)) {
                alert(`Pill Name: ${capitaliseFirstLetter(pills[id].name)}\nDose per pill: ${pills[id].dosePerPill}mg\nPills per dose: ${pills[id].pillsPerDose}\nDoses per day: ${pills[id].dosesPerDay}\nMin time between doses: ${pills[id].minHoursBetweenDoses} hrs`);
            }
            else {
                alert("Please fill this slot to view its information!")
            }
        });
    });

    document.querySelectorAll('.edit_pill_btn').forEach(btn => {
        btn.addEventListener('click', () => {
            let id = btn.id[btn.id.length - 1];
            window.location = "/edit_pill/slot_" + (parseInt(id)+1);
        });
    });


    // Loop through pill slots
    for (let i = 0; i < 4; i++) {
        const removeBtn = document.getElementById(`remove_pill_slot${i}`);
        const span = document.getElementById(`pill_span${i}`);

        if (removeBtn) {
            removeBtn.addEventListener('click', async() => {
                console.log(`Clearing slot ${i}`);

                await requester.removePill(i)
                await fillSlots()
            });
        }
    }

    document.getElementById('schedule_div').addEventListener('click', async (e) => {
        if (e.target && e.target.id === 'update_schedule_btn') {
            const scheduleDiv = document.getElementById('schedule_div');
            
            // Clear existing schedule
            scheduleDiv.innerHTML = '<h2>Schedule</h2><button id="update_schedule_btn" class="button">UPDATE</button><div class="table_wrapper"><table class="schedule_table"><thead><tr><th>Time</th><th>Pills (Amount)</th></tr></thead><tbody></tbody></table></div>';
            
            const tbody = scheduleDiv.querySelector('tbody');
            
            const schedule = await generateSchedule();
            
            // Populate new schedule
            schedule.schedule.forEach(entry => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${entry.time}</td><td>${entry.pills.map(p => `${capitaliseFirstLetter(p.name)} (${p.amount})`).join(',<br>')}</td>`;
                tbody.appendChild(row);
            });

            // Handle skipped pills
            if (schedule.skippedPills.length > 0) {
                const skippedDiv = document.createElement('div');
                skippedDiv.className = 'skipped_pills';
                skippedDiv.innerHTML = '<h3>Skipped Pills</h3>';
                skippedDiv.innerHTML += '<ul>' + schedule.skippedPills.map(p => `<li>${p.name}: ${p.reason}</li>`).join('') + '</ul>';
                scheduleDiv.appendChild(skippedDiv);
            }
        }
    });

})

async function fillSlots() {
    let data = await requester.getDataByType("Pills")
    for (const pillIndex in data) {
        let name = data[pillIndex].name;
        document.getElementById(`pill_span${pillIndex}`).innerText = (name) ? capitaliseFirstLetter(name) : "FREE SLOT";
    }


}

function capitaliseFirstLetter(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}