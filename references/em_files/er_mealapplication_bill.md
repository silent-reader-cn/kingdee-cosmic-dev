# 用餐申请单-er_mealapplication_bill

## 内部参与人员-多选基础资料表 t_er_internaluser

- **表名称：** 内部参与人员-多选基础资料表
- **表名：** t_er_internaluser

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
| 1 | pk_t_er_internaluser |  | fpkid |
| 2 | idx_er_internaluser_fk |  | fid |

---

## 用餐申请单-多语言表 t_er_mealapplication_bill_l

- **表名称：** 用餐申请单-多语言表
- **表名：** t_er_mealapplication_bill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mealapplication_bill_l |  | fid,flocaleid |
| 2 | pk_t_er_mealapplication_bill_l |  | fpkid |

---

## 用餐申请单-主表 t_er_mealapplication_bill

- **表名称：** 用餐申请单-主表
- **表名：** t_er_mealapplication_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdinnerstandard | 用餐标准 | varchar | 50 |  | √ | ' ' | 用餐标准 |
| 4 | fdinneramount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fstdexpquotetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 7 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | ftripamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 12 | fenddate | 用餐日期.结束 | timestamp | 0 |  |  | null | 用餐日期.结束 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 15 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | ftripexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | finternalhighestlevel | 内部参与人最高级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fentrycurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fdescription | 用餐事由 | varchar | 600 |  | √ | ' ' | 用餐事由 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fapplierposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 26 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fdinnerscene | 用餐场景 | varchar | 50 |  | √ | ' ' | 用餐场景,枚举: 1 :商务宴请 5 :团建用餐 4 :工作用餐 |
| 28 | fstartdate | 用餐日期.开始 | timestamp | 0 |  |  | null | 用餐日期.开始 |
| 29 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 30 | fcityfield | 用餐城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 31 | fdinnerusernum | 用餐人数 | varchar | 50 |  | √ | ' ' | 用餐人数 |
| 32 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 33 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mbill_fcompanyid |  | fcompanyid |
| 2 | pk_t_er_mealapplication_bill |  | fid |
| 3 | idx_er_mealapplicationbill_fk |  | fbillno |
| 4 | idx_er_mbill_fbizdate_fbillno |  | fbillno,fbizdate |
