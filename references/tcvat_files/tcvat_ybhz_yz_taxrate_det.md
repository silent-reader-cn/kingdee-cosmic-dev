# 汇总税额预征明细参数单据-tcvat_ybhz_yz_taxrate_det

## 汇总税额预征明细参数单据-主表 t_tcvat_ybhz_yz_taxrate_d

- **表名称：** 汇总税额预征明细参数单据-主表
- **表名：** t_tcvat_ybhz_yz_taxrate_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | fzjgsqqbljxse | 总机构上期全部累计销售额 | numeric | 23 | 10 | √ | 0 | 总机构上期全部累计销售额 |
| 4 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fzjgdqqbljxse | 总机构当期全部累计销售额 | numeric | 23 | 10 | √ | 0 | 总机构当期全部累计销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_yz_taxrate_d |  | fid |
| 2 | idx_taxc_yzcs_org_date |  | forgid,fstartdate,fenddate |
