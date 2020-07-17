const { expect } = require('chai');
const request = require('request');

describe('API', () => {
  describe('GET index', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });

    it('should return the correct message', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        if (err) throw err;
        expect(body).to.equal('Welcome to the payment system');
      });
      done();
    });
  });
  describe('GET /cart/:id', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865/cart/12', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });
    it('should return the correct message', (done) => {
      request('http://localhost:7865/cart/12', (err, res, body) => {
        if (err) throw err;
        expect(body).to.equal(`Payment methods for cart 12`);
      });
      done();
    });
    it('should return 404 for a non-number id', (done) => {
      request('http://localhost:7865/cart/hello-v', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
      done();
    })
  })
  describe('GET /available_payments', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865/available_payments', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      });
      done();
    });
    it('should return the correct message', (done) => {
      request('http://localhost:7865/available_payments', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.eql({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
      });
      done();
    });
  });
  describe('POST /login', () => {
    it('should return correct message if userName is passed', (done) => {
      request({
          url: 'http://localhost:7865/login',
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: { userName: 'Scout' },
          json: true
        }, (err, res, body) => {
          if (err) throw err;
          expect(res.statusCode).to.equal(200);
          expect(body).to.equal('Welcome Scout');
        }
      );
      done();
    });

    it('should return 404 if userName is not passed', (done) => {
      request({
          url: 'http://localhost:7865/login',
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: { user: 'Scout' },
          json: true
        }, (err, res, body) => {
          if (err) throw err;
          expect(res.statusCode).to.equal(404);
          expect(body).to.equal('Please provide a username');
        }
      );
      done();
    });
  });
});
