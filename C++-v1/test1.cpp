#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(){
  fstream fs;
  fs.open ("test.txt", fstream::in | fstream::out | std::fstream::app);

  fs << " more lorem ipsum";

  fs.close();

  return 0;
}