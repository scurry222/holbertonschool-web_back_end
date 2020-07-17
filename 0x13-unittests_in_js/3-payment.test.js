const sinon = require('sinon');
const { expect } = require('chai')
const sendPaymentRequestToApi = require('./3-payment.js');
// const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    const spy = sinon.spy(console, 'log');
  
    it('logs to the console the right messages', () => {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledWith('The total is: 120')).to.be.true;
        spy.restore();
    })
})
