#include <unistd.h>
#include <stdio.h>

int main(){

	int size = 0;
	int n = read(0,&size,sizeof(size));
	if(n != sizeof(size))
	{
		perror("read error");
	}else
	{
		perror("read ok");
	}
	if(size == 8){
		printf("ok");
	}else{
		printf("not ok");
	}
	printf("%d\n",size);
	return 0;
}
