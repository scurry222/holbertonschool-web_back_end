const chai = require('chai');
const chaiHttp = require('chai-http');
const { expect } = require('chai');

chai.use(chaiHttp);

describe('API', () => {
  describe('GET /', () => {
    it('should return status code 200', () => {
      chai.request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
      })
    });

    it('should return the correct message', () => {
      chai.request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        if (err) throw err;
        expect(res.text).to.equal('Welcome to the payment system');
      })
    });
  })

  describe('GET /cart/:id', () => {
    it('should return the correct status code and message', () => {
      chai.request('http://localhost:7865')
      .get('/cart/12', (err, res, body) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(200);
        expect(body.text).to.equal(`Payment methods for cart 12`);
      });
    });
    it('should return 404 for a non-number id', () => {
      chai.request('http://localhost:7865')
      .get('/cart/hello -v')
      .end((err, res) => {
        if (err) throw err;
        expect(res.statusCode).to.equal(404);
      });
    })
  })
})
