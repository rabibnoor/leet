class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int seenrow[9][10] = {0};
        int seencol[9][10] = {0};
        int seenbox[9][20] = {0};
        
        for (int i = 0; i< 9;  i ++){
            for (int j = 0; j< 9;  j ++){
                if (board[i][j] == '.') continue;
                
                int in3 = board[i][j] - '0';

                if (seenrow[i][in3] != 0) return 0; 
                if (seencol[j][in3] != 0) return 0;

                int box_index = (i / 3) * 3 + (j / 3);
                
                if (seenbox[box_index][in3] != 0) return 0;
                
                seenrow[i][in3] = 1; 
                seencol[j][in3] = 1; 
                seenbox[box_index][in3] = 1;
            }
        }
        return 1;
    }
};