# 财产行为税附表-房产税小计-tcret_ccxws_fcs_xj_fb

## 财产行为税附表-房产税小计-主表 t_tcret_ccxws_fcsxj_fb

- **表名称：** 财产行为税附表-房产税小计-主表
- **表名：** t_tcret_ccxws_fcsxj_fb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 3 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 4 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 5 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_ccxws_fcsxj_fb |  | fid |
| 2 | idx_tcret_ccxws_fcsxj_fb |  | fsbbid |
