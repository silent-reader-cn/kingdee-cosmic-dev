# 运行时应用-bos_devportal_appruntime

## 运行时应用-主表 t_meta_appruntime

- **表名称：** 运行时应用-主表
- **表名：** t_meta_appruntime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fhomeid | fhomeid | varchar | 36 |  | √ | ' ' |  |
| 3 | fvisible | fvisible | varchar | 5 |  | √ | '1' |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 254 |  |
| 5 | fdeploystatus | fdeploystatus | varchar | 5 |  | √ | '2' |  |
| 6 | forgfunc | forgfunc | varchar | 5 |  | √ | ' ' |  |
| 7 | fappid | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | falluserapp | falluserapp | bpchar | 1 |  | √ | '0' |  |
| 9 | fcloudnum | fcloudnum | varchar | 50 |  | √ | ' ' |  |
| 10 | fopentype | fopentype | varchar | 5 |  | √ | ' ' |  |
| 11 | fcloudid | 云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 12 | fhomenum | fhomenum | varchar | 36 |  | √ | ' ' |  |
| 13 | fdbroute | fdbroute | varchar | 36 |  | √ | ' ' |  |
| 14 | fusertype | fusertype | varchar | 100 |  | √ | ' ' |  |
| 15 | ftimestamp | ftimestamp | timestamp | 0 |  |  | null |  |
| 16 | fdata | fdata | text | 0 |  |  | null |  |
| 17 | fimage | fimage | varchar | 500 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fappid | fappid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_appruntime_alluserapp |  | falluserapp |
| 2 | t_meta_appruntime_pkey |  | fappid |
| 3 | idx_kdp_appruntime_id |  | fid |
| 4 | idx_kdp_appruntime_cloudid |  | fcloudid |
| 5 | idx_kdp_appruntime_cloudnum |  | fcloudnum |

---

## 运行时应用-多语言表 t_meta_appruntime_l

- **表名称：** 运行时应用-多语言表
- **表名：** t_meta_appruntime_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 2 | fhomename | fhomename | varchar | 200 |  |  | null |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 500 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_appruntime_l_pkey |  | fpkid |
| 2 | idx_kdp_appruntimel_item |  | fappid,flocaleid |
