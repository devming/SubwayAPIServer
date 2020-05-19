# 지하철 역사 내 방위 제시 시스템 연구

## 프로젝트 명: 가온길로(모바일)

### 1. 사용 기술
- __Backend Framework / Language__: Django 2.05 / Python 3.4
- __Frontend__: HTML, CSS, Bootstrap
- __Mobile__: iOS [[Link](https://github.com/devming/SubwayiOSApplication)]
- __Open API__: Seoul OpenAPI [지하철 최단 경로 API](https://data.seoul.go.kr/dataList/datasetView.do?infId=OA-12762&srvType=A&serviceKind=1&currentPageNo=1)
- __Server__: AWS ubuntu free tier
- __Database__: SQLite3

### 2. Rest API 


#### GET /qr/`:stationAdminId`/`:landmarkIndex`/`:destinationStationName`


1. __Description__ 
   
   현재 날짜 기준 최신 주보의 버전을 가져온다. 앱에 저장되어 있는 버전이 응답받은 서버의 버전과 다르면 데이터 새로고침을 위한 API를 호출하고, 같다면 API호출 없이 내부적으로 저장된 데이터를 사용한다.
   
   > ##### Request Parameters
   
   - `station_admin_id `: QR코드를 찍으면 나오는 해당 역의 관리자 id
   - `landmark_index `: Landmark Point의 고유번호
   - `destination_station_name`: 사용자의 목적지 지하철 역 이름
   
2. __Headers__
   
   Content-Type: application/json

3. __Body__
   
   null


4. __Response__

	- Response Code
	
    Status Code       | Response         
    ------------|---------- 
    200 | Operation succeeded.
    400 | Unknown error. 
    500 | Internal server error

    - Response Data
    
   ```json 
	{
		"stationName": "지하철 역 이름",
		"direction": "사용자가 가야할 방향"
	}
   ```
   
   - Response Description
	
	
	> _stationName_: 현재 역에 대한 정보를 받아온다.
	
	> _direction_: 사용자가 가야할 방향을 제시한다. 
	  	    현재는 LEFT(왼쪽), RIGHT(오른쪽), NONE(잘못된 값) 기준으로만 잡혀있다.
   

