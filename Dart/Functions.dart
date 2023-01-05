void main() {
  // bool isNoble(int noble_number) => _nobleGases[noble_number] != null;

  const list = ['apples', 'oranges', 'bananas'];
  list
      .map((item) => item.toUpperCase())
      .forEach((item) => print('$item : ${item.length}'));
}
