
subroutine add_one(matrix, nrows, ncols)
    integer, intent(in) :: nrows, ncols
    double precision, intent(inout) :: matrix(nrows, ncols)
            
    integer :: ii, jj
    
    print *, nrows, ncols
    
    do ii = 1, size(matrix, 1)
        do jj = 1, size(matrix, 2)
            matrix(ii, jj) = matrix(ii, jj) + 1
        end do
    end do
end subroutine add_one
