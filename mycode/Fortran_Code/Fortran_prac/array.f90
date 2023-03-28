program array
    implicit none
    real(kind=8), dimension(3,2) :: A
    real(kind=8), dimension(2,3) :: b
    real(kind=8), dimension(3,3) :: c
    integer :: i
    
    A = reshape((/1,2,3,4,5,6/), (/3,2/))
    print *, A
    
    do i=1,3
        print *, a(i,:)
        enddo
        
    b = transpose(a)
    print *, b
    
    c = matmul(a,b)
    print *, c
    
    
end program array
