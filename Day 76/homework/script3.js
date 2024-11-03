const person = {
    name: "ლაშა",
    age: 30,
    profession: "პროგრამისტი",

    greet() {
        return `გამარჯობა, მე ვარ ${this.name}`;
    },
    changeProfession(newProfession) {
        this.profession = newProfession;
    },
    celebrateBirthday() {
        this.age += 1;
        return `გილოცავთ დაბადების დღეს, ${this.name}! ახლა ${this.age} წლის ხარ.`;
    }
};
