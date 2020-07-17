class Utils {
    static calculateNumber(type, a, b) {
        const aRounded = Math.round(a);
        const bRounded = Math.round(b);
    
        if (type === 'SUM') return aRounded + bRounded;
    
        else if (type === 'SUBTRACT') return aRounded - bRounded;
    
        else if (type === 'DIVIDE')
            return bRounded === 0 ? 'ERROR' : aRounded / bRounded;
    }
}

module.exports = Utils;
