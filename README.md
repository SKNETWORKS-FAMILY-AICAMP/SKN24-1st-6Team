🚘 CARPORT (카포트)


한번에 요즘 자동차 등록, 판매 수를 볼수있는 플랫폼





<br>
👥 팀 소개


팀명: 구갱 


팀원들이 90년대생인 데이터로 90년도생인 gang 


김유진 @shortcut-2


김정현 @Jeich-16


정재훈 @JeaHoon-J


권민제 @min3802


박정은 @brainkat





<br>
📋 프로젝트 개요


CARPORT는 2025년 최신 데이터를 바탕으로, 자동차 구매를 고민하거나 시장 동향이 궁금한 분들을 위해 전국 자동차 등록 현황과 인기 모델 정보를 한눈에 보여주는 플랫폼입니다.



프로젝트 소개: 자동차 정보를 얻기 위해 이곳저곳 찾아다닐 필요 없이, 여러 사이트의 핵심 정보를 한 페이지에서 바로 확인할 수 있도록 제작했습니다. 



기획 배경: "자동차에 대해 궁금한 건 많은데, 매번 여러 사이트를 뒤져보기 귀찮지 않을까?"라는 고민에서 시작했습니다. 여러 사이트 봐야하는 과정을 단축해서 한사이트에서 여러사이트 정보를 볼수있는 사이트를 기획하게 되었습니다.






<br>
🎯 주요 목표 및 필요성


프로젝트 목표: 사용자 입장에서 더 빠르고 편한 정보찾기 





<br>
🛠️ 기술 스택


FRONTEND: Streamlit


BACKEND: Python 3.12


DATABASE: MySQL


DATA PROCESSING: Pandas, NumPy


DATA VISUALIZATION: Plotly, Matplotlib


WEB SCRAPING: BeautifulSoup, Selenium





<br>
🏁 실행하기 


의존 페키지 설치


```python
pip install -r requirements.txt
```




<br>
🔢  ERD & DB


<img width="1820" height="772" alt="ERD" src="https://github.com/user-attachments/assets/11dcc2c9-c864-44b8-9e20-01fb0507dc92" />



SQL Database Script


```sql

create database vehicledb;

grant all privileges on vehicledb.* to ohgiraffers@'%';

use vehicledb;

CREATE TABLE `vehicle_company` (
	`company_id`	INT	AUTO_INCREMENT COMMENT '회사  코드',
	`company_name`	VARCHAR(20)	NULL	COMMENT '회사 이름',
	PRIMARY KEY (`company_id`)
) ENGINE=INNODB COMMENT '자동차 회사';

CREATE TABLE `faq_category` (
    `faq_cat_id`   INT AUTO_INCREMENT COMMENT '카테고리 코드',
    `faq_cat_name` VARCHAR(50) NOT NULL COMMENT '카테고리 이름',
    `company_id`   INT NOT NULL COMMENT '회사 외래키',
    PRIMARY KEY (`faq_cat_id`),
    CONSTRAINT fk_faq_company FOREIGN KEY (`company_id`) REFERENCES `vehicle_company` (`company_id`)
) ENGINE=INNODB COMMENT '자주하는 질문 카테고리';

CREATE TABLE `faq` (
    `faq_id`     INT AUTO_INCREMENT COMMENT 'FAQ PK',
    `faq_cat_id` INT NOT NULL COMMENT '카테고리 FK',
    `question`   TEXT NOT NULL COMMENT '질문',
    `answer`     TEXT NOT NULL COMMENT '답장',
    PRIMARY KEY (`faq_id`),
    CONSTRAINT fk_faq_category FOREIGN KEY (`faq_cat_id`) REFERENCES `faq_category` (`faq_cat_id`)
) ENGINE=INNODB COMMENT '자주하는 질문';

CREATE TABLE `vehicle_sales` (
	`sales_id`	INT	AUTO_INCREMENT NOT NULL	COMMENT '판매 코드',
	`sales_date`	DATE	NOT NULL	COMMENT '등록 날짜',
	`company_id`	INT 	NOT NULL,
	`sales_count`	INT	NOT NULL	COMMENT '판매 수',
	`sales_model`	VARCHAR(100)	NOT NULL COMMENT '자동차 모델',
	 PRIMARY KEY (`sales_id`),
   CONSTRAINT fk_company_id FOREIGN KEY (`company_id`) REFERENCES `vehicle_company` (`company_id`)
)ENGINE=INNODB COMMENT '자동차 판매';

CREATE TABLE `total_registered_vehicle` (
	`reg_id`	INT AUTO_INCREMENT	COMMENT '등록 코드',
	`city`	VARCHAR(50)	NOT NULL COMMENT '시도명',
	`district`	VARCHAR(50)	NOT NULL	COMMENT '시군구',
	`reg_type`	VARCHAR(30)	NOT NULL	COMMENT '가입 구분',
	`vehicle_type`	VARCHAR(30)	NOT NULL	COMMENT '자동차 분류',
	`reg_count`	INT	NOT NULL	COMMENT '등록 수',
	`reg_date`	DATE	NOT NULL,
	PRIMARY KEY (`reg_id`)
)ENGINE=INNODB COMMENT '자동차등록현황';

CREATE TABLE `new_registered_vehicle` (
	`new_reg_id`	INT AUTO_INCREMENT	NOT NULL COMMENT '신규 등록 코드',
	`new_reg_date`	DATE	NOT NULL	COMMENT '등록 날짜',
	`age_range`	INT	NOT NULL	COMMENT '연령대',
	`gender`	CHAR(1)	NOT NULL	COMMENT '성별 F:여자 M:남자',
	`fuel_type`	VARCHAR(20)	NOT NULL	COMMENT '사용연료',
	`new_reg_count`	INT	NOT NULL	COMMENT '신규등록 수',
	PRIMARY KEY (`new_reg_id`)
)ENGINE=INNODB COMMENT '신규등록';
```



테이블 삭제
```sql
DROP TABLE IF EXISTS total_registered_vehicle CASCADE;
DROP TABLE IF EXISTS faq CASCADE;
DROP TABLE IF EXISTS faq_category CASCADE;
DROP TABLE IF EXISTS vehicle_sales CASCADE;
DROP TABLE IF EXISTS new_registered_vehicle CASCADE;
DROP TABLE IF EXISTS vehicle_company CASCADE;
```





<br>
📊 수행결과
FAQ 페이지 
<img width="1512" height="908" alt="faq3" src="https://github.com/user-attachments/assets/f18cb326-9759-42b6-947c-71787e230cdc" />
<img width="1509" height="903" alt="faq2" src="https://github.com/user-attachments/assets/b5dc994b-5b8d-45ed-b728-092070900460" />
<img width="1511" height="908" alt="faq1" src="https://github.com/user-attachments/assets/4c04e594-b283-4d18-912a-cdcd6de7f2bd" />





<br>
📓한 줄 회고 


다음 계선: vehicle_company 데이터 입력 자동화기, 더 다양한 FAQ 데이터 포함학기
