const sinon = require('sinon');
const { expect } = require('chai')
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {

    const spy = sinon.spy(console, 'log');
  
    it('logs to the console the right messages', () => {
        const calcNumStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        calcNumStub.withArgs('SUM', 100, 20)
        sendPaymentRequestToApi();
        expect(spy.calledWith('The total is: 10')).to.be.true;
        spy.restore();
    })
})
