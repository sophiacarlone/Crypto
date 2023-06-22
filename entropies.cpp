//Sophia Carlone
//Assignment 1 - entropie calculator

#include<iostream>
#include<fstream>
#include<cmath>
#include<map>
#include<cctype>
#include<iterator>
using namespace std;

void entropy(ifstream& in);

int main(){
  string filename;
  ifstream in;

  cout << "filename: " << endl;
  cin >> filename;

  in.open(filename);
  if(in.fail()) exit(0);
  
  entropy(in);
  
  in.close();

  return 0;
}

void entropy(ifstream& in){
    map<char, int> character_keeping;
    char current;
    double count = 0;
    double entropy = 0;

    while(in>>current){
	int ascii_num = int(current);
	if((ascii_num < 91 && ascii_num > 64) || (ascii_num < 123 && ascii_num > 96)){
		current = tolower(current);
		count++;
		auto itr = character_keeping.find(current);
		if(itr == character_keeping.end())
			character_keeping.insert(pair<char, int>(current, 1));
		else itr->second++;
	}
    }
    for(auto it = character_keeping.begin(); it != character_keeping.end(); it++){
	    //cout << it->first << endl;
	    double f0 = (it->second) / count;
	    double entropyC = f0 * log2(1/f0);
	    entropy += f0 * log2(1/f0); 
	    cout << it->first << " " << entropyC << endl;
    }
    cout << entropy << endl;
}	
