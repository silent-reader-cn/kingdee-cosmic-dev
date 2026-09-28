# 集成云灰度特性-isc_gray_feature

## 集成云灰度特性-主表 t_isc_gray_feature

- **表名称：** 集成云灰度特性-主表
- **表名：** t_isc_gray_feature

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant | 租户标识 | varchar | 50 |  | √ | ' ' | 租户标识 |
| 3 | fcreated_time | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 4 | fenv_sign | 环境特征码 | varchar | 50 |  | √ | ' ' | 环境特征码 |
| 5 | fcreator_id | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: S :有效 X :许可过期 X1 :许可非法 X2 :账套不符 X3 :特征码不符 |
| 7 | flicense_content | 许可密钥 | varchar | 2000 |  | √ | ' ' | 许可密钥 |
| 8 | fnumber | 特性编码 | varchar | 50 |  | √ | ' ' | 特性编码 |
| 9 | faccount | 账套标识 | varchar | 50 |  | √ | ' ' | 账套标识 |
| 10 | fexpired_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_gray_feature_number |  | fnumber |
| 2 | pk_t_isc_gray_feature |  | fid |
