function faktorial(num) {
  let natija = 1;
  for (let i = 1; i <= num; i++) {
    natija = natija * i;
  }
  return natija;
}
console.log(faktorial(6));

