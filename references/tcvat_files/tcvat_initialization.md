# 留抵退税数据初始化(废弃)-tcvat_initialization

## 留抵退税数据初始化(废弃)-主表 t_tcvat_initialization

- **表名称：** 留抵退税数据初始化(废弃)-主表
- **表名：** t_tcvat_initialization

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrefundallowed | 允许退还税额 | numeric | 23 | 10 | √ | 0.0000000000 | 允许退还税额 |
| 3 | fendamount | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frefundstatus | 退税状态 | varchar | 30 |  | √ | ' ' | 退税状态,枚举: 1 :已确认 2 :未确认 |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | finputisproportional | 进项构成比例 | numeric | 23 | 10 | √ | 0.0000000000 | 进项构成比例 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fthantaxperiod | 比对税期 | timestamp | 0 |  |  | null | 比对税期 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | ftaxrebatesjudge | 退税判断 | varchar | 30 |  | √ | ' ' | 退税判断,枚举: 1 :符合退税条件 2 :不符合退税条件。不满足：连续六个月增量留抵税额均大于零，且第六个月增量留抵税额不低于50万元 3 :不符合退税条件，纳税信用等级不是A级或B级 4 :不符合退税条件，不满足：增量留抵税额大于零 |
| 12 | ftaxrefundperiod | 退税所属期 | timestamp | 0 |  |  | null | 退税所属期 |
| 13 | fallspecialtickets | 全部已抵扣进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 全部已抵扣进项税额 |
| 14 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | factualfundallowed | 实际退还税额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际退还税额 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | ftaxrefundenterprise | 退税企业类型 | varchar | 30 |  | √ | ' ' | 退税企业类型,枚举: A :一般企业 B :先进制造业企业 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | ftaxspecialtickets | 已抵扣专票等税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已抵扣专票等税额 |
| 20 | ftaxcreditrating | 纳税信用等级 | varchar | 30 |  | √ | ' ' | 纳税信用等级,枚举: A :A B :B M :M C :C D :D |
| 21 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fincrementamount | 增量留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 增量留抵税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_initialization_pkey |  | fid |
| 2 | idx_tcvat_initialization |  | forg,ftaxrefundperiod |
