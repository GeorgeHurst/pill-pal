class Requester {
    constructor() {
        this.config = null
        this.api = "http://127.0.0.1:5000/api";
    }

    /*********STANDALONE ENDPOINTS***********/
    async getDataByType(type) {
        if (!type) return
        return fetch(this.api + `/get/${type}`)
            .then(response => {
                if (!response.ok) {
                    console.error(`Couldn't load data of type - ${type}: Network response was not ok`);
                }
                return response.json();
            })
            .then(data => { return data })
            .catch(console.error)
    }

    async saveDataByType(type, data) {
        if (!type || !data || data.length == 0) return
        return fetch(this.api + `/set/${type}`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => { return response.json(); })
        .catch(console.error)
    }

    async getPillDataBySlot(slot) {
        if (parseInt(slot) < 0 || parseInt(slot) > 3) return
        return fetch(this.api + `/get/pill/${slot}`)
            .then(response => {
                if (!response.ok) {
                    console.error(`Couldn't load data for pill slot ${type}: Network response was not ok`);
                }
                return response.json();
            })
            .then(data => { return data })
            .catch(console.error)
    }

    async savePillSlotData(slot, data) {
        if (!slot || !data || data.length == 0) return
        return fetch(this.api + `/set/pill/${slot}`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => { return response.json(); })
        .catch(console.error)
    }

    async removePill(slot) {
        if (!slot) return
        return fetch(this.api + `/remove/pill/${slot}`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => { return response.json(); })
    }

    /***************************************/
}
