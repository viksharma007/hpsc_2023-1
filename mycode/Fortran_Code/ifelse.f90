!ifelse.f90
program ifelse
    implicit none
    real (kind = 8) :: x
    integer :: i
    i = 3
    
    if (i <= 2) then
    print *, "i is less than or equal to 2"
    
    else if (i .ne. 5) then
    print *, "i is greater than 2 and not equal to 5"
    
    else
    print *, "i is equal to 5"
    end if
end program ifelse
