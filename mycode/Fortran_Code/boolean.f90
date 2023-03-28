!boolean.f90
program boolean
    implicit none
    integer :: i,k
    logical :: ever_zero
    
    ever_zero = .false.
    do i=1,10
    k = 3*i - 1
    ever_zero = (ever_zero .or. (k==0))
    enddo
    
    if (ever_zero) then
    print *, "3*i -1 takes the value of 0  for some i"
    else
    print *, "3*i -1 is not 0  for any i"
    end if
end program boolean
