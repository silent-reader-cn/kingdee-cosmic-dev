# 用户隐私记录-bos_user_privacy_record

## 用户隐私记录-主表 t_bas_privacy_user_record

- **表名称：** 用户隐私记录-主表
- **表名：** t_bas_privacy_user_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fclienttype | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | flocaleid | 语言 | varchar | 50 |  | √ | ' ' | 语言 |
| 6 | fopflag | 操作描述 | varchar | 50 |  | √ | ' ' | 操作描述 |
| 7 | fsynstatus | 同步状态 | bpchar | 1 |  | √ | '0' | 同步状态,枚举: 1 :已同步 0 :未同步 |
| 8 | fprivacypolicyid | 隐私协议 | int8 | 64 |  | √ | 0 | [隐私协议 bos_privacy_policy](../portal_files/bos_privacy_policy.md) |
| 9 | fcountry | 国家 | varchar | 50 |  | √ | ' ' | 国家 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_privacy_user_record |  | fuserid,fprivacypolicyid |
| 2 | pk_t_bas_privacy_user_record |  | fid |
