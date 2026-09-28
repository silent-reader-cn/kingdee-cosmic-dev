# 单据配置-ai_billconfig

## 单据配置-主表 t_ai_billconfig

- **表名称：** 单据配置-主表
- **表名：** t_ai_billconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillentity | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fhasvchfield | 已生成凭证标识 | varchar | 50 |  | √ | ' ' | 已生成凭证标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_billconfig_bill |  | fbillentity |
| 2 | pk_ai_billconfig |  | fid |
