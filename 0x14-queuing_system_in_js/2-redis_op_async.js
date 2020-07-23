import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const get = promisify(client.get).bind(client);

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

client.on('connect', () => {
    console.log('Redis client connected to the server')
})

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, reply) => {
        redis.print(`Reply: ${reply}`);
    });
}

async function displaySchoolValue(schoolName) {
    console.log(await get(schoolName));
}

(async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100')
    await displaySchoolValue('HolbertonSanFrancisco');
})()
