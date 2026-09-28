# 消息验权配置-wf_verification

## 消息验权配置-主表 t_wf_verification

- **表名称：** 消息验权配置-主表
- **表名：** t_wf_verification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnumber | 验权应用 | varchar | 50 |  | √ | ' ' | 验权应用,枚举: |
| 3 | fformnumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 4 | fformid | 表单对象 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_verification |  | fid |
| 2 | idx_wf_verification_number |  | fformnumber |
