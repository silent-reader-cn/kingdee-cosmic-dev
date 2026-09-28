# A202000分支机构信息-tccit_qysds_fzjgxx_dyn

## A202000分支机构信息-主表 t_tccit_qysds_fzjgxx_dyn

- **表名称：** A202000分支机构信息-主表
- **表名：** t_tccit_qysds_fzjgxx_dyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frownumber | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1.分支机构 count :合计行 |
| 4 | fmzqysdsdffxbfyhje | 民族自治地区企业所得税地方分享部分优惠金额 | numeric | 23 | 10 | √ | 0 | 民族自治地区企业所得税地方分享部分优惠金额 |
| 5 | ffzjgxsqyxyhqk | 分支机构享受区域性优惠情况 | varchar | 50 |  | √ | ' ' | 分支机构享受区域性优惠情况 |
| 6 | fftybsdse | 分摊应补(退)所得税额 | numeric | 23 | 10 | √ | 0 | 分摊应补(退)所得税额 |
| 7 | fsjftybsdse | 实际分摊应补（退）所得税额 | numeric | 23 | 10 | √ | 0 | 实际分摊应补（退）所得税额 |
| 8 | ffzjggzze | 4.职工薪酬 | numeric | 23 | 10 | √ | 0 | 4.职工薪酬 |
| 9 | fxsmzdfyhje | 享受民族地方优惠金额 | numeric | 23 | 10 | √ | 0 | 享受民族地方优惠金额 |
| 10 | fxsmzdfjmfd | 享受民族地方减免幅度 | numeric | 23 | 10 | √ | 0 | 享受民族地方减免幅度 |
| 11 | ffzjgxsqyyhbasedata | 分支机构享受区域性优惠情况基础资料 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 13 | ffpse | 7.分配所得税额 | numeric | 23 | 10 | √ | 0 | 7.分配所得税额 |
| 14 | ffzjgzcze | 5.资产总额 | numeric | 23 | 10 | √ | 0 | 5.资产总额 |
| 15 | fljyftsdse | 累计已分摊所得税额 | numeric | 23 | 10 | √ | 0 | 累计已分摊所得税额 |
| 16 | forgstatus | 机构状态 | varchar | 10 |  | √ | ' ' | 机构状态 |
| 17 | fqnljxsmzdfyhje | 全年累计已享受民族地方优惠金额 | numeric | 23 | 10 | √ | 0 | 全年累计已享受民族地方优惠金额 |
| 18 | ffzjgsrze | 3.营业收入 | numeric | 23 | 10 | √ | 0 | 3.营业收入 |
| 19 | ffpbl | 6.分配比例 | numeric | 23 | 10 | √ | 0 | 6.分配比例 |
| 20 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 21 | fzjgqk | 总机构情况 | varchar | 50 |  | √ | ' ' | 总机构情况 |
| 22 | ffzjgnsrsbh | 1.分支机构纳税人识别号 | varchar | 50 |  | √ | ' ' | 1.分支机构纳税人识别号 |
| 23 | ffzjgmc | 2.分支机构名称 | varchar | 300 |  | √ | ' ' | 2.分支机构名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idxt_tccit_qysds_fzjgxx_dyn_uq |  | fsbbid,fewblxh |
| 2 | pk_tccit_qysds_fzjgxx_dyn |  | fid |
