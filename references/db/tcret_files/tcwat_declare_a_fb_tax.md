# 申报表A减免附表税款-tcwat_declare_a_fb_tax

## 申报表A减免附表税款-主表 t_tcwat_declare_a_fb_tax

- **表名称：** 申报表A减免附表税款-主表
- **表名：** t_tcwat_declare_a_fb_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fjmxzdm | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :水资源类型1 3 :水资源类型2 4 :水资源类型3 999 :合计 |
| 5 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 6 | fbqsyse | 本期适用税额 | numeric | 23 | 10 | √ | 0 | 本期适用税额 |
| 7 | fbqjmse | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 8 | fjmsxmmc | 减免税项目名称 | varchar | 50 |  | √ | ' ' | 减免税项目名称 |
| 9 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 10 | fjzbl | 减征比例 | numeric | 23 | 10 | √ | 0 | 减征比例 |
| 11 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 12 | fjmssl | 减免税水量 | numeric | 23 | 10 | √ | 0 | 减免税水量 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcwat_declare_afbtax |  | fsbbid,fewblxh |
| 2 | pk_tcwat_declare_a_fb_tax |  | fid |
