from formation import AppBuilder

app = AppBuilder(path="d:/GDisk/GeekBraims/Python/PythonSeminars/Seminar7/PhoneBook/formation-studio/phone.xml")

app.connect_callbacks(globals())

app.mainloop()