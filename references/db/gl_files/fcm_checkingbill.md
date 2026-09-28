# 结账检查对象-fcm_checkingbill

## 结账检查对象-主表 t_fcm_checkingbill

- **表名称：** 结账检查对象-主表
- **表名：** t_fcm_checkingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 3 | fname | 结账检查对象 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | forgpropvalue | 组织规则 | varchar | 50 |  | √ | ' ' | 组织规则,枚举: |
| 5 | fperiodpropvalue | 期间规则 | varchar | 50 |  | √ | ' ' | 期间规则,枚举: |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | flastupdatetime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fbillname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcm_checkingbill |  | fbillnumber |
| 2 | pk_t_fcm_checkingbill |  | fid |
