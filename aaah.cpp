#include <iostream>
using namespace std;


string jmCapacity;
string docRequest;




int main(){
    cin>> jmCapacity >>docRequest;

    if (docRequest < jmCapacity){
        cout<<"no\n";
    }else{
        cout<< "go";
    }
}
