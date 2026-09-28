# 累计数据初始化-tcvat_totaldata_init

## 累计数据初始化-主表 t_tcvat_totaldata_init

- **表名称：** 累计数据初始化-主表
- **表名：** t_tcvat_totaldata_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fhgzyjksse | 累计已抵扣海关专用缴款书增值税税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣海关专用缴款书增值税税额 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fsndzcze | 上年度末资产总额 | numeric | 23 | 10 | √ | 0 | 上年度末资产总额 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsndcxqjxse | 上年度存续期间增值税销售额合计 | numeric | 23 | 10 | √ | 0 | 上年度存续期间增值税销售额合计 |
| 9 | finputrate | 进项构成比例(%) | numeric | 23 | 10 | √ | 0 | 进项构成比例(%) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 12 | fzzszyfpse | 累计已抵扣增值税专用发票税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣增值税专用发票税额 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fsndxse | 上年度增值税应税销售额合计 | numeric | 23 | 10 | √ | 0 | 上年度增值税应税销售额合计 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftotalmonth | 上年度企业存续月数 | varchar | 50 |  | √ | ' ' | 上年度企业存续月数 |
| 17 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 18 | fljdkse | 累计已抵扣的全部进项税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣的全部进项税额 |
| 19 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :数据引入 2 :手工新增 |
| 20 | fljdkjjkwspzse | 累计已抵扣解缴税款完税凭证注明的增值税额 | numeric | 23 | 10 | √ | 0 | 累计已抵扣解缴税款完税凭证注明的增值税额 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_totaldata_init |  | fid |
| 2 | idx_tcvat_totaldata_init |  | forgid,fskssqq,fskssqz |
