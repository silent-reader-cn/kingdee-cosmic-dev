# 隐私协议-bos_privacy_policy

## 隐私协议-主表 t_bas_privacy_policy

- **表名称：** 隐私协议-主表
- **表名：** t_bas_privacy_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 发布状态 | bpchar | 1 |  | √ | '0' | 发布状态 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :用户使用协议 2 :隐私政策 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcountryid | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 10 | flocaleid | 语种 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 11 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 12 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_privacy_policy |  | fid |
| 2 | inx_t_bas_privacy_policy |  | ftype |
