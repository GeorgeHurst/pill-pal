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

  const diffHours = Math.floor(diff / 60).toString().padStart(2, '0');
  const diffMinutes = (diff % 60).toString().padStart(2, '0');

  return [diffHours, diffMinutes];
}





document.addEventListener('DOMContentLoaded', async ()=>{
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

        function updateNotifications() {
            noti_ul.innerHTML = "";
            const time = getCurrentTime();
            const [hour, min] = time.split(':');
        
            currentSchedule.forEach(slot => {
                const [slot_hour, slot_min] = slot.time.split(':');
                const [deltaHours, deltaMins] = getTimeDifferenceHHMM(slot.time, time);
        
                let message = ""; let colour = "";
        
                if (slot.time === time) {
                    message = `Your ${slot.time} dose is due now.<button class="noti-btn">CLEAR</button>`;
                    colour = "#34C759"
                } 
                else if (slot_hour > hour) {
                    if (deltaHours < 2) {
                        message = `Your ${slot.time} dose is due soon.<button class="noti-btn">CLEAR</button><br>(${deltaHours}h ${deltaMins}m remaining)`;
                        colour = "#FFC107"
                    }
                } 
                else if (slot_hour < hour) {
                    message = `Your ${slot.time} dose is overdue!<button class="noti-btn">CLEAR</button><br>(${deltaHours}h ${deltaMins}m overdue)`;
                    colour = "#CC0000"
                }
        
                if (message) {
                    const li = document.createElement("li");
                    li.innerHTML = message;
                    li.style.color = colour
                    noti_ul.appendChild(li);
                }
            });
        
            notification_div.appendChild(noti_ul);
        }
        
        updateNotifications()
        setInterval(updateNotifications, 60000); // 60000
        
        
    })