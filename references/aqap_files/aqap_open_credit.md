# 开证记录表-aqap_open_credit

## 开证记录表-主表 t_aqap_open_credit

- **表名称：** 开证记录表-主表
- **表名：** t_aqap_open_credit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | favwtbankbic | avwtbankbic | varchar | 20 |  |  | '' | avwtbankbic |
| 3 | fcreditno | creditno | varchar | 32 |  |  | '' | creditno |
| 4 | fdraweeaddress | draweeaddress | varchar | 200 |  |  | '' | draweeaddress |
| 5 | faddclause_tag | addclause_详情 | text | 0 |  |  | null | addclause_详情 |
| 6 | fforwardcnapscode | forwardcnapscode | varchar | 15 |  |  | '' | forwardcnapscode |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftermini | termini | varchar | 250 |  |  | '' | termini |
| 9 | fcredittype | credittype1 | varchar | 2 |  |  | '' | credittype1 |
| 10 | facceptorcnapscode | acceptorcnapscode | varchar | 15 |  |  | '' | acceptorcnapscode |
| 11 | ffilename | filename | varchar | 50 |  |  | '' | filename |
| 12 | fpaydays | paydays | varchar | 8 |  |  | '' | paydays |
| 13 | fmrgnaccno | mrgnaccno | varchar | 50 |  |  | '' | mrgnaccno |
| 14 | fdraftcustflg | draftcustflg | varchar | 6 |  |  | '' | draftcustflg |
| 15 | fmixtenordays | mixtenordays | varchar | 8 |  |  | '' | mixtenordays |
| 16 | fmrgnproportion | mrgnproportion | varchar | 8 |  |  | '' | mrgnproportion |
| 17 | fversion | version | int8 | 64 |  |  | null | version |
| 18 | fbankbatchseqid | bankbatchseqid | varchar | 30 |  | √ | '' | bankbatchseqid |
| 19 | fname | 名称 | varchar | 50 |  |  | '' | 名称 |
| 20 | favwtbank | avwtbank | varchar | 1 |  |  | '' | avwtbank |
| 21 | facceptoraddress | acceptoraddress | varchar | 200 |  |  | '' | acceptoraddress |
| 22 | fterminiair | terminiair | varchar | 250 |  |  | '' | terminiair |
| 23 | finserttime | inserttime | timestamp | 0 |  |  | null | inserttime |
| 24 | fpayfinishtime | payfinishtime | timestamp | 0 |  |  | null | payfinishtime |
| 25 | fshipdate | shipdate | varchar | 10 |  |  | '' | shipdate |
| 26 | fmrgncurrency | mrgncurrency | varchar | 5 |  |  | '' | mrgncurrency |
| 27 | foprtel | oprtel | varchar | 20 |  |  | '' | oprtel |
| 28 | fenable | 使用状态 | varchar | 50 |  |  | '' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fgasdescription | gasdescription | varchar | 250 |  |  | '' | gasdescription |
| 30 | fnumber | 编码 | varchar | 30 |  |  | '' | 编码 |
| 31 | fmixtenortype | mixtenortype | varchar | 1 |  |  | '' | mixtenortype |
| 32 | fdeliveryport | deliveryport | varchar | 250 |  |  | '' | deliveryport |
| 33 | fbankmsg | bankmsg | varchar | 200 |  |  | '' | bankmsg |
| 34 | fadvicnapscode | advicnapscode | varchar | 15 |  |  | '' | advicnapscode |
| 35 | frqstserialno | rqstserialno | varchar | 30 |  |  | '' | rqstserialno |
| 36 | fdetailseqid | detailseqid | varchar | 32 |  |  | '' | detailseqid |
| 37 | fmoreproportion | moreproportion | varchar | 10 |  |  | '' | moreproportion |
| 38 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 39 | favwtbanknmadd | avwtbanknmadd | varchar | 200 |  |  | '' | avwtbanknmadd |
| 40 | fstatus | 数据状态 | varchar | 50 |  |  | '' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 41 | fdraftproportion | draftproportion | varchar | 4 |  |  | '' | draftproportion |
| 42 | fbiztype | biztype | varchar | 20 |  | √ | '' | biztype |
| 43 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 44 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 45 | fsynccount | synccount | int8 | 64 |  |  | null | synccount |
| 46 | fremark | remark | varchar | 250 |  |  | '' | remark |
| 47 | fbankrefkey | bankrefkey | varchar | 100 |  |  | '' | bankrefkey |
| 48 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 49 | fcreditstatus | creditstatus | varchar | 20 |  |  | '' | creditstatus |
| 50 | fispartship | ispartship | varchar | 3 |  |  | '' | ispartship |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fadviaddress | adviaddress | varchar | 140 |  |  | '' | adviaddress |
| 53 | fopendate | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 54 | fpresentperiod | presentperiod | varchar | 100 |  |  | '' | presentperiod |
| 55 | fcontractamount | 金额1 | numeric | 23 | 10 |  | null | 金额1 |
| 56 | fpaytype | paytype | varchar | 1 |  |  | '' | paytype |
| 57 | fcontractno | contractno | varchar | 30 |  |  | '' | contractno |
| 58 | fduedate | 长日期1 | timestamp | 0 |  |  | null | 长日期1 |
| 59 | fmixdraftinvamt | mixdraftinvamt | numeric | 23 | 10 |  | null | mixdraftinvamt |
| 60 | fupdatetime | updatetime | timestamp | 0 |  |  | null | updatetime |
| 61 | fbankloginid | bankloginid | varchar | 20 |  | √ | '' | bankloginid |
| 62 | fstatusmsg | statusmsg | varchar | 200 |  |  | '' | statusmsg |
| 63 | fcashway | cashway | varchar | 1 |  |  | '' | cashway |
| 64 | fpresentday | presentday | varchar | 10 |  |  | '' | presentday |
| 65 | fimplclassname | implclassname | varchar | 120 |  | √ | '' | implclassname |
| 66 | fexplain | explain | varchar | 250 |  |  | '' | explain |
| 67 | fbankversionid | bankversionid | varchar | 20 |  | √ | '' | bankversionid |
| 68 | fapplicantcreditnum | applicantcreditnum | varchar | 50 |  |  | '' | applicantcreditnum |
| 69 | fcreditmode | creditmode | varchar | 3 |  |  | '' | creditmode |
| 70 | fdetailbizno | detailbizno | varchar | 32 |  |  | '' | detailbizno |
| 71 | fbankrefdate | bankrefdate | varchar | 10 |  |  | '' | bankrefdate |
| 72 | ffileurl | fileurl | varchar | 100 |  |  | '' | fileurl |
| 73 | faddclause | addclause | varchar | 50 |  |  | '' | addclause |
| 74 | fstatusname | statusname | varchar | 20 |  |  | '' | statusname |
| 75 | fdocclause_tag | docclause_详情 | text | 0 |  |  | null | docclause_详情 |
| 76 | febgid | ebgid | varchar | 50 |  |  | '' | ebgid |
| 77 | fconinstructions | coninstructions | varchar | 1 |  |  | '' | coninstructions |
| 78 | fcostbear | costbear | varchar | 2 |  |  | '' | costbear |
| 79 | fbatchseqid | batchseqid | varchar | 50 |  | √ | '' | batchseqid |
| 80 | fistranship | istranship | varchar | 3 |  |  | '' | istranship |
| 81 | fcharcurrency | charcurrency | varchar | 5 |  |  | '' | charcurrency |
| 82 | ferrormsg | errormsg | varchar | 200 |  |  | '' | errormsg |
| 83 | fcreditform | creditform | varchar | 3 |  |  | '' | creditform |
| 84 | fdraweecnapscode | draweecnapscode | varchar | 15 |  |  | '' | draweecnapscode |
| 85 | fsubbiztype | subbiztype | varchar | 20 |  | √ | '' | subbiztype |
| 86 | fforwardaddress | forwardaddress | varchar | 200 |  |  | '' | forwardaddress |
| 87 | fsubmitsuccesstime | submitsuccesstime | timestamp | 0 |  |  | null | submitsuccesstime |
| 88 | freserved2 | reserved2 | varchar | 20 |  |  | '' | reserved2 |
| 89 | fbankdetailseqid | bankdetailseqid | varchar | 30 |  | √ | '' | bankdetailseqid |
| 90 | fmrgnacctype | mrgnacctype | varchar | 2 |  |  | '' | mrgnacctype |
| 91 | freserved1 | reserved1 | varchar | 20 |  |  | '' | reserved1 |
| 92 | fcharaccno | characcno | varchar | 50 |  |  | '' | characcno |
| 93 | fdocclause | docclause | varchar | 50 |  |  | '' | docclause |
| 94 | fapplicantaddressen | applicantaddressen | varchar | 250 |  |  | '' | applicantaddressen |
| 95 | flastsynctime | lastsynctime | timestamp | 0 |  |  | null | lastsynctime |
| 96 | fcounteraddress | counteraddress | varchar | 200 |  |  | '' | counteraddress |
| 97 | fstartair | startair | varchar | 250 |  |  | '' | startair |
| 98 | flessproportion | lessproportion | varchar | 10 |  |  | '' | lessproportion |
| 99 | faccno | accno | varchar | 30 |  | √ | '' | accno |
| 100 | fflowserialno | flowserialno | varchar | 30 |  |  | '' | flowserialno |
| 101 | fmixdraftinvproportion | mixdraftinvproportion | varchar | 4 |  |  | '' | mixdraftinvproportion |
| 102 | foprnm | oprnm | varchar | 50 |  |  | '' | oprnm |
| 103 | frequesttime | requesttime | timestamp | 0 |  |  | null | requesttime |
| 104 | fbankserialno | bankserialno | varchar | 50 |  |  | '' | bankserialno |
| 105 | fcustomid | customid | varchar | 50 |  | √ | '' | customid |
| 106 | fbankstatus | bankstatus | varchar | 20 |  |  | '' | bankstatus |
| 107 | fpackagekey | packagekey | varchar | 100 |  |  | '' | packagekey |
| 108 | fdueaddress | dueaddress | varchar | 200 |  |  | '' | dueaddress |
| 109 | fqueryimplclassname | queryimplclassname | varchar | 120 |  | √ | '' | queryimplclassname |
| 110 | fcurrency | currency | varchar | 5 |  |  | '' | currency |
| 111 | fpackagetime | packagetime | timestamp | 0 |  |  | null | packagetime |
| 112 | fdraftamt | draftamt | numeric | 23 | 10 |  | null | draftamt |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_open_credit_0 |  | fbatchseqid |
| 2 | idx_aqap_open_credit_1 |  | fbankbatchseqid |
| 3 | idx_aqap_open_credit_2 |  | fdetailbizno |
| 4 | t_aqap_open_credit_pkey |  | fid |

---

## 开证记录表-多语言表 t_aqap_open_credit_l

- **表名称：** 开证记录表-多语言表
- **表名：** t_aqap_open_credit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_open_credit_l_pkey |  | fpkid |
| 2 | idx_aqap_open_credit_l_0 |  | fid,flocaleid |
