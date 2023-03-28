program matrix1
    implicit none
    real (kind = 8) ,dimension(3,2) :: a
    real (kind = 8) ,dimension(2,3) :: b
    real (kind = 8) ,dimension(3,3) :: c
    integer :: i
    
    a = reshape((/1,2,3,4,5,6/), (/3,2/))
    print *, "a = ",a
    
    do i = 1,3
    print *,a(i,:)
    enddo
    
    b = transpose(a)
    
    c = matmul(a,b)
    print *, "c = ",c
end program matrix1
