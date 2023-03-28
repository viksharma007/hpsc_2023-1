OBJECTS = sub3module.o \
	  main.o
          
MODULES = sub3module.mod

.PHONY: clean

output.txt: main.exe
	./main.exe > output.txt
	
main.exe: $(MODULES) $(OBJECTS)
	gfortran $(OBJECTS) -o main.exe
	
%.o: %.f90
	gfortran -c $<
	
%.mod: %.f90
	gfortran -c $<	
clean:
	rm -f $(OBJECTS) $(MODULES) main.exe
