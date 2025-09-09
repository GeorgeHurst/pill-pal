let enteredPin = ""

// const requester = new Requester();

function press(value) {

    if (value == 'clear') {
        document.getElementById('pincode').innerText = "";
        enteredPin = "";
        return;
    }
    else if (value == 'enter') {

        if (enteredPin != "") {

            fetch('http://127.0.0.1:5000/api/authenticate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ passcode: enteredPin })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location = "/main"
                } else {
                    alert("Access Denied");
                }
            })
            .catch(error => console.error('Error:', error));
    
            document.getElementById('pincode').innerText = "";
            enteredPin = "";
            return;
        }
    }
    else if (enteredPin.length < 6) {
        document.getElementById('pincode').innerText += "*\u00A0";
        enteredPin += value;
        return;
    }

}


// Main Page
function updateClock() {
    const now = new Date();

    const date = now.getDate();
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const month = monthNames[now.getMonth()];

    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    const formattedTime = `${date} ${month} ${hours}:${minutes}:${seconds}`;
    document.getElementById('time').textContent = formattedTime;

}

updateClock(); 
setInterval(updateClock, 1000); 




menuButton.addEventListener('click', () => {
    sidePane.classList.toggle('open');
});


document.addEventListener('click', (event) => {
    if (!sidePane.contains(event.target) && !menuButton.contains(event.target)) {
        sidePane.classList.remove('open');
    }
});


// function updateTimeDifference() {
//     const targetTime = "14:30"; // Time from your HTML
//     const [targetHour, targetMinute] = targetTime.split(":").map(Number);

//     const now = new Date();
//     const target = new Date(now);
//     target.setHours(targetHour, targetMinute, 0, 0);

//     // If target time is in the past today, adjust for tomorrow
//     if (target < now) {
//       target.setDate(target.getDate() + 1);
//     }

//     const diffMs = target - now;
//     const diffMins = Math.floor(diffMs / 60000);
//     const hours = Math.floor(diffMins / 60);
//     const minutes = diffMins % 60;

//     const display = `${hours}h ${minutes}m`;

//     document.querySelector(".time-diff").textContent = display;
//   }

//   updateTimeDifference();
//   setInterval(updateTimeDifference, 60000);

function capitaliseFirstLetter(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

// Returns the time in HH:MM format
function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

function getTimeDifferenceHHMM(time1, time2) {
  const [h1, m1] = time1.split(':').map(Number);
  const [h2, m2] = time2.split(':').map(Number);

  const minutes1 = h1 * 60 + m1;
  const minutes2 = h2 * 60 + m2;

  let diff = Math.abs(minutes1 - minutes2);
  diff = Math.min(diff, 1440 - diff); // Handle day wrap-around

  const diffHours = Math.floor(diff / 60)
  const diffMinutes = (diff % 60)

  return [diffHours, diffMinutes];
}





document.addEventListener('DOMContentLoaded', async ()=>{

document.addEventListener("selectstart", e => e.preventDefault());
document.addEventListener("dragstart", e => e.preventDefault());

    let currentSchedule = await fetch(`http://127.0.0.1:5000/api/get/schedule`)
    .then(response => {
                if (!response.ok) {
                    console.error(`Couldn't load data schedule: Network response was not ok`);
                }
                return response.json();
            })
            .then(data => { return data })
            .catch(console.error)
            
            const schedule_div = document.getElementById('schedule-div')
            const notification_div = document.getElementById('notification-div')

            const ul = document.createElement("ul");
            
            let prevTime = "";

            currentSchedule.forEach(slot => {
                slot.pills.forEach( pill => {
                    const li = document.createElement("li");
                    if (slot.time === prevTime) {
                        li.innerHTML = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + `- ${capitaliseFirstLetter(pill.name)} x${pill.amount} `;
                    }
                    else {
                        li.innerHTML = `${slot.time} - ${capitaliseFirstLetter(pill.name)} x${pill.amount} `;
                    }
                    ul.appendChild(li);
                    prevTime = slot.time
                });
        })

        schedule_div.appendChild(ul);
        
        
    const noti_ul = document.createElement("ul");
    const clearedNotifications = new Set();

    let currentDay = new Date().toDateString(); 

    noti_ul.addEventListener("click", (event) => {
    if (event.target.classList.contains("noti-btn")) {
        const li = event.target.closest("li");
        const timeKey = li.getAttribute("data-time");
        clearedNotifications.add(timeKey);
        li.remove();
    }
    });

    const reset_notiBtn = document.getElementById('reset-noti-btn')
    reset_notiBtn.addEventListener('click', ()=>{
        clearedNotifications.clear();
        updateNotifications();
    })

    const DUE_SOON_MIN = 120;
    const DUE_GRACE_MIN = 5;

    const toMinutes = (hhmm) => {
    const [h, m] = hhmm.split(':').map(n => parseInt(n, 10));
    return h * 60 + m;
    };
    const hmFromMinutes = (minsAbs) => {
    const h = Math.floor(minsAbs / 60);
    const m = minsAbs % 60;
    return [h, m];
    };

    function updateNotifications() {
    const today = new Date().toDateString();

    if (today !== currentDay) {
        clearedNotifications.clear();
        noti_ul.innerHTML = "";
        currentDay = today;
    }

    noti_ul.innerHTML = "";

    const nowStr = getCurrentTime();
    // const nowStr = "15:36";

    const nowMin = toMinutes(nowStr);

    currentSchedule.forEach(slot => {
        if (clearedNotifications.has(slot.time)) return;

        const slotMin = toMinutes(slot.time);
        const diff = slotMin - nowMin;

        let message = "";
        let colour  = "";

        //        V                        V    REMOVED = SIGN
        if (diff >= -DUE_GRACE_MIN && diff <= 0) {
            const minsUntilOverdue = DUE_GRACE_MIN + diff;
            message = `Your ${slot.time} dose is due now. <button class="noti-btn">CLEAR</button><br>(${minsUntilOverdue}m until overdue)`;
            colour = "#34C759";
        } else if (diff > 0 && diff <= DUE_SOON_MIN) {
            const [h, m] = hmFromMinutes(diff);
            message = `Your ${slot.time} dose is due soon. <button class="noti-btn">CLEAR</button><br>(${h}h ${m}m remaining)`;
            colour = "#FFC107";
        } else if (diff < -DUE_GRACE_MIN) {
            const [h, m] = hmFromMinutes(-diff);
            message = `Your ${slot.time} dose is overdue! <button class="noti-btn">CLEAR</button><br>(${h}h ${m}m overdue)`;
            colour = "#CC0000";
        } else {
            return
        }

        const li = document.createElement("li");
        li.setAttribute("data-time", slot.time);
        li.innerHTML = message;
        li.style.color = colour;
        noti_ul.appendChild(li);
    });

    notification_div.appendChild(noti_ul);
}


        
    function startNotificationLoop() {

        updateNotifications();


        const now = new Date();
        const msUntilNextMinute = (60 - now.getSeconds()) * 1000 - now.getMilliseconds();


        setTimeout(() => {
            updateNotifications();


            setInterval(updateNotifications, 60000);

        }, msUntilNextMinute);
    }

    startNotificationLoop();
        
        
    
})

