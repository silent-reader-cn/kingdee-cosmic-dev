# 接口日志归档-pbd_apilog_back

## 接口日志归档-主表 t_mal_apilogback

- **表名称：** 接口日志归档-主表
- **表名：** t_mal_apilogback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 3 | fstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: S :成功 F :失败 R :执行中 |
| 4 | fcreatorid | 调用者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 6 | fparams_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 7 | fextsysapi | 接口配置 | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 8 | fend_time | 状态更新/结束时间 | timestamp | 0 |  |  | null | 状态更新/结束时间 |
| 9 | fparams | 参数 | text | 0 |  |  | null | 参数 |
| 10 | fresult | 结果 | text | 0 |  |  | null | 结果 |
| 11 | fsystype | 系统类型 | bpchar | 1 |  | √ | ' ' | 系统类型,枚举: 1 :自建 2 :京东 3 :苏宁 4 :得力 5 :西域 9 :震坤行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_apilogback_fcreatetime |  | fcreatetime |
| 2 | idx_mal_apilogback_fextsysapi |  | fextsysapi |
| 3 | pk_t_mal_apilogback |  | fid |
