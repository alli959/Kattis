#include <iostream>
#include <vector>
#include <cmath>
#include <math.h>

using namespace std;

typedef long long ll;
typedef vector<int> vll;




int main(){
    int number;


    
    while(cin >> number){
        vll dividors; 

        for (int i=2; i<=sqrt(number); i++) { 
            if (number%i==0)  {
                //cout << "i" << endl << i << endl; 
            if (number/i == i) {  
                dividors.push_back(i);
            }
            else { 
                dividors.push_back(i);
                if(number/i != number){
                    //cout << "number/i" << endl << number/i << endl;
                    dividors.push_back(number/i); 
                }
            }
 
        } 
    } 
    
            
            
        

        int sum = 1;

        for(int i = 0; i<dividors.size(); i++){
            sum += dividors[i];
            
        }
                
        if(sum == number){
            cout << number;
            cout << " perfect" << endl;
        }
        else if((sum-2) <= number && number <= (sum+2)){
            cout << number;
            cout << " almost perfect" << endl;
        }

        else{
            cout << number;
            cout << " not perfect" << endl;
        }

    }
}