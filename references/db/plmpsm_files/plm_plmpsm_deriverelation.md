# 派生关系-plm_plmpsm_deriverelation

## 派生关系-主表 t_plmpsm_derive_relation

- **表名称：** 派生关系-主表
- **表名：** t_plmpsm_derive_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmaterialsourceid | 物料源 | int8 | 64 |  | √ | 0 | 物料源 |
| 4 | fbomsourceid | BOM源 | int8 | 64 |  | √ | 0 | BOM源 |
| 5 | fmastersourceid | 主源业务 | int8 | 64 |  | √ | 0 | 主源业务 |
| 6 | fmaterialtargetid | 目标物料 | int8 | 64 |  | √ | 0 | 目标物料 |
| 7 | fmastertargetid | 目标主业务 | int8 | 64 |  | √ | 0 | 目标主业务 |
| 8 | fbomtargetid | 目标BOM | int8 | 64 |  | √ | 0 | 目标BOM |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmpsm_derive_relation |  | fmaterialsourceid |
| 2 | pk_t_plmpsm_derive_relation |  | fid |
