#include<bits/stdc++.h>
using namespace std;

int max(int a, int b) {
    if(a > b) return a;
    else return b;
};

int longestCommonSubstring(string a, string b){
    int solutionTable[a.length() + 1][b.length() + 1];

    for(int i = 0; i <= a.length(); i++){
        for(int j = 0; j <= b.length(); j++){
            if(i == 0 || j == 0) solutionTable[i][j] = 0; 
            else if(a.at(i-1) == b.at(j-1)) solutionTable[i][j] = solutionTable[i-1][j-1] + 1;
            else solutionTable[i][j] = max(solutionTable[i-1][j], solutionTable[i][j-1]);
        }
    }
    
    return solutionTable[a.length()][b.length()];
}

int main(){
    string a, b;
    cin>>a;
    cin>>b;
    cout<<longestCommonSubstring(a,b)<<endl;
    return 0;
}