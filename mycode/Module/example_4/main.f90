program sub3
    use sub3module
    implicit none
    real(kind=8), dimension(3) :: y,z
    
    y = (/1.0,2.0,3.0/)
    call fsub(y,z)
    print *,"z = ", z
end program sub3
