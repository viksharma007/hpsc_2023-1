program mysqrt
	implicit none
	real (kind=8) :: root_val, a , sqrt_true , b , tol_r , s_init_r
	integer :: kmax_r
	print *,"Enter the value of number"
	read *,root_val,kmax_r,s_init_r,tol_r
	
	sqrt_true = sqrt(root_val)

	call sqrtNT(root_val , kmax_r, s_init_r, tol_r, a, b)
	
	print *,"sqrt_true = ",sqrt_true
	print *,"sqrtNT = ",a
	print *,"error = ",sqrt_true - a
	print *,"Number of iteration taken to converge = ",b

end program mysqrt

!Function called sqrtNT(x) retrun sqrt using Newton's Method

subroutine sqrtNT(x , kmax, s_init, tol, square, iter)
	implicit none
	
	!Function argument
	real (kind=8), intent(in) :: x, tol, s_init
	real (kind=8), intent(out) :: iter, square
	integer, intent(in) :: kmax
	
	! Local variable
	real (kind=8) :: delta_s,s_prev,s
	integer :: k
	s = s_init
	print *,"x = ",x
	do k=1,kmax
	    s_prev=s
	    s = 0.5*(s+x/s)
	    delta_s = abs(s - s_prev)
	    if ((delta_s/x)<tol) then
		exit
	    endif
	enddo
	
	print *, "iteration = ",k
	if (k>=kmax) then
	      print *, "Netwon method did not converge for kmax iterations;"
	endif
	iter = k
	square = s
end subroutine sqrtNT
