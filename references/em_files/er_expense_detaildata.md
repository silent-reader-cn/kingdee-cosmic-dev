# 费用明细信息表-er_expense_detaildata

## 费用明细信息表-主表 t_er_expense_detail_data

- **表名称：** 费用明细信息表-主表
- **表名：** t_er_expense_detail_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentryamount | 报销金额（本位币） | numeric | 23 | 10 | √ | 0 | 报销金额（本位币） |
| 3 | fentryappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 4 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 5 | fcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 7 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcompany | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fquarter | 季度 | int8 | 64 |  | √ | 0 | 季度 |
| 10 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0 | 核定不含税金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foricurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fyearmonth | 年月 | int8 | 64 |  | √ | 0 | 年月 |
| 17 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定不含税金额（本位币） |
| 18 | fencashamount | 付现金额 | numeric | 23 | 10 | √ | 0 | 付现金额 |
| 19 | fstdproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | ftravelitem | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | forientryamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 27 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 事由 | varchar | 600 |  | √ | ' ' | 事由 |
| 30 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 31 | fyear | 年份 | int8 | 64 |  | √ | 0 | 年份 |
| 32 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 33 | forientryappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: er_publicreimbursebill :对公报销单 er_dailyreimbursebill :费用报销单 er_tripreimbursebill :差旅报销单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_detail_data_fbillid |  | fbillid |
| 2 | pk_er_expense_detail_data |  | fid |

---

## 报销人-多选基础资料表 t_er_detaildata_reimburse

- **表名称：** 报销人-多选基础资料表
- **表名：** t_er_detaildata_reimburse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_detaildata_reim_fid |  | fid |
| 2 | pk_er_detaildata_reimburse |  | fpkid |
