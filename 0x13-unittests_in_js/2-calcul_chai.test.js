const { ShouldThrow, expect } = require('chai');
const calculateNumber = require('./1-calcul.js');


describe('calculateNumber', () => {
    it('correctly adds 1 and 3', () => {
        expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    })
    it('correctly adds 2.7 and 5.7', () => {
        expect(calculateNumber('SUM', 2.7, 5.7)).to.equal(9);
    })
    it('correctly adds 0 and 1.1', () => {
        expect(calculateNumber('SUM', 0, 1.1)).to.equal(1);
    })
    it('correctly adds -1.1 and 1.1', () => {
        expect(calculateNumber('SUM', -1.1, 1.1)).to.equal(0);
    })
    it('correctly adds 3.5 and 1.5', () => {
        expect(calculateNumber('SUM', 3.5, 1.5)).to.equal(6);
    })
    it('correctly adds 3.9999999 and 1', () => {
        expect(calculateNumber('SUM', 3.9999999, 1)).to.equal(5);
    })
    it('correctly adds -0.4999999 and 0', () => {
        expect(calculateNumber('SUM', -0.4999999, 0)).to.equal(0);
    })
    it('correctly adds 0 and 0', () => {
        expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    })
    it('correctly subtracts 1 and 3', () => {
        expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
    })
    it('correctly subtracts 2.7 and 5.7', () => {
        expect(calculateNumber('SUBTRACT', 2.7, 5.7)).to.equal(-3);
    })
    it('correctly subtracts 0 and 1.1', () => {
        expect(calculateNumber('SUBTRACT', 0, 1.1)).to.equal(-1);
    })
    it('correctly subtracts -1.1 and 1.1', () => {
        expect(calculateNumber('SUBTRACT', -1.1, 1.1)).to.equal(-2);
    })
    it('correctly subtracts 3.5 and 1.5', () => {
        expect(calculateNumber('SUBTRACT', 3.5, 1.5)).to.equal(2);
    })
    it('correctly subtracts 3.9999999 and 1', () => {
        expect(calculateNumber('SUBTRACT', 3.9999999, 1)).to.equal(3);
    })
    it('correctly subtracts -0.4999999 and 0', () => {
        expect(calculateNumber('SUBTRACT', -0.4999999, 0)).to.equal(0);
    })
    it('correctly subtracts 0 and 0', () => {
        expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    })
    it('correctly divides 1 and 3', () => {
        expect(calculateNumber('DIVIDE', 1, 3)).to.equal(0.3333333333333333);
    })
    it('correctly divides 2.7 and 5.7', () => {
        expect(calculateNumber('DIVIDE', 2.7, 5.7)).to.equal(0.5);
    })
    it('correctly divides 0 and 1.1', () => {
        expect(calculateNumber('DIVIDE', 0, 1.1)).to.equal(0);
    })
    it('correctly divides -1.1 and 1.1', () => {
        expect(calculateNumber('DIVIDE', -1.1, 1.1)).to.equal(-1);
    })
    it('correctly divides 3.5 and 1.5', () => {
        expect(calculateNumber('DIVIDE', 3.5, 1.5)).to.equal(2);
    })
    it('correctly divides 3.9999999 and 1', () => {
        expect(calculateNumber('DIVIDE', 3.9999999, 1)).to.equal(4);
    })
    it('correctly divides -0.4999999 and 0', () => {
        expect(calculateNumber('DIVIDE', -0.4999999, 0)).to.equal('ERROR');
    })
    it('correctly divides 0 and 0', () => {
        expect(calculateNumber('DIVIDE', 0, 0)).to.equal('ERROR');
    })
})
