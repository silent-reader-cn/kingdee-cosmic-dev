# 财产和行为税附表-环保税-tcret_ccxws_hbs_fb

## 财产和行为税附表-环保税-主表 t_tcret_ccxws_hbs_fb

- **表名称：** 财产和行为税附表-环保税-主表
- **表名：** t_tcret_ccxws_hbs_fb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsybh | 税源编号 | varchar | 50 |  | √ | ' ' | 税源编号 |
| 3 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 4 | fjmxzdm | 减免性质代码和项目名称 | varchar | 500 |  | √ | ' ' | 减免性质代码和项目名称 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 6 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 7 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 8 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 9 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 10 | fwrwlb | 污染物类别 | varchar | 50 |  | √ | ' ' | 污染物类别 |
| 11 | fwrwmc | 污染物名称 | varchar | 50 |  | √ | ' ' | 污染物名称 |
| 12 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_ccxws_hbs_fb |  | fid |
| 2 | idx_tcret_ccxws_hbs_fb |  | fsbbid,fewblxh |
