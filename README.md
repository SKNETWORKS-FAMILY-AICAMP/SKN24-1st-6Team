# SKN24-1st-6Team
## 🚘 CARPORT (카포트)
*"자동차 구매 정보는 여기서: 현황·인기 차종·FAQ 통합 가이드"*

---
## 1. 👥 팀 소개
### ✨ 구갱 (Gu-Gang) ✨
- 90년대생 데이터로 이루어진 👉 Gang 😎🔥
> 💪😆 90’s + Gang = 구갱 ✨🔫

<br>

| **김유진** | **김정현** | **정재훈** | **권민제** | **박정은** |
|---|---|---|---|---|
|   🐣   |   🦊   |   🐯   |   🐼   |   🐱   |
| [@shortcut-2](https://github.com/shortcut-2) | [@Jeich-16](https://github.com/Jeich-16) | [@JeaHoon-J](https://github.com/JeaHoon-J) | [@min3802](https://github.com/min3802) | [@brainkat](https://github.com/brainkat) |

---

## 2. 📋 프로젝트 개요

> *자동차 등록 현황이 궁금한데, 한번에 볼 수 있는 곳 없을까?*

<br>

> *작년에 제일 많이 팔린 차는 뭘까?*

- 통계 페이지를 검색해서 들어가야 하는 불편함, 분산된 자동차 정보를 한번에 확인하기 위해 이곳저곳 찾아다닐 필요 없이, **여러 사이트의 핵심 정보를 한 페이지에서** 바로 확인할 수 있도록 제작. 
---
### 2-1. 🔍 배경

**<전체 등록 및 신규 등록 차량 정의>**
1) 전체 등록 정의: 해당 시점에 자동차 등록 원부에 등록되어 있는 **자동차의 총 수**
- 누적되는 데이터이므로 차량 보유규모, 지역별 자동차 보급 수준, 장기적인 증가나 감소의 추세를 보는데 용이함
- 시･도별로 등록된 자동차의 제반사항을 파악하여 교통행정의 기초 자료로 활용하기 위함
###### (참조 1. 국토교통부,자동차등록현황보고』통계정보보고서, [https://www.kostat.go.kr/board.es?mid=a10409070000&bid=12030&tag=&act=view&list_no=442885&ref_bid=])

<br>

2) 신규 등록 정의 : **새로 자동차를 구매**하여 자동차 등록 원부에 등록한 건 수
- Business Research Insights(2023)에서는 분석 범위를 차량데이터 전체가 아닌 자동차 데이터 분석에 초점을 맞추어 시장의 규모를 측정(소비 심리나 경기 상황 반영)하고 향후 전망을 제시함 
###### (참조 2. 보험연구원,「차량데이터 이용 현황 및 보험회사 시사점」, 보험연구원 홈페이지, [https://www.kiri.or.kr/report/reportList.do?docId=580489&catId=4])
---
### 2-2. ✔️ 한계점

1) 전국 자동차 등록대수는 전반적인 자동차를 구매하는 동향을 볼 수 있지만, 그중 **어떤 차가 인기가 있는지 확인할 수 없음** 
	→ 판매량을 통해 자동차 구매 예정 고객은 가장 인기가 많은 차종에 대한 정보를 확인할 수 있음

<br>

2) 예비 구매자들은 현재 인기 있는 모델을 확인하거나, 구매 전 FAQ를 확인하기 위해 제조사별 페이지를 **일일이 찾아서 비교**해야 하므로 편의성이 떨어짐
	→ 해당 정보를 한 페이지에서 확인하는 편리성을 제공
---
### 2-3. 🚘 프로젝트 소개

**CARPORT**는 2025년 최신 데이터를 바탕으로, 자동차 구매를 고민하거나 시장 동향이 궁금한 분들을 위해 **전국 자동차 등록 현황**과 **인기 모델 정보, FAQ**를 한눈에 보여주는 플랫폼입니다. 

---
### 2-4. 🎯 목표

1. **2025 전국 자동차 등록 현황**
	- 시/도/구별, 차종별로 국내에 자동차가 몇 대 등록되어 있는지 확인

2. **2025 자동차 신규 등록 현황/판매량 조회**
	- 신규 등록자들의 연령대/성별/사용연료 현황을 확인    → 제조사별 2025년 판매량 확인을 통해 최신 트렌드를 파악하여 예비 구매자에게 정보 제공

3. **국내 상위 제조사의 FAQ 통합 정보 제공**
	- 판매량이 높은 대표적인 브랜드(현대, 기아)의 FAQ를 한번에 확인할 수 있도록 함

---

## 3. 🛠️ 기술 스택

|   영역   |   기술   |
| ---------------------- | ---------- |
| FRONTEND | <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=python&logoColor=white"> |
| BACKEND | <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> |
| DATABASE | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> |
| DATA PROCESSING | <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=mysql&logoColor=white"> |
| DATA VISUALIZATION | <img src="https://img.shields.io/badge/plotly-7A76FF?style=for-the-badge&logo=mysql&logoColor=white"> ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) |
| WEB SCRAPING | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-61DAFB?style=for-the-badge&logo=python&logoColor=white) <img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=mysql&logoColor=white"> |

---
## 4. WBS
<img width="915" height="667" alt="WBS" src="https://github.com/user-attachments/assets/9bb0a82a-54f0-4bd6-a0db-dafce8c4d908" />

---
## 5. 요구사항 명세서
<img width="1054" height="436" alt="요구사항명세서" src="https://github.com/user-attachments/assets/bb193860-b2db-4c68-8ab2-324d3a637b9a" />

---
## 6. ERD

<img width="1820" height="772" alt="ERD" src="https://github.com/user-attachments/assets/11dcc2c9-c864-44b8-9e20-01fb0507dc92" />

---
## 7. 수행 결과
### 의존 패키지 설치

```python
pip install -r requirements.txt
```

### 🔢 SQL Database Script

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

#### 테이블 삭제

```sql
DROP TABLE IF EXISTS total_registered_vehicle CASCADE;
DROP TABLE IF EXISTS faq CASCADE;
DROP TABLE IF EXISTS faq_category CASCADE;
DROP TABLE IF EXISTS vehicle_sales CASCADE;
DROP TABLE IF EXISTS new_registered_vehicle CASCADE;
DROP TABLE IF EXISTS vehicle_company CASCADE;
```

### 메인
---

### 자동차 등록 현황
---
<img width="925" height="822" alt="total_reg_page_1" src="https://github.com/user-attachments/assets/01de72b7-5987-4470-b05b-3849052afa96" />

![total_reg_page](https://github.com/user-attachments/assets/dcdc5ab8-1400-4892-8846-106335561081)

### 자동차 신규 등록 현황
---
<img width="60%" height="60%" alt="new_register_page__1" src="https://github.com/user-attachments/assets/f725e647-2c04-40e6-b595-3ba77c9940ad" />
<img width="60%" height="60%" alt="new_register_page__2" src="https://github.com/user-attachments/assets/153255be-33f7-4dd3-8ec9-730fef8ac561" />
<img width="60%" height="60%" alt="new_register_page__3" src="https://github.com/user-attachments/assets/d52ab7c5-c85c-429d-947b-23a195dee92d" />


### 자동차 판매량 조회
---
<img width="50%" height="50%" alt="vehicle_sales_page__1" src="https://github.com/user-attachments/assets/5a2fcd5f-7855-445c-9850-927d0996ef5e" />
<img width="50%" height="50%" alt="vehicle_sales_page__2" src="https://github.com/user-attachments/assets/0e8b430f-7bf3-4c51-b795-75d5beab7bf5" />

### FAQ
---
https://github.com/user-attachments/assets/130e2634-0fe8-4be8-8259-fac140a7acc9



---

<br>

## 📓한줄 회고 
**김유진**
> 금번 프로젝트를 통해 팀원들의 도움 덕분에 짧은 기간이지만 구현에 성공할 수 있었습니다. 
> 자동차 등록 현황 데이터 수집을 위해 BeautifulSoup과 Selenium으로 웹 크롤링을 직접 시도하며, python 코드를 더 이해하는 시간이 되었습니다. 기획부터 산출까지 짧은 기간 안에 구성할 수 있었던 경험을 통해 이후 프로젝트에서도 어떻게 세팅 하고 시작해야 할지 체득할 수 있는 계기였습니다.
> MySQL의 DB를 가져와 Streamlit에 구현하는 것과 데이터를 어떻게 효과적으로 보여줄 것인가에 대한 고민이 부족했던 것 같습니다. 이후에는 실제 개발 단계 이전부터 기획과 모의 구현에 충실하게 임하여 데이터 표현에도 조금 더 신경 쓰고 싶습니다.

**김정현**
>

**정재훈**
>

**권민제**
>웹 크롤링 능력은 확실히 향상되었지만, Streamlit과 GitHub 사용에는 여전히 미숙함을 느꼈고 팀 프로젝트에서 의사소통 면에서도 소극적인 태도를 완전히 극복하지 못한 점이 아쉬웠다. 앞으로는 GitHub 사용법을 정리해 개인 레포지토리를 만들어 직접 실습해보고, 팀 활동에서는 작은 의견이라도 먼저 제시하며 보다 적극적으로 참여해보고자 한다.

**박정은**
>

