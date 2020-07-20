module.exports = function calculateNumber(type, a, b) {
    const aActual = Math.round(a);
    const bActual = Math.round(b);

    if (type === 'SUM') return aActual + bActual;

    else if (type === 'SUBTRACT') return aActual - bActual;

    else if (type === 'DIVIDE')
        return bActual === 0 ? 'Error' : aActual / bActual;
}
