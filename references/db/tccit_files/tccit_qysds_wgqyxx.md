# 被投资外国企业信息-tccit_qysds_wgqyxx

## 被投资外国企业信息-主表 t_tccit_qysds_wgqyxx

- **表名称：** 被投资外国企业信息-主表
- **表名：** t_tccit_qysds_wgqyxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fszgnssbh | 5.所在国纳税识别号 | varchar | 100 |  | √ | ' ' | 5.所在国纳税识别号 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :企业信息 |
| 4 | fwgqywwmc | 3.外国企业外文名称 | varchar | 600 |  | √ | ' ' | 3.外国企业外文名称 |
| 5 | fzyywlx | 6.主营业务类型 | varchar | 600 |  | √ | ' ' | 6.主营业务类型 |
| 6 | fwgqyzwcld | 2.外国企业中文成立地 | varchar | 600 |  | √ | ' ' | 2.外国企业中文成立地 |
| 7 | fwgqyzwmc | 1.外国企业中文名称 | varchar | 600 |  | √ | ' ' | 1.外国企业中文名称 |
| 8 | fbgrcgbl | 7.报告人持股比例 | numeric | 23 | 10 | √ | 0.0000000000 | 7.报告人持股比例 |
| 9 | fwgqywwcld | 4.外国企业外文成立地 | varchar | 600 |  | √ | ' ' | 4.外国企业外文成立地 |
| 10 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 11 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_qysds_wgqyxx_pkey |  | fid |
| 2 | idx_tccit_qysds_wgqyxx |  | fsbbid |
