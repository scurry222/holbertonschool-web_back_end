module.exports = function getPaymentTokenFromAPI(success) {
    if (success === true) return new Promise((resolve, reject) => {
        return resolve({ data: 'Successful response from the API' })
    })
}
