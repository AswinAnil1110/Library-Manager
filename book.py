import mysql.connector

class LibraryManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ASWIN@123",
            database="library_db"
        )
        print("Connection Successful")

    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from book where id=%s"
            value = (id,)
            self.cursor.execute(query,value)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """
                       insert into book (title,author,category,price,published_date)
                       values (%s, %s, %s, %s, %s)
                    """
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Book Added Successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("select * from book")
            record=self.cursor.fetchall()
            for data in record:
                print(data)

        except Exception as e:
            print(e)

    def retrive(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id =%s"
            value=(id,)
            self.cursor.execute(query,value)
            record = self.cursor.fetchone()
            if record==None:
                print("No Book Found...!")
            print(record)

        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query="select * from book where id =%s"
            value=(id,)
            self.cursor.execute(query,value)
            record = self.cursor.fetchone()
            if record != None:
                query = "delete from book where id =%s "
                self.cursor.execute(query,value)
                self.connection.commit()
                print("Book Deleted Successfully...!")
            else:
                print("No Book Found")

        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s ,"
                    placeholder = placeholder.rstrip(",")
                    query = f"update book set {placeholder} where id=%s "
                    value = [v for v in kwargs.values()]
                    value.append(id)
                    self.cursor.execute(query,value)
                    self.connection.commit()
                    print("Book Updated Successfully")
            else:
                print("No Book Found")
        except Exception as e:
            print(e)


books=LibraryManager()
# books.post(title="Baddie",author="Aljin",category="Flirting",price=5500,published_date="2024-02-28")
# books.get()
# books.retrive(id=5)
# books.delete(id=5)
# print("After Deleting a Book...")
# books.get()
books.put(id=1,author="Anus")