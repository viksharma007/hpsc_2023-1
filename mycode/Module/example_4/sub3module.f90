module sub3module

contains

subroutine fsub(x,f)
    real(kind=8), dimension(:), intent(in) :: x
    real(kind=8), dimension(size(x)), intent(out) :: f
    f = x**2
end subroutine fsub

end module sub3module
