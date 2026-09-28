# 总机构差额扣除模板-tcvat_hz_diffdeduct_sjjt

## 总机构差额扣除模板-主表 t_tcvat_hz_diff_temp_sjjt

- **表名称：** 总机构差额扣除模板-主表
- **表名：** t_tcvat_hz_diff_temp_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifftypeid | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 6 | fdeductamount | 本期实际扣除额 | numeric | 23 | 10 | √ | 0 | 本期实际扣除额 |
| 7 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 8 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 9 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 11 | fproject | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 12 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 13 | fdeductiontype | 免税性质代码及名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | fsuborg | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |
| 16 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_diff_temp_sjjt |  | fid |
| 2 | idx_t_tcvat_hz_diff_temp_sjjt |  | forgid,fstartdate,fenddate |
