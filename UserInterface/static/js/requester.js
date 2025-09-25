class Requester {
    constructor() {
        this.api = `${window.location.protocol}//${window.location.hostname}:5000/api`
    }

    /*********STANDALONE ENDPOINTS***********/
    async loadDataByType(type) {
        if (!type) return
        return fetch(this.api + `/load_data/${type}`)
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
        return fetch(this.api + `/save_data/${type}`,
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