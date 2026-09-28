# 增值税汇总核算总分支机构税款分配计算表-tcvat_ybhz_yz_zfjgfpb

## 增值税汇总核算总分支机构税款分配计算表-主表 t_tcvat_ybhz_yz_zfjgfpb

- **表名称：** 增值税汇总核算总分支机构税款分配计算表-主表
- **表名：** t_tcvat_ybhz_yz_zfjgfpb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnormaltaxsale | 一般计税方法销售额 | numeric | 23 | 10 | √ | 0 | 一般计税方法销售额 |
| 3 | fjxsezce | 进项税额转出额 | numeric | 23 | 10 | √ | 0 | 进项税额转出额 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计行 2 :动态行 |
| 5 | fbqsjjjdje | 本期实际加计抵减额 | numeric | 23 | 10 | √ | 0 | 本期实际加计抵减额 |
| 6 | fzfjgynse | 总分支机构应纳税额 | numeric | 23 | 10 | √ | 0 | 总分支机构应纳税额 |
| 7 | fjyjsynse | 简易计税方法应纳税额 | numeric | 23 | 10 | √ | 0 | 简易计税方法应纳税额 |
| 8 | fcorporatename | 总分支公司名称 | varchar | 100 |  | √ | ' ' | 总分支公司名称 |
| 9 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0 | 进项税额 |
| 10 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0 | 应纳税额减征额 |
| 11 | fynsefpe | 应纳税额分配额 | numeric | 23 | 10 | √ | 0 | 应纳税额分配额 |
| 12 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0 | 销项税额 |
| 13 | fsqldse | 上期留抵税额 | numeric | 23 | 10 | √ | 0 | 上期留抵税额 |
| 14 | funifiedsocialcode | 统一社会信用代码 | varchar | 50 |  | √ | ' ' | 统一社会信用代码 |
| 15 | ffpl | 三级分支机构分配率 | numeric | 23 | 10 | √ | 0 | 三级分支机构分配率 |
| 16 | fynsefpse | 应纳税额(分配税额) | numeric | 23 | 10 | √ | 0 | 应纳税额(分配税额) |
| 17 | ffpbl | 分配比例 | numeric | 23 | 10 | √ | 0 | 分配比例 |
| 18 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 19 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 20 | fybjsynse | 一般计税方法应纳税额 | numeric | 23 | 10 | √ | 0 | 一般计税方法应纳税额 |
| 21 | frowno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_yz_zfjgfpb |  | fid |
| 2 | idx_t_tcvat_ybhz_yz_zfjgfpb_s |  | fsbbid |
