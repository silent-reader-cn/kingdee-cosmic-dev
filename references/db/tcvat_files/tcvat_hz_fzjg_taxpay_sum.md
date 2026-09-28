# 总机构分支机构预缴台账单据-tcvat_hz_fzjg_taxpay_sum

## 总机构分支机构预缴台账单据-主表 t_tcvat_hz_fz_taxpay_sum

- **表名称：** 总机构分支机构预缴台账单据-主表
- **表名：** t_tcvat_hz_fz_taxpay_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | ftaxrate | 预征率 | varchar | 50 |  | √ | ' ' | 预征率 |
| 4 | fsuborgid | 分支机构名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsalesamount | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 8 | ftaxpayamount | 已预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_fz_taxpay_sum |  | fid |
| 2 | idx_tcvat_hz_fz_taxpay_sum |  | forgid,fstartdate,fenddate |
