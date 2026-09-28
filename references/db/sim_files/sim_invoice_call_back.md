# 回调配置-sim_invoice_call_back

## 回调配置-主表 t_sim_invoice_call_back

- **表名称：** 回调配置-主表
- **表名：** t_sim_invoice_call_back

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmethodname | 方法名称 | varchar | 100 |  | √ | ' ' | 方法名称 |
| 3 | fcloudid | 所属云标识 | varchar | 50 |  | √ | ' ' | 所属云标识 |
| 4 | fsystemsource | 业务系统来源 | varchar | 50 |  | √ | ' ' | 业务系统来源 |
| 5 | fservicename | 服务名称 | varchar | 100 |  | √ | ' ' | 服务名称 |
| 6 | fcallbackmethod | 回调方法 | varchar | 100 |  | √ | ' ' | 回调方法,枚举: BlankItemsCallBackServiceImpl :空单下推，没有明细关系 |
| 7 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_invoice_call_back |  | fsystemsource |
| 2 | pk_t_sim_invoice_call_back |  | fid |
