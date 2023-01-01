
document.querySelector('#watchlist').onclick = ()=>{
    console.log('watchlist')
    document.querySelector('#appointmnetbody').style.display = 'none';
    document.querySelector('#watchlistbody').style.display = 'block';
}

document.querySelector('#appointment').onclick = ()=>{
    console.log('appointmnet')
    document.querySelector('#watchlistbody').style.display = 'none';
    document.querySelector('#appointmnetbody').style.display = 'block';
}