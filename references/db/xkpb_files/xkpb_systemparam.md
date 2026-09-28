# 项目预算系统参数-xkpb_systemparam

## 项目预算系统参数-主表 t_xkbm_systemparam

- **表名称：** 项目预算系统参数-主表
- **表名：** t_xkbm_systemparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbudgetdimensiongroup | fbudgetdimensiongroup | bpchar | 1 |  | √ | ' ' |  |
| 3 | fuploadaspdf | fuploadaspdf | bpchar | 1 |  | √ | ' ' |  |
| 4 | fiseditsubmitreport | fiseditsubmitreport | bpchar | 1 |  | √ | ' ' |  |
| 5 | fovertip | 超额编制提示 | bpchar | 1 |  | √ | ' ' | 超额编制提示 |
| 6 | fuploadasexcel | fuploadasexcel | bpchar | 1 |  | √ | ' ' |  |
| 7 | fuploadasexcellist | fuploadasexcellist | bpchar | 1 |  | √ | ' ' |  |
| 8 | fbudgetallownegative | fbudgetallownegative | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbudgetctrl | 启用预算控制 | bpchar | 1 |  | √ | ' ' | 启用预算控制 |
| 10 | fuploadasexceldev | fuploadasexceldev | bpchar | 1 |  | √ | ' ' |  |
| 11 | fratetypeid | 默认汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 12 | fenablesumreportctrl | fenablesumreportctrl | bpchar | 1 |  | √ | ' ' |  |
| 13 | fenableperiodsumreportctr | fenableperiodsumreportctr | bpchar | 1 |  | √ | ' ' |  |
| 14 | fnotcompletedbutcanchange | fnotcompletedbutcanchange | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_systemparam |  | fbudgetctrl |
| 2 | pk_xkbm_systemparam |  | fid |
