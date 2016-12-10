#include <unistd.h>
#include <stdio.h>
#include <vector>

class Type{
	public:
		char a[3];
		void destroy(){
			delete this;
		}
};

using namespace std;
typedef vector<long> lilong;
int main(){

	const long long max = 10000000;
	lilong arr;
	long long pre = 0;
	long long i = 0;
	for(; i != max; ++i){
		Type *p = new Type;
		Type *pint = new Type;
		if(max % 400 == 0)
			usleep(1);

		pint->destroy();
		arr.push_back((long)p);
		if( i % 10000 == 0){
			for (;pre != i; ++pre){
				delete (Type*)arr[pre];
			}
		}
	}
	for (;pre != i; ++pre){
		delete (Type*)arr[pre];
	}

	char buf[20];
	for(lilong::iterator it = arr.begin(); it != arr.end(); ++it){
		if(write(1,&*it,sizeof(*it)) != sizeof(*it)){
			perror("write error");
		}
	   
	}

	return 0;
}

