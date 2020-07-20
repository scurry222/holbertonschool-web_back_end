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
    })
  })
})
