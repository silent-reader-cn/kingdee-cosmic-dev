# 集成服务商管理-ccas_integratedmanage

## 集成服务商管理-主表 t_ccas_integratedmanage

- **表名称：** 集成服务商管理-主表
- **表名：** t_ccas_integratedmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finstalldate | 补丁包安装时间 | timestamp | 0 |  |  | null | 补丁包安装时间 |
| 3 | fsupplier | 服务商 | bpchar | 1 |  | √ | '0' | 服务商 |
| 4 | fsocialcreditcode | 统一社会信用代码 | varchar | 256 |  | √ | ' ' | 统一社会信用代码 |
| 5 | fintegratedtype | 集成服务类型 | varchar | 256 |  | √ | ' ' | 集成服务类型 |
| 6 | fifalreadyinstall | 是否已安装补丁包 | bpchar | 1 |  | √ | '0' | 是否已安装补丁包 |
| 7 | fsuppliername | 服务商名称 | varchar | 256 |  | √ | ' ' | 服务商名称 |
| 8 | fisinstallpack | 是否需安装补丁包 | bpchar | 1 |  | √ | '0' | 是否需安装补丁包 |
| 9 | fintegratedserviceid | 集成服务标识 | varchar | 256 |  | √ | ' ' | 集成服务标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_integratedmanage_id |  | fintegratedserviceid |
| 2 | pk_t_ccas_integratedmanage |  | fid |
