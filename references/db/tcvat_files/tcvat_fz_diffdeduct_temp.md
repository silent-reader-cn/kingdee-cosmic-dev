# 差额扣除模板-tcvat_fz_diffdeduct_temp

## 差额扣除模板-主表 t_tcvat_fz_diffdeduct

- **表名称：** 差额扣除模板-主表
- **表名：** t_tcvat_fz_diffdeduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | fdifftypeid | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 8 | fproject | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 9 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 10 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_fz_diffdeduct |  | fstartdate,fenddate,forgid |
| 2 | pk_tcvat_fz_diffdeduct |  | fid |
