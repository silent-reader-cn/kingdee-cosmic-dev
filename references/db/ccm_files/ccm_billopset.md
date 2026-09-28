# 单据支持信用的操作设置-ccm_billopset

## 单据支持信用的操作设置-主表 t_ccm_billops

- **表名称：** 单据支持信用的操作设置-主表
- **表名：** t_ccm_billops

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptype | 更新类型 | varchar | 30 |  | √ | ' ' | 更新类型,枚举: update :更新 close :关闭 |
| 3 | fentitykey | 信用单据 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 4 | fops | 支持的操作 | varchar | 512 |  | √ | ' ' | 支持的操作,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_billops |  | fentitykey,foptype |
| 2 | pk_ccm_billops |  | fid |
