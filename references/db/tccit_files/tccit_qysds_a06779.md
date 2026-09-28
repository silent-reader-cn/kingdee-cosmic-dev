# 企业所得税A06779-tccit_qysds_a06779

## 企业所得税A06779-主表 t_tccit_qysds_a06779

- **表名称：** 企业所得税A06779-主表
- **表名：** t_tccit_qysds_a06779

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdysd | 递延所得 | numeric | 23 | 10 | √ | 0 | 递延所得 |
| 3 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 4 | frownumber | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 5 | fobtaindate | 取得股权时间 | timestamp | 0 |  |  | null | 取得股权时间 |
| 6 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行次 |
| 7 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 8 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 9 | ftaxbase | 计税基础 | numeric | 23 | 10 | √ | 0 | 计税基础 |
| 10 | ftechno | 技术成果编号 | varchar | 100 |  | √ | ' ' | 技术成果编号 |
| 11 | ftechtype | 技术成果类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fbusinessname | 企业名称 | varchar | 50 |  | √ | ' ' | 企业名称 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | ftechname | 技术成果名称 | varchar | 100 |  | √ | ' ' | 技术成果名称 |
| 15 | fheadernsrsbh | 表头纳税人识别号 | varchar | 50 |  | √ | ' ' | 表头纳税人识别号 |
| 16 | ffairvalue | 公允价值 | numeric | 23 | 10 | √ | 0 | 公允价值 |
| 17 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 18 | fassociated | 与投资方是否为关联企业 | varchar | 50 |  | √ | ' ' | 与投资方是否为关联企业,枚举: 0 :否 1 :是 |
| 19 | fheaderyear | 年度 | varchar | 50 |  | √ | ' ' | 年度 |
| 20 | fheadernsrmc | 表头纳税人名称 | varchar | 100 |  | √ | ' ' | 表头纳税人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_a06779_fsbbid |  | fsbbid |
| 2 | pk_tccit_qysds_a06779 |  | fid |
