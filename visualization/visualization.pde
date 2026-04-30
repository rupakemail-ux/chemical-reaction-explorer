void setup() {
  size(600, 400);
  background(255);
}

void draw() {
  fill(200, 0, 0);
  ellipse(200, 200, 50, 50); // Atom 1
  fill(0, 0, 200);
  ellipse(400, 200, 50, 50); // Atom 2
  stroke(0);
  line(200, 200, 400, 200);  // Bond forming
}
