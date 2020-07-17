const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
    it('correctly adds 1 and 3', () => {
        assert.equal(calculateNumber(1, 3), 4)
    })
    it('correctly adds 2.7 and 5.7', () => {
        assert.equal(calculateNumber(2.7, 5.7), 9)
    })
    it('correctly adds 0 and 1.1', () => {
        assert.equal(calculateNumber(0, 1.1), 1)
    })
    it('correctly adds -1.1 and 1.1', () => {
        assert.equal(calculateNumber(-1.1, 1.1), 0)
    })
    it('correctly adds 3.5 and 1.5', () => {
        assert.equal(calculateNumber(3.5, 1.5), 6)
    })
    it('correctly adds 3 and 1.5', () => {
        assert.equal(calculateNumber(3, 1.5), 5)
    })
    it('correctly adds 3.9999999 and 1', () => {
        assert.equal(calculateNumber(3.9999999, 1), 5)
    })
    it('correctly adds -0.4999999 and 0', () => {
        assert.equal(calculateNumber(-0.4999999, 0), 0)
    })
    it('correctly adds 0 and 0', () => {
        assert.equal(calculateNumber(0, 0), 0)
    })
})
