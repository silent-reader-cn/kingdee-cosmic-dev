# 用餐申请单-er_mealapplication_bill

## 内部参与人员-多选基础资料表 t_er_internaluser

- **表名称：** 内部参与人员-多选基础资料表
- **表名：** t_er_internaluser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 2 | fcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdinnerstandard | 用餐标准 | varchar | 50 |  | √ | ' ' | 用餐标准 |
| 4 | fdinneramount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fstdexpquotetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 7 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftripamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 9 | fheadproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 13 | fenddate | 用餐日期.结束 | timestamp | 0 |  |  | null | 用餐日期.结束 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 16 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 17 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | ftripexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | finternalhighestlevel | 内部参与人最高级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fentrycurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fdescription | 用餐事由 | varchar | 600 |  | √ | ' ' | 用餐事由 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fapplierposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 28 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fdinnerscene | 用餐场景 | varchar | 50 |  | √ | ' ' | 用餐场景,枚举: 1 :商务宴请 5 :团建用餐 4 :工作用餐 |
| 30 | fstartdate | 用餐日期.开始 | timestamp | 0 |  |  | null | 用餐日期.开始 |
| 31 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 32 | fcityfield | 用餐城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 33 | fdinnerusernum | 用餐人数 | varchar | 50 |  | √ | ' ' | 用餐人数 |
| 34 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 35 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

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
