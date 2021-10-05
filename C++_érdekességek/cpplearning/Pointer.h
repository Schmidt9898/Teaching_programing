#pragma once
#include <iostream>
#include <string>
//I used delete in this text but delete operator does not get rid of the data only free it, so the data will be in the memory until on other program overrides it.

std::string array_ToString(size_t size, int* arr);


void goodPointers()
{
    //here is a variable with a value of 5
    int int_var = 5;
    std::cout << "Int_var value is = " << int_var << "\n";
    //This variable has a place and an addres in the memory
    int* int_var_pointer = &int_var;
    std::cout << "Int_var_pointer value is = " << int_var_pointer << "\n";
    //This int_var_pointer is still a variable but the value is the addres of int_var
    //changing this value will not change the int_var but will point to a different point in  the memory.
    //you can change the value of int_var with int_var_pointer if you dereferenc the object.
    *int_var_pointer += 1; //++ is not working if it is postfix.
    std::cout << "Int_var value is changed = " << int_var << "\n";

    //Pointer used to allocate dinamic memory like arrays and objects

    int* array;//this has no memory behind it
    array = new int(10);
    std::cout << "array points to an integer addres  with value of " << *array << "\n";
    delete array; //this will deallocate the memory
    //please if you allocate memory always delete it. you only can delete it by the addres, if you overwrite it or forget it you can no longer delete it.
    //dont worry, if you close the program the memory will be deleted.
    //array stil point to the memory that the int was located but now that memory is not ours so reaching for it will cause a segmentation fault
    //*array = 1;//if you try to run this may or may not will be an error

    //lets allocate more memory
    array = new int[int_var];//this line allocate 6 * 4 byte of memory and the start byte addres will be the array value
    std::cout << array_ToString(int_var, array) << "\n";//this probably print ugly numbers because its memory not cleared, this is called memory junk
    delete[] array;// delete will deallocate the memory, witout [] it will only deallocate the first element

    //you can zero out an array with {}
    array = new int[int_var] {};
    std::cout << array_ToString(int_var, array) << "\n";//0,0,0,0,0,0
    delete[] array;

    //or you can add a array to it
    array = new int[int_var] {1, 2, 3, 4, 5, 6};
    std::cout << array_ToString(int_var, array) << "\n";//1,2,3,4,5,6
    std::cout << array << " array is still a pointer to an int\n";
    std::cout << *array << " *array is still an int value. the first element\n";
    std::cout << *(array + 1) << " get the secound element\n";//you can get the other elements by changing the array value
    //but you may use [] operator.
    std::cout << array[2] << " get the third element\n";//This example shows why we index from 0
    //please notice that an int is 4 byte and we only add 1 to the addres
    //the compiler know that this is an int pointer so it will calculate the correct size and increment by it.
    std::cout << 3[array] << " get the fourth element\n"; // yeah, in c++ beacause it is only an addition to the start addres you can just swap the operands

    delete[] array;


    //because it is just pointer and bytes you can freely cast any type
    //it not always will be good or readable, but you do know what you are doing, i hope
    char* char_array = new char[8]{ 'c','h' ,'a' ,'r' ,'i' ,'n' ,'t' ,'\0' };//this is basicly a string "charint" last one is the end of string byte
    std::cout << char_array << "\n";
    //lets convert it to a int array
    array = (int*)char_array;// 8 byte is 2 int

    std::cout << array_ToString(2, array) << "\n";//lets se those bytes as int. Not so beautiful, but thats it.
    delete[] array;//you can delete an array by this but only delete once, dont delete the char_array because these 2 point to the same addres

}

void badPointers()
{
    //I don't have to tell you that anything in this function is bad practice and you should 
    //never do this.
    //If you can accept it, here is how you do it.
    struct Obj
    {
        // I don't want you to change the following values.
    private:
        int one = 1;
        int two = 2;
    public:
        std::string Print() { return std::to_string(one) + "," + std::to_string(two); };
    };


    Obj obj;
    std::cout << obj.Print() << "\n";

    //Next row wont compile because one is private
    //std::cout<<obj.one<<"\n";
    
    //a struct puts the variables as an array with elemsize of the largest element
    //(sometimes can be efficient with the small variables)
    //so if you want to reach the one variable, you have to index the obj
    int* obj_p = (int*)&obj;
    obj_p[0] = 10;
    obj_p[1] = 20;
    std::cout<<obj.Print()<<"\n";


    //but again you should never do this.




}




















std::string array_ToString(size_t size, int* arr)
{
    std::string str = "";
    for (size_t i = 0; i < size; i++)
    {
        str = str + std::to_string(arr[i]) + ",";
    }
    str.pop_back();
    return str;
}