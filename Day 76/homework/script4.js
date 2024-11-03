function findSmallestAndLargestWords(text) {
    const words = text.split(' ');
    let smallest = words[0];
    let largest = words[0];

    for (const word of words) {
        if (word.length < smallest.length) smallest = word;
        if (word.length > largest.length) largest = word;
    }

    return [smallest, largest];
}
