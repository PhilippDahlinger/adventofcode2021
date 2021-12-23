Logic logic = new Logic();
float tile_size = 40;
float off_x = 50;
float off_y = 50;
int a_x = 0;
int a_y = 1;
int selected = 0;
int s_x = 0;
int s_y = 0;
String[] labels = {"A", "B", "C", "D"};

void setup(){
  size(800, 400);
}


void render_board(){
   for (int i = 0; i < 13; i ++){
     for (int j = 0; j < 7; j++){
       String name = logic.pos[i][j];
       if ((selected == 1) && (i == s_x) && (j == s_y)){
         fill(255, 0, 0);
       } else if ((i == a_x) && (j == a_y)){
         fill(200);
       } else {
         if (name == "#"){
           fill(0);
         } else if (name == "A"){
           fill(100, 100, 255);
         } else if (name == "B"){
           fill(100, 255, 100);
         } else if (name == "C"){
           fill(200, 100, 100);
         } else if (name == "D"){
           fill(255, 255, 100);
         } else {
           fill(255);
         }
       }
       
       rect(off_x + tile_size * i, off_y + tile_size * j, tile_size, tile_size);
       fill(0);
       if (name != "#"){
         text(name, off_x + i*tile_size + tile_size/2, off_y + (j) * tile_size + tile_size / 2);  
       }
        
     }
   }
}

void render_turns(){
  fill(0);
  for (int i = 0; i < 4; i++) {
     text(labels[i], 600 + i*tile_size, 100);
     text(logic.turns[i], 600 + i * tile_size, 100 + tile_size);
  }
  
  text(logic.get_energy(), 600, 100 + 3 * tile_size);
  
}

void draw(){
  background(255);
  render_board(); 
  render_turns();
}


void keyPressed(){
  if (keyCode == RIGHT) {
    a_x += 1; 
  }
  else if (keyCode == LEFT) {
    a_x -= 1;
  }
  else if (keyCode == UP) {
    a_y -= 1; 
  }
  else if (keyCode == DOWN) {
    a_y += 1;
  }
  else if (key == ' ') {
     selected = 1 - selected;
     if (selected == 0) {
       logic.move(s_x, s_y, a_x, a_y);
     } else {
       s_x = a_x;
       s_y = a_y; 
     }
  } else if (key == BACKSPACE){
    logic.go_back_in_time(); 
  }
  
  
  if (a_x < 0){
    a_x = 0;
  }
  if (a_x >= 13){
    a_x = 12;
  }
  if (a_y < 0){
    a_y = 0;
  }
  if (a_y >= 7){
    a_y = 6;
  }  
  
}
