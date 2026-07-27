function countVowels(str) {
    const vowels='aeiouAeiou';
    let count=0;
    let consonants=0;
    for(i=0;i<str.length;i++){
        if(vowels.includes(str[i])){
            count++;
        }
        
    }
    return count;
}
console.log(countVowels("JavaScript"))