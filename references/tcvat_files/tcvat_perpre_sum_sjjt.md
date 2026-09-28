# 一般纳税人计提分次预缴底稿单据-tcvat_perpre_sum_sjjt

## 一般纳税人计提分次预缴底稿单据-主表 t_tcvat_perpre_sum_sjjt

- **表名称：** 一般纳税人计提分次预缴底稿单据-主表
- **表名：** t_tcvat_perpre_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 6 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 7 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 8 | fperpreproject | 分次预缴项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 9 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_perpre_sum_jt_orgdate |  | forgid,ftaxperiod,fdeadline |
| 2 | idx_taxc_perpre_sum_jt_serial |  | fserialno |
| 3 | pk_tcvat_perpre_sum_sjjt |  | fid |
