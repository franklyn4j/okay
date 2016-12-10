#ifndef heap_h
#define heap_h

#include <vector>

typedef std::vector<long> lilong;
class heap{

struct item{
	item(long,long);
	long data;
	long count;
	bool operator<(const item&)const;
};

	public:
		heap(long);
		heap(const lilong&);
		~heap();

	typedef std::vector<item> aritem;

	private:
		const long max_heap_size;
		aritem heap_data;

	private:
	    void max_heapify(long i);
	    inline long parent(long i){
			return i>>1;
		}
       
		inline long left(long i){
			return (i<<1);
		}

		inline long right(long i){
			return (i<<1)+1;
		}


};


#endif
