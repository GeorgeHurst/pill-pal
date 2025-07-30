class Requester {
    constructor() {
        this.config = null
        this.api = "http://localhost:5000";
    }

    /*********STANDALONE ENDPOINTS***********/
    async loadDataByType(type) {
        if (!type) return
        return fetch(this.api + `/api/get/${type}`)
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
        return fetch(this.api + `/api/set/${type}`,
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

    /***************************************/
}