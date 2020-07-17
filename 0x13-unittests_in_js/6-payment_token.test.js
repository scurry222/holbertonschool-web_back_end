const { expect } = require('chai');
const getPaymentTokenFromApi = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
    it('should return true when true is passed', (done) => {
        getPaymentTokenFromApi(true).then(function(res) {
            expect(res).to.eql({ data: 'Successful response from the API' })
        })
        done();
    })
})
