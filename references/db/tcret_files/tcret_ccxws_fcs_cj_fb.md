# 财产和行为税附表-房产税从价-tcret_ccxws_fcs_cj_fb

## 财产和行为税附表-房产税从价-主表 t_tcret_ccxws_fcscj_fb

- **表名称：** 财产和行为税附表-房产税从价-主表
- **表名：** t_tcret_ccxws_fcscj_fb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | fjmxzdm | 减免性质代码和项目名称 | varchar | 500 |  | √ | ' ' | 减免性质代码和项目名称 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 5 | ffcbm | 房产编码 | varchar | 50 |  | √ | ' ' | 房产编码 |
| 6 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 7 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 8 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 9 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 10 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_ccxws_fcscj_fb |  | fsbbid |
| 2 | pk_tcret_ccxws_fcscj_fb |  | fid |
| 3 | idx_tcret_ccxws_fcscj_fb_1 |  | fewblxh,fsbbid |
