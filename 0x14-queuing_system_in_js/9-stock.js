import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
    {
        itemId: 1,
        itemName: 'Suitcase 250',
        price: 50,
        initialAvailableQuantity: 4
    },
    {
        itemId: 2,
        itemName: 'Suitcase 450',
        price: 100,
        initialAvailableQuantity: 10
    },
    {
        itemId: 3,
        itemName: 'Suitcase 650',
        price: 350,
        initialAvailableQuantity: 2
    },
    {
        itemId: 4,
        itemName: 'Suitcase 1050',
        price: 550,
        initialAvailableQuantity: 5
    }
]

const getItemById = (id) => listProducts[id];

const app = express();

app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)))

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (item) {
        item.currentQuantity = await getCurrentReservedStockById(itemId);
        res.send(JSON.stringify(item));
        return;
    }
    res.status(404).send(JSON.stringify({status: 'Product not found'}));
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);

    if (!item) {
        res.status(404).send(
            JSON.stringify({
                status: 'Product not found',
            })
        );
        return;
    }
    const stock = await getCurrentReservedStockById(itemId);
    if (stock < 1) {
        res.status(403).send(
            JSON.stringify({
                status: 'Not enough stock available',
                itemId
            })
        );
        return;
    }
    reserveStockById(itemId, stock);
    res.send(JSON.stringify({
        status: 'Reservation confirmed',
        itemId
    }))
})

app.listen('1245', () => {
    listProducts.forEach((product) => reserveStockById(product.itemId,
        product.initialAvailableQuantity));
})

const client = redis.createClient();
const get = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => client.set(itemId, stock);

async function getCurrentReservedStockById(itemId) { return await get(itemId) }
