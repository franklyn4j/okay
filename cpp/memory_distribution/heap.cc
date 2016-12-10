#include <vector>

#include "heap.hh"

heap::item::item(long i):data(i),count(0){

}


heap::heap(const lilong& ar):max_heap_size(ar.size()){

	heap_data.reserve(max_heap_size*sizeof(item));

	for(lilong::iterator it = ar.begin();
			it != ar.end(); ++it){
		heap_data.push_back(item(*it));
	}
}

head::~heap(){

}

void max_heapify(long i){


}
