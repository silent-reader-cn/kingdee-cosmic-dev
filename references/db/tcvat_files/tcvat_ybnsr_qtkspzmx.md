# 其他扣税凭证明细表-tcvat_ybnsr_qtkspzmx

## 其他扣税凭证明细表-主表 t_tcvat_ybnsr_qtkspzmx

- **表名称：** 其他扣税凭证明细表-主表
- **表名：** t_tcvat_ybnsr_qtkspzmx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fje | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :桥、闸通行费 2 :国内旅客运输服务 3 :尚未抵扣完毕的不动产或者不动产在建工程 4 :固定资产、无形资产、不动产转变用途可以抵扣的进项税额 5 :合计 |
| 4 | ffs | 份数 | int8 | 64 |  | √ | 0 | 份数 |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | fse | 税额 | numeric | 23 | 10 |  | null | 税额 |
| 7 | fewblname | 二维表行名称 | varchar | 150 |  | √ | ' ' | 二维表行名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_ybnsr_qtkspzmx_sbid |  | fsbbid |
| 2 | pk_tcvat_ybnsr_qtkspzmx |  | fid |
