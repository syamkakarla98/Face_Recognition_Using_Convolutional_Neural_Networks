
class_labels = {1:'164G1A0571', 2:'164G1A05B0', 4:'164G1A0584', 3:'164G1A0589'}
from datetime import datetime
import sqlite3

def check_attendance(connection, stid, time):
        global class_labels
        data_list = None
        cur = connection.cursor()
        if time>=int('0930') and time<=int('1020'):
            curs=cur.execute("SELECT P1 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        elif time>=int('1021') and time<=int('1110'):
            curs=cur.execute("SELECT P2 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        elif time>=int('1121') and time<=int('1210'):
            curs=cur.execute("SELECT P3 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            print('Checked')
        elif time>=int('1211') and time<=int('1300'):
            curs=cur.execute("SELECT P4 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        elif time>=int('1401') and time<=int('1450'):
            curs=cur.execute("SELECT P5 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        elif time>=int('1451') and time<=int('1540'):
            curs=cur.execute("SELECT P6 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        elif time>=int('1541') and time<=int('1630'):
            curs=cur.execute("SELECT P7 FROM Attendance WHERE RollNo=?", (class_labels[stid],))
            data_list = curs.fetchall()
            # print(data_list)
        return True if data_list == None or len(data_list)==0 or data_list[0][0] == None else False

def post_attendace(st_id):
        global class_labels
        conn = sqlite3.connect('Database.db')
        time = int(datetime.now().strftime('%H%M'))
        # if check_attendance(conn, st_id, time):
        if check_attendance(conn, st_id, time):
                cur = conn.cursor()
                if time>=int('0930') and time<=int('1020'):
                        cur.execute('''UPDATE Attendance SET p1 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1021') and time<=int('1110'):
                        cur.execute('''UPDATE Attendance SET p2 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1121') and time<=int('1210'):
                        cur.execute('''UPDATE Attendance SET p3 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1211') and time<=int('1300'):
                        cur.execute('''UPDATE Attendance SET p4 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1400') and time<=int('1450'):
                        cur.execute('''UPDATE Attendance SET p5 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1451') and time<=int('1540'):
                        cur.execute('''UPDATE Attendance SET p6 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
                if time>=int('1541') and time<=int('1630'):
                        cur.execute('''UPDATE Attendance SET p7 = ? WHERE RollNo = ?''', (datetime.now().strftime("%H:%M:%S"),class_labels[st_id]))
                        print('Attendance Posted')
        conn.commit()
        conn.close()




def get_details():
        global class_labels, PERIOD
        PERIOD = 'P3'
        conn = sqlite3.connect('Database.db')
        cur = conn.cursor()
        tim = cur.execute('SELECT '+ PERIOD +' FROM ATTENDANCE WHERE RollNo=?', (class_labels[2], ))
        tim = tim.fetchall()[0][0]
        conn.close()
get_details()


# conn = sqlite3.connect('Database.db')
# cur = conn.cursor()
# post_attendace(3)


# print(check_attendance(conn, 1, 1418))
# data = cur.execute('SELECT * FROM ATTENDANCE')
# for i in  data.fetchall():
#     print(i)
# conn.close()
# post_attendace(2)