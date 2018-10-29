// comments

/**
 * Awesome
 */

true;
false;
null;
undefined;
void 0;
1;
1.0;
/a/;
("a");
`a`;
`${a}`;

2 + 4;
4 - 2;
4 ** 4;

function awesome() {
  console.log("hi");
}

class Console {
  constructor() {
    super();
  }
  get hi() {}
}

class Console extends Awesome {
  constructor() {
    super();
  }
  get hi() {
    console.log("hi");
    let a = "awesome";
    a();
    awesome.log();
  }
}
