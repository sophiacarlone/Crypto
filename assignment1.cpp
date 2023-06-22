//Sophia Carlone
//Crypto Assignment 1 -- assignment decrypter
//really simple encrypter and decrypter

#include<iostream>
#include<fstream> //Oh yeah, text files
using namespace std;

void Encrypt(string &message, const string &keyword); //Encrypting function declaration
void Decrypt(string &emessage, const string &keyword); //Decrypting function declaration

int main(){
  string filename; //text file name
  ifstream in; //file stream
  string message = ""; //message to be encrypted then decrypted
  string keyword = ""; //keyword encryption and decryption is based off of
  
  cout << "file name please!" << endl;
  cin >> filename;
  in.open(filename); //open file

  if(in.fail()) exit(0);
  in >> message; //assumes file is just one line with no enters or spaces, like the message for part 1
  in.close();

  cout << "Keyword please!" << endl;
  cin >> keyword;

  cout << "Original message: " << message << endl;
  Encrypt(message, keyword); //changing message to be encrypted
  cout << "Encrypted text: " << message << endl;
  Decrypt(message, keyword); //changing message to be decrypted
  cout << "Decrypted text: " << message << endl;

  return 0;
}

/*
Function to encrypt message based on choosen keyword
takes in string message and string keyword used to determine change
*/
void Encrypt(string &message, const string &keyword){
  int shift = 0; //monoalphebatic shift
  for(int i = 0; i < keyword.size(); i++){ //shifts multiple times
    shift = (int(keyword[i]) - int ('a')); //shifts based on currently letter of keyword
    for(int j = 0; j < message.size(); j++){
      message[j] = (char)((int(message[j]) + shift - 97)%26 + 97); //message character gets shifted using ascii
    }
  }
}

/*
Function to decrypte message based on choosen keyword
takes in string emessage that is encrypted and string keyword used in change
*/
void Decrypt(string &emessage, const string &keyword){
  int shift = 0; //monoalphebatic shift
  for(int i = 0; i < keyword.size(); i++){
    shift = 26 - (int(keyword[i]) - int('a')); //shift multiple times based on keyword to go back to original
    for(int j = 0; j < emessage.size(); j++){
      emessage[j] = (char)((int(emessage[j]) + shift - 97)%26 + 97); //emessage character gets shifted back using ascii
    }
  }
} 
