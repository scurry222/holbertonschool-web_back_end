const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = require('chai');

chai.use(chaiHttp);

describe('API', () => {
  describe('GET /', () => {
    it('should return status code 200', () => {
      return chai.request('http://localhost:7865')
      .get('/', function(err, res) {
        if (err) throw err;
        expect(res).to.equal(200);
      })
    });

    it('should return the correct message', () => {
      return chai.request('http://localhost:7865')
      .get('/', function(err, res, body) {
        if (err) throw err;
        expect(body).to.equal('Welcome to the payment system');
      })
    });
  });

  describe('GET /cart/:id', () => {
    it('should return the correct status code and message', () => {
      return chai.request('http://localhost:7865')
      .get('/cart/12', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal(`Payment methods for cart 12`);
      });
    });
    it('should return 404 for a non-number id', () => {
      return chai.request('http://localhost:7865')
      .get('/cart/12', (err, res) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
    });
  });

  describe('GET /available_payments', () => {
    it('should return correct status code and message', () => {
      return chai.request('http://localhost:7865')
      .get('/available_payments', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.eql({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
      });
    });
  });
  describe('POST /login', () => {
    it('should return correct message if userName is passed', () => {
      chai.request('http://localhost:7865')
      .post('/login')
      .set({
        'method': 'POST',
        'headers': { 'Content-Type': 'application/json' }
      })
      .send({
        'body': { 'userName': 'Scout' },
        'json': 'true'
      }), (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Scout');
      }
    });

    it('should return 404 if userName is not passed', () => {
      chai.request('http://localhost:7865')
      .post('/login')
      .set ({
        'method': 'POST',
        'headers': { 'Content-Type': 'application/json' },
      })
      .send({
        'body': {},
        'json': true
      }), ((err, res, body) => {
          if (err) throw err;
          expect(res.statusCode).to.equal(404);
          expect(body).to.equal('Please provide a username');
        }
      );
    });
  });
});
