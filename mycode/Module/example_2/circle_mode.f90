module circle_mode
    real(kind=8), parameter :: pi = 3.141592653d0
    
contains
    
    real(kind=8) function area(r)
        real(kind=8), intent(in) :: r
        area = pi*r**2
     end function area
     
     real(kind=8) function circumference(r)
         real(kind=8), intent(in) :: r
         circumference = 2.d0*pi*r
     end function circumference
     
end module circle_mode
