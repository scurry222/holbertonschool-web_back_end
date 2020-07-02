import Currency from './3-currency';

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    set amount(amount) {
        this.amount = amount;
    }
    get amount() {
        return this._amount;
    }

    set currency(currency) {
        this.currency = currency;
    }
    get currency() {
        return this._currency;
    }

    displayFullPrice() {
        return `${this.amount} ${this.currency.displayFullCurrency()}`;
    }

    convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}