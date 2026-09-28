# 总机构分次预缴计提单据-tcvat_hz_perpre_sum_jt

## 总机构分次预缴计提单据-主表 t_tcvat_hz_perpre_sum_jt

- **表名称：** 总机构分次预缴计提单据-主表
- **表名：** t_tcvat_hz_perpre_sum_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 5 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 6 | fperpreproject | 分次预缴项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 7 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 10 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 11 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 12 | fsuborg | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |
| 14 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_perpre_hz_sumjt_seria |  | fserialno |
| 2 | pk_tcvat_hz_perpre_sum_jt |  | fid |
