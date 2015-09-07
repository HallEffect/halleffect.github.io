Title: Преобразование std::vector в list и наоборот c использованием Boost.Python
Date: 2015-05-13
Tags: Python, Boost
Category: Блог
Author: Alexander Teleshov

Конвертер для преобразования из std::vector в list
```cpp
template<typename T>
struct cppvector_to_list
{
    static PyObject *convert( T const &v )
    {
        boost::python::list list;

        for ( auto const &it : v )
        {
            list.append( *it );
        }

        return incref( list.ptr() );
    }
};
```

Конвертер для преобразования из list в std::vector
```cpp
template< typename T >
struct list_to_cppvector
{
    list_to_cppvector()
    {
        converter::registry::push_back( convertible, construct, type_id< std::vector<T> >() );
    }

    static void *convertible( PyObject * ); // метод проверки на конвертируемость
    static void construct( PyObject *, converter::rvalue_from_python_stage1_data * ); // Конструктор объекта
};


template<typename T> void *list_to_cppvector<T>::convertible( PyObject *obj )
{
    return PyList_Check( obj ) ? obj : 0;
}


template<typename T> void list_to_cppvector<T>::construct( PyObject *obj, converter::rvalue_from_python_stage1_data *data )
{
    void *storage = reinterpret_cast< converter::rvalue_from_python_storage< std::vector<T> >* >( data )->storage.bytes;

    // Создаем boost.python.list. Заполняем его элементами питоновского списка
    list l( handle<>( borrowed( obj ) ) );

    // Используя размещающий new, размещаем объекты из временного вектора, по адресу <storage>
    std::vector<T> &v = *( new ( storage ) std::vector<T> () );

    // Заполняем вектор значениями из питоновского листа
    v.resize( len( l ) );

    for ( int i = 0; i != len( l ); ++i )
    {
        v.at( i ) = extract<T>( l[i] );
    }

    data->convertible = storage;
}
```

Региструрем конвертеры для нужных типов:
```
to_python_converter< std::vector<unsigned short> , 
                     cppvector_to_list<std::vector<unsigned short> > >();

to_python_converter< std::vector<double> , 
                     cppvector_to_list<std::vector<double> > >();

list_to_cppvector< unsigned short >();
list_to_cppvector< double >();    
```