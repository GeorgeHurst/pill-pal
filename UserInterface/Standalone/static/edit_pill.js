const requester = new Requester();


document.addEventListener('DOMContentLoaded', async() => {
    const slotId = document.getElementById('pill-data').dataset.slotId;

    // const form = document.querySelector('.edit_form form');
    const pillSubmitButton = document.getElementById('pillSubmitButton');
    const nameInput = document.getElementById('name');
    const dosePerPillInput = document.getElementById('dosePerPill');
    const pillsPerDoseInput = document.getElementById('pillsPerDose');
    const dosesPerDayInput = document.getElementById('dosesPerDay');
    const minHoursBetweenDosesInput = document.getElementById('minHoursBetweenDoses');

    let data = await requester.getPillDataBySlot(slotId);

    console.log("DATA: ",data);

    nameInput.value = data.name ? data.name : "";
    dosePerPillInput.value = data.dosePerPill;
    pillsPerDoseInput.value = data.pillsPerDose;
    dosesPerDayInput.value = data.dosesPerDay;
    minHoursBetweenDosesInput.value = data.minHoursBetweenDoses;

    console.log(slotId)

    pillSubmitButton.addEventListener('click', () => {
        newPillData = {
            "slotId": slotId,
            "dosePerPill": dosePerPillInput.value,
            "dosesPerDay": dosesPerDayInput.value,
            "minHoursBetweenDoses": minHoursBetweenDosesInput.value,
            "name": nameInput.value,
            "pillsPerDose": pillsPerDoseInput.value
        }
        requester.savePillSlotData(slotId, newPillData)

        window.location = "/";
    })


})

