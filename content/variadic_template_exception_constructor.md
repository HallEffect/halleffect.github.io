Title: Шаблонный конструктор пользовательского класса исключения с переменным числом аргументов
Date: 2015-05-13
Category: Блог
Tags: Python, Boost

Author: Alexander Teleshov

```cpp
#ifndef MYEXCEPTION_H_
#define MYEXCEPTION_H_

#include <exception>
#include <string>
#include <sstream>
#include <tuple>

class MyException : public std::exception
{

public:
    MyException(): m_msg("Ошибка")
    {

    }

    template <typename ...Args> MyException(Args... message) : m_msg("")
    {
        auto tp = std::make_tuple(message...);
        std::stringstream ss;
        ss << tp;
        m_msg = ss.str();
    }

    ~MyException() throw() {}

    const char *what() const throw();

private:
    std::string m_msg;

}; // end of class MyException : public std::exception


// Вспомогательная ф-ция: выводит элементы начиная с индекса IDX, из кортежа
// содержащего MAX элементов.
template <int IDX, int MAX, typename... Args>
struct PRINT_TUPLE
{
    static void print (std::stringstream &strm, const std::tuple<Args...> &t)
    {
        strm << std::get<IDX>(t);
        PRINT_TUPLE < IDX + 1, MAX, Args... >::print(strm, t);
    }
};


// Частичная специализация для завершения рекурсии
template <int MAX, typename... Args>
struct PRINT_TUPLE<MAX, MAX, Args...>
{
    static void print (std::stringstream &strm, const std::tuple<Args...> &t)
    {

    }
};


// Оператор вывода для кортежей
template <typename... Args>
std::stringstream &operator << (std::stringstream &strm, const std::tuple<Args...> &t)
{
    PRINT_TUPLE<0, sizeof...(Args), Args...>::print(strm, t);
    return strm;
}

#endif /* end of include guard: MYEXCEPTION_H_ */
```