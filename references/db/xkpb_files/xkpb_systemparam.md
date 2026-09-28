# 项目预算系统参数-xkpb_systemparam

## 项目预算系统参数-主表 t_xkbm_systemparam

- **表名称：** 项目预算系统参数-主表
- **表名：** t_xkbm_systemparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fbudgetdimensiongroup | fbudgetdimensiongroup | bpchar | 1 |  | √ | ' ' |  |
| 4 | fuploadaspdf | fuploadaspdf | bpchar | 1 |  | √ | ' ' |  |
| 5 | fenableperiodsumactreport | fenableperiodsumactreport | bpchar | 1 |  | √ | '0' |  |
| 6 | fiseditsubmitreport | fiseditsubmitreport | bpchar | 1 |  | √ | ' ' |  |
| 7 | fenableexcuteunopmaindim | fenableexcuteunopmaindim | bpchar | 1 |  | √ | '0' |  |
| 8 | fmaxversioncount | fmaxversioncount | int4 | 32 |  | √ | 0 |  |
| 9 | fovertip | 超额编制提示 | bpchar | 1 |  | √ | ' ' | 超额编制提示 |
| 10 | fuploadasexcel | fuploadasexcel | bpchar | 1 |  | √ | ' ' |  |
| 11 | fuploadasexcellist | fuploadasexcellist | bpchar | 1 |  | √ | ' ' |  |
| 12 | fbudgetallownegative | fbudgetallownegative | bpchar | 1 |  | √ | ' ' |  |
| 13 | fenableexcuteopmaindim | fenableexcuteopmaindim | bpchar | 1 |  | √ | '1' |  |
| 14 | fbudgetctrl | 启用预算控制 | bpchar | 1 |  | √ | ' ' | 启用预算控制 |
| 15 | fuploadasexceldev | fuploadasexceldev | bpchar | 1 |  | √ | ' ' |  |
| 16 | fratetypeid | 默认汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 17 | funweaverptforbidsubmit | funweaverptforbidsubmit | bpchar | 1 |  | √ | '1' |  |
| 18 | fhistorydept | 启用历史部门数据 | bpchar | 1 |  | √ | '0' | 启用历史部门数据 |
| 19 | fenablesumreportctrl | fenablesumreportctrl | bpchar | 1 |  | √ | ' ' |  |
| 20 | fenableperiodsumreportctr | fenableperiodsumreportctr | bpchar | 1 |  | √ | ' ' |  |
| 21 | fnotcompletedbutcanchange | fnotcompletedbutcanchange | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_systemparam |  | fbudgetctrl |
| 2 | pk_xkbm_systemparam |  | fid |
