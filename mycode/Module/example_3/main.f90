program main
    
    use circle_mode, only: pi, area
    implicit none
    real(kind=8) :: a
    
    call initialize()  !sets pi
    
    print *, 'pi  = ',pi
    
    a = area(2.d0)
    print *,"area for the cicle of radius 2: ", a

end program main
