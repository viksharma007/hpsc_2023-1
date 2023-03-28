program mysqrt
	implicit none
	real (kind=8) :: x,y,sqrt_true
	real (kind=8), external :: sqrtNT 
	x = 2.d0
	sqrt_true = sqrt(x)
	y = sqrtNT(x) !uses our sqrtNT fucntion
	!y = sqrt(x)
	print *,"x = ",x
	print *,"sqrt_true = ",sqrt_true
	print *,"sqrtNT = ",y
	print *,"error = ",sqrt_true - y

end program mysqrt

!Function called sqrtNT(x) retrun sqrt using Newton's Method

function sqrtNT(x)
	implicit none
	
	!Function argument
	real (kind=8), intent(in) :: x
	real (kind=8) :: sqrtNT
	
	! Local variable
	real (kind=8) :: s,tol,delta_s,s_prev
	integer :: k,kmax
	
	kmax = 100
	s = 1.d0
	tol = 1.d-14
	
	do k=1,kmax
	    s_prev=s
	    s = 0.5*(s+x/s)
	    delta_s = abs(s - s_prev)
	    if ((delta_s/x)<tol) then
		exit
	    endif
	enddo
	
	print *, "k = ",k
	if (k>=kmax) then
	      print *, "Netwon method did not converge for kmax iterations;"
	endif
	
	sqrtNT = s
	
end function sqrtNT
