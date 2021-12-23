import java.util.LinkedList;

public class Logic{
   String[][] pos = new String[13][7];
   int[] turns = new int[4];
   LinkedList<String[][]> history_pos = new LinkedList<String[][]>();
   LinkedList<int[]> history_turns = new LinkedList<int[]>();
   int history_pointer = -1;
   
   public Logic(){
     for (int i = 0; i < 4; i++){
       turns[i] = 0; 
     }
     for (int j= 0; j < 7; j++){
       for (int i = 0; i < 13; i++){
         pos[i][j] = "#";  
       }
     }
     
     for (int i = 1; i < 12; i++) {
       this.pos[i][1] = "."; 
     }
     this.pos[3][2] = "A";
     this.pos[5][2] = "D";
     this.pos[7][2] = "A";
     this.pos[9][2] = "B";
     
     this.pos[3][3] = "D";
     this.pos[5][3] = "C";
     this.pos[7][3] = "B";
     this.pos[9][3] = "A";
     
     this.pos[3][4] = "D";
     this.pos[5][4] = "B";
     this.pos[7][4] = "A";
     this.pos[9][4] = "C";
     
     this.pos[3][5] = "B";
     this.pos[5][5] = "C";
     this.pos[7][5] = "D";
     this.pos[9][5] = "C";
   }
   
   private boolean is_letter(String inp){
     return (inp == "A") || (inp == "B") || (inp == "C") || (inp == "D");
   }
   
   
   public void to_history(){
     int[] old_turns = new int[4];
     String[][] old_pos = new String[13][7];
     for (int i = 0; i < 4; i++){
       old_turns[i] = this.turns[i]; 
     }
     for (int i = 0; i < 13; i++){
       for (int j = 0; j < 7; j++){
         old_pos[i][j] = this.pos[i][j];
       }
     }
     this.history_pos.add(old_pos);
     this.history_turns.add(old_turns);
   }
   
   public void go_back_in_time(){
     if (!this.history_pos.isEmpty()){
       this.pos = this.history_pos.pollLast();
       this.turns = this.history_turns.pollLast();

     }
   }
   
   public void add_turns(int start_x, int start_y, int stop_x, int stop_y){
     String name =  this.pos[stop_x][stop_y];
     int index;
     if (name == "A"){
       index = 0; 
     } else if (name == "B"){
       index = 1; 
     } else if (name == "C"){
       index = 2; 
     } else if (name == "D"){
       index = 3; 
     } else {
       index = -100; 
     }
     int count = 0;
     if ((start_y != 1) && (stop_y != 1)) {
        count += start_y - 1;
        start_y = 1;
     }
     count += int(abs(start_x - stop_x));
     count += int(abs(start_y - stop_y));
     
     this.turns[index] += count;
   }
   
   public boolean move(int start_x, int start_y, int stop_x, int stop_y){
     if (!this.is_letter(this.pos[start_x][start_y])){
        return false;
     }
     if (this.pos[stop_x][stop_y] != "."){
        return false; 
     }
     this.to_history();
     this.pos[stop_x][stop_y] = this.pos[start_x][start_y];
     this.pos[start_x][start_y] = ".";
     this.add_turns(start_x, start_y, stop_x, stop_y);

     return true;
   }
   
   public int get_energy(){
      return turns[0] + turns[1] * 10 + turns[2] * 100 + turns[3] * 1000;
   }
}
