# A109010分支机构信息动态行-tccit_qysds_a109010_dyn

## A109010分支机构信息动态行-主表 t_tccit_qysds_a109010_dyn

- **表名称：** A109010分支机构信息动态行-主表
- **表名：** t_tccit_qysds_a109010_dyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxsmzdfyhfd | 享受民族地方优惠幅度 | numeric | 23 | 10 | √ | 0 | 享受民族地方优惠幅度 |
| 3 | frownumber | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 4 | fqnljfpje | 全年累计分配金额 | numeric | 23 | 10 | √ | 0 | 全年累计分配金额 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 99 :合计 |
| 6 | fsjfpsdse | 实际分配所得税额 | numeric | 23 | 10 | √ | 0 | 实际分配所得税额 |
| 7 | fftybsdse | 分摊应补(退)所得税额 | numeric | 23 | 10 | √ | 0 | 分摊应补(退)所得税额 |
| 8 | ffzjggzze | 4.职工薪酬 | numeric | 23 | 10 | √ | 0 | 4.职工薪酬 |
| 9 | fxsmzdfyhje | 应享受民族地方优惠金额 | numeric | 23 | 10 | √ | 0 | 应享受民族地方优惠金额 |
| 10 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 11 | ffzjglxlb | 分支机构类型类别 | varchar | 50 |  | √ | ' ' | 分支机构类型类别 |
| 12 | fymzdfyhtzfpje | 因民族地方优惠调整分配金额 | numeric | 23 | 10 | √ | 0 | 因民族地方优惠调整分配金额 |
| 13 | ffpse | 7.分配所得税额 | numeric | 23 | 10 | √ | 0 | 7.分配所得税额 |
| 14 | ffzjgzcze | 5.资产总额 | numeric | 23 | 10 | √ | 0 | 5.资产总额 |
| 15 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :正常 0 :注销 |
| 16 | ffzjgzgswjdm | 分支机构税务机关代码 | varchar | 50 |  | √ | ' ' | 分支机构税务机关代码 |
| 17 | ffzjgsrze | 3.营业收入 | numeric | 23 | 10 | √ | 0 | 3.营业收入 |
| 18 | ffpbl | 6.分配比例 | numeric | 23 | 10 | √ | 0 | 6.分配比例 |
| 19 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 20 | fqnljyxsmzdfyhje | 全年累计已享受民族地方优惠金额 | numeric | 23 | 10 | √ | 0 | 全年累计已享受民族地方优惠金额 |
| 21 | ffzjgyhbasedata | 分支机构享受区域性优惠情况 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 22 | ffzjgnsrsbh | 1.分支机构纳税人识别号 | varchar | 50 |  | √ | ' ' | 1.分支机构纳税人识别号 |
| 23 | ffzjgmc | 2.分支机构名称 | varchar | 300 |  | √ | ' ' | 2.分支机构名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_a109010_dyn_fsbbid |  | fsbbid |
| 2 | pk_tccit_qysds_a109010_dyn |  | fid |
