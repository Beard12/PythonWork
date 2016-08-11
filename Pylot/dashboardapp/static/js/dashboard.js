function confirmation(){
	
	bool= confirm("Are you sure you would like to delete this user?")
	if(bool){
		$(this).submit()
	}
	else{
		$(this).submit(
			return false)
	}

}