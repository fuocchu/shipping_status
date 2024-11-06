
USE ORDER_STATUS

CREATE TABLE ORDERS(
	ID NVARCHAR(20) PRIMARY KEY,
	ORDER_STATUS VARCHAR(20),
	LOC VARCHAR(100),
	TIME_est SMALLDATETIME

)

INSERT INTO ORDERS VALUES ('KA01','Shipped','BienHoa','2024-11-01'),
						 ('KA02','In Progress','TP.HCM','2024-11-20'),
						 ('KA05','Declined','WuHan','2024-10-30')