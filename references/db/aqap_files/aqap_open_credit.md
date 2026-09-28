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
| 6 | fpayaccno2 | payaccno | varchar | 80 |  |  | '' | payaccno |
| 7 | fforwardcnapscode | forwardcnapscode | varchar | 15 |  |  | '' | forwardcnapscode |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftermini | termini | varchar | 250 |  |  | '' | termini |
| 10 | fpayacccurrency2 | payacccurrency | varchar | 5 |  |  | '' | payacccurrency |
| 11 | fcredittype | credittype1 | varchar | 2 |  |  | '' | credittype1 |
| 12 | facceptorcnapscode | acceptorcnapscode | varchar | 15 |  |  | '' | acceptorcnapscode |
| 13 | ffilename | filename | varchar | 50 |  |  | '' | filename |
| 14 | fpaydays | paydays | varchar | 8 |  |  | '' | paydays |
| 15 | fmrgnaccno | mrgnaccno | varchar | 50 |  |  | '' | mrgnaccno |
| 16 | fdraftcustflg | draftcustflg | varchar | 6 |  |  | '' | draftcustflg |
| 17 | fmixtenordays | mixtenordays | varchar | 8 |  |  | '' | mixtenordays |
| 18 | fcountercountry | counterCountry | varchar | 100 |  |  | null | counterCountry |
| 19 | fmrgnproportion | mrgnproportion | varchar | 8 |  |  | '' | mrgnproportion |
| 20 | fversion | version | int8 | 64 |  |  | null | version |
| 21 | fbankbatchseqid | bankbatchseqid | varchar | 30 |  | √ | '' | bankbatchseqid |
| 22 | fname | 名称 | varchar | 50 |  |  | '' | 名称 |
| 23 | favwtbank | avwtbank | varchar | 1 |  |  | '' | avwtbank |
| 24 | fpayamt2 | payamt | numeric | 23 | 10 |  | null | payamt |
| 25 | facceptoraddress | acceptoraddress | varchar | 200 |  |  | '' | acceptoraddress |
| 26 | fterminiair | terminiair | varchar | 250 |  |  | '' | terminiair |
| 27 | finserttime | inserttime | timestamp | 0 |  |  | null | inserttime |
| 28 | fpayfinishtime | payfinishtime | timestamp | 0 |  |  | null | payfinishtime |
| 29 | fshipdate | shipdate | varchar | 10 |  |  | '' | shipdate |
| 30 | fmrgncurrency | mrgncurrency | varchar | 5 |  |  | '' | mrgncurrency |
| 31 | fpayacccurrency | payacccurrency | varchar | 5 |  |  | '' | payacccurrency |
| 32 | fpaynature | paynature | varchar | 5 |  |  | '' | paynature |
| 33 | foprtel | oprtel | varchar | 20 |  |  | '' | oprtel |
| 34 | freduceamt | reduceAmt | numeric | 23 | 10 |  | null | reduceAmt |
| 35 | fenable | 使用状态 | varchar | 50 |  |  | '' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fgasdescription | gasdescription | varchar | 250 |  |  | '' | gasdescription |
| 37 | fnumber | 编码 | varchar | 30 |  |  | '' | 编码 |
| 38 | fmixtenortype | mixtenortype | varchar | 1 |  |  | '' | mixtenortype |
| 39 | fdeliveryport | deliveryport | varchar | 250 |  |  | '' | deliveryport |
| 40 | frefusepoint | refusepoint | varchar | 50 |  |  | null | refusepoint |
| 41 | fbankmsg | bankmsg | varchar | 200 |  |  | '' | bankmsg |
| 42 | fadvicnapscode | advicnapscode | varchar | 15 |  |  | '' | advicnapscode |
| 43 | frqstserialno | rqstserialno | varchar | 30 |  |  | '' | rqstserialno |
| 44 | fdetailseqid | detailseqid | varchar | 32 |  |  | '' | detailseqid |
| 45 | fmoreproportion | moreproportion | varchar | 10 |  |  | '' | moreproportion |
| 46 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 47 | favwtbanknmadd | avwtbanknmadd | varchar | 200 |  |  | '' | avwtbanknmadd |
| 48 | ftxnpscpt | txnpscpt | varchar | 500 |  |  | '' | txnpscpt |
| 49 | fstatus | 数据状态 | varchar | 50 |  |  | '' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 50 | fdraftproportion | draftproportion | varchar | 4 |  |  | '' | draftproportion |
| 51 | fbiztype | biztype | varchar | 20 |  | √ | '' | biztype |
| 52 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 54 | fsynccount | synccount | int8 | 64 |  |  | null | synccount |
| 55 | fcountername | 文本102 | varchar | 200 |  |  | '' | 文本102 |
| 56 | fcharfeeinfo_tag | charfeeinfo_详情 | text | 0 |  |  | null | charfeeinfo_详情 |
| 57 | fremark | remark | varchar | 250 |  |  | '' | remark |
| 58 | fbankrefkey | bankrefkey | varchar | 100 |  |  | '' | bankrefkey |
| 59 | freceiptplace | 接管地/发送地/接货地 | varchar | 70 |  |  | null | 接管地/发送地/接货地 |
| 60 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fcreditstatus | creditstatus | varchar | 20 |  |  | '' | creditstatus |
| 62 | fispartship | ispartship | varchar | 3 |  |  | '' | ispartship |
| 63 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 64 | fadviaddress | adviaddress | varchar | 140 |  |  | '' | adviaddress |
| 65 | fibppaytype | ibppaytype | varchar | 5 |  |  | '' | ibppaytype |
| 66 | fopendate | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 67 | fpresentperiod | presentperiod | varchar | 100 |  |  | '' | presentperiod |
| 68 | fcontractamount | 金额1 | numeric | 23 | 10 |  | null | 金额1 |
| 69 | fpaytype | paytype | varchar | 1 |  |  | '' | paytype |
| 70 | ftrancode | trancode | varchar | 10 |  |  | '' | trancode |
| 71 | fcontractno | contractno | varchar | 30 |  |  | '' | contractno |
| 72 | fdocs | docs | varchar | 5 |  |  | null | docs |
| 73 | ftransflag | transflag | varchar | 2 |  |  | null | transflag |
| 74 | fpayamt | payamt | numeric | 23 | 10 |  | null | payamt |
| 75 | fduedate | 长日期1 | timestamp | 0 |  |  | null | 长日期1 |
| 76 | fmixdraftinvamt | mixdraftinvamt | numeric | 23 | 10 |  | null | mixdraftinvamt |
| 77 | fupdatetime | updatetime | timestamp | 0 |  |  | null | updatetime |
| 78 | fbankloginid | bankloginid | varchar | 20 |  | √ | '' | bankloginid |
| 79 | fstatusmsg | statusmsg | varchar | 200 |  |  | '' | statusmsg |
| 80 | fcashway | cashway | varchar | 1 |  |  | '' | cashway |
| 81 | fpresentday | presentday | varchar | 10 |  |  | '' | presentday |
| 82 | fimplclassname | implclassname | varchar | 120 |  | √ | '' | implclassname |
| 83 | freturndesc | returndesc | varchar | 20 |  |  | '' | returndesc |
| 84 | fexplain | explain | varchar | 250 |  |  | '' | explain |
| 85 | fbankversionid | bankversionid | varchar | 20 |  | √ | '' | bankversionid |
| 86 | freject | reject | varchar | 500 |  |  | null | reject |
| 87 | fapplicantcreditnum | applicantcreditnum | varchar | 50 |  |  | '' | applicantcreditnum |
| 88 | fcreditmode | creditmode | varchar | 3 |  |  | '' | creditmode |
| 89 | fbuscurrency | buscurrency | varchar | 5 |  |  | '' | buscurrency |
| 90 | fmodfrequency | 文本114 | varchar | 5 |  |  | null | 文本114 |
| 91 | fdetailbizno | detailbizno | varchar | 32 |  |  | '' | detailbizno |
| 92 | fbankrefdate | bankrefdate | varchar | 10 |  |  | '' | bankrefdate |
| 93 | ffileurl | fileurl | varchar | 100 |  |  | '' | fileurl |
| 94 | ffeemode | 文本86 | varchar | 5 |  |  | '' | 文本86 |
| 95 | fpayeecountry | payeecountry | varchar | 5 |  |  | '' | payeecountry |
| 96 | faddclause | addclause | varchar | 50 |  |  | '' | addclause |
| 97 | fstatusname | statusname | varchar | 20 |  |  | '' | statusname |
| 98 | fdocclause_tag | docclause_详情 | text | 0 |  |  | null | docclause_详情 |
| 99 | febgid | ebgid | varchar | 50 |  |  | '' | ebgid |
| 100 | fapplicantname | applicantname | varchar | 200 |  |  | '' | applicantname |
| 101 | fconinstructions | coninstructions | varchar | 1 |  |  | '' | coninstructions |
| 102 | faddamt | addAmt | numeric | 23 | 10 |  | null | addAmt |
| 103 | fcostbear | costbear | varchar | 2 |  |  | '' | costbear |
| 104 | fbatchseqid | batchseqid | varchar | 50 |  | √ | '' | batchseqid |
| 105 | fmixtenor | 远期/混合付款期限 | varchar | 100 |  |  | '' | 远期/混合付款期限 |
| 106 | fistranship | istranship | varchar | 3 |  |  | '' | istranship |
| 107 | fcharcurrency | charcurrency | varchar | 5 |  |  | '' | charcurrency |
| 108 | ferrormsg | errormsg | varchar | 200 |  |  | '' | errormsg |
| 109 | fibpisref | ibpisref | varchar | 5 |  |  | '' | ibpisref |
| 110 | fcreditform | creditform | varchar | 3 |  |  | '' | creditform |
| 111 | fdraweecnapscode | draweecnapscode | varchar | 15 |  |  | '' | draweecnapscode |
| 112 | fsubbiztype | subbiztype | varchar | 20 |  | √ | '' | subbiztype |
| 113 | freturndesc_tag | returndesc_详情 | text | 0 |  |  | null | returndesc_详情 |
| 114 | fforwardaddress | forwardaddress | varchar | 200 |  |  | '' | forwardaddress |
| 115 | fsubmitsuccesstime | submitsuccesstime | timestamp | 0 |  |  | null | submitsuccesstime |
| 116 | freserved2 | reserved2 | varchar | 20 |  |  | '' | reserved2 |
| 117 | fbankdetailseqid | bankdetailseqid | varchar | 30 |  | √ | '' | bankdetailseqid |
| 118 | fbusamt | 金额4 | numeric | 23 | 10 |  | null | 金额4 |
| 119 | fmrgnacctype | mrgnacctype | varchar | 2 |  |  | '' | mrgnacctype |
| 120 | freserved1 | reserved1 | varchar | 20 |  |  | '' | reserved1 |
| 121 | fcharaccno | characcno | varchar | 50 |  |  | '' | characcno |
| 122 | fdocclause | docclause | varchar | 50 |  |  | '' | docclause |
| 123 | fapplicantaddressen | applicantaddressen | varchar | 250 |  |  | '' | applicantaddressen |
| 124 | flastsynctime | lastsynctime | timestamp | 0 |  |  | null | lastsynctime |
| 125 | fpayaccno | payaccno | varchar | 80 |  |  | '' | payaccno |
| 126 | fcounteraddress | counteraddress | varchar | 200 |  |  | '' | counteraddress |
| 127 | flastmoddate | 文本115 | varchar | 8 |  |  | null | 文本115 |
| 128 | fstartair | startair | varchar | 250 |  |  | '' | startair |
| 129 | flessproportion | lessproportion | varchar | 10 |  |  | '' | lessproportion |
| 130 | faccno | accno | varchar | 30 |  | √ | '' | accno |
| 131 | fflowserialno | flowserialno | varchar | 30 |  |  | '' | flowserialno |
| 132 | freceivedno | 文本84 | varchar | 40 |  |  | '' | 文本84 |
| 133 | fcorramt | corramt | numeric | 23 | 10 |  | null | corramt |
| 134 | fmixdraftinvproportion | mixdraftinvproportion | varchar | 4 |  |  | '' | mixdraftinvproportion |
| 135 | foprnm | oprnm | varchar | 50 |  |  | '' | oprnm |
| 136 | frequesttime | requesttime | timestamp | 0 |  |  | null | requesttime |
| 137 | fbankserialno | bankserialno | varchar | 50 |  |  | '' | bankserialno |
| 138 | fcustomid | customid | varchar | 50 |  | √ | '' | customid |
| 139 | fcontractcurrency | contractcurrency | varchar | 10 |  |  | null | contractcurrency |
| 140 | fcharges | 费用条款 | varchar | 20 |  |  | null | 费用条款 |
| 141 | fdrawon | 文本109 | varchar | 2 |  |  | null | 文本109 |
| 142 | fbankstatus | bankstatus | varchar | 20 |  |  | '' | bankstatus |
| 143 | fcharfeeinfo | charfeeinfo | varchar | 30 |  |  | '' | charfeeinfo |
| 144 | fpackagekey | packagekey | varchar | 100 |  |  | '' | packagekey |
| 145 | fdueaddress | dueaddress | varchar | 200 |  |  | '' | dueaddress |
| 146 | fqueryimplclassname | queryimplclassname | varchar | 120 |  | √ | '' | queryimplclassname |
| 147 | fcostbearparty | 文本85 | varchar | 5 |  |  | '' | 文本85 |
| 148 | flastshipdate | 最迟装运期 | varchar | 8 |  |  | '' | 最迟装运期 |
| 149 | fcurrency | currency | varchar | 5 |  |  | '' | currency |
| 150 | fafterfrom | afterFrom | varchar | 2 |  |  | null | afterFrom |
| 151 | fpackagetime | packagetime | timestamp | 0 |  |  | null | packagetime |
| 152 | fdocpcsmode | docpcsmode | varchar | 5 |  |  | '' | docpcsmode |
| 153 | fibpregno | ibpregno | varchar | 30 |  |  | '' | ibpregno |
| 154 | fdraftamt | draftamt | numeric | 23 | 10 |  | null | draftamt |
| 155 | facptdate | 长日期9 | timestamp | 0 |  |  | null | 长日期9 |

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
