#include <map>
#include <unistd.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

struct item{
	item(long d,long c):data(d),count(c){}
	long data;
	long count;
	bool operator<(const item& r){
		return count < r.count; 
	}
};

using namespace std;
int main(int argc,char ** argv){

	map<long,long> data;
	long addr = 0;
	long count = 0;
	while(read(0,&addr,sizeof(addr)) == sizeof(addr)){
		++count;
		map<long,long>::iterator it = data.find(addr);
		if(it == data.end()){
			data.insert(make_pair(addr,0));
		}else{
			++it->second;
		}
	}

	perror("read end");

	printf("%ld data read\n",count);

	
	vector<item>  ar;
	for(map<long,long>::iterator it = data.begin();
			it != data.end(); ++it){
		ar.push_back(item(it->first,it->second));
	}

	make_heap(ar.begin(),ar.end());

	long len = count;
	if(argc == 2){
		len = atoi(argv[1]);
	}
	
	printf("len is %ld\n",len);

	for(int i = 0;i < len && ar.size() > 0; ++i){
		pop_heap(ar.begin(),ar.end());
		item largest = ar.back();
		ar.pop_back();
		printf("%ld : %ld\n",largest.data,largest.count);
	}
	
	return 0;

}
