# 异常日志-ipop_errloginfo

## 异常日志-主表 t_ipop_errloginfo

- **表名称：** 异常日志-主表
- **表名：** t_ipop_errloginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 3 | flogkey | 日志标识 | varchar | 50 |  | √ | ' ' | 日志标识 |
| 4 | fsync | 是否同步 | varchar | 1 |  | √ | '0' | 是否同步 |
| 5 | ferrtitle | 异常标题 | varchar | 50 |  | √ | ' ' | 异常标题 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ferrdetail_tag | 异常详情_详情 | text | 0 |  |  | null | 异常详情_详情 |
| 8 | ferrdetail | 异常详情 | varchar | 255 |  | √ | ' ' | 异常详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_errloginfo |  | fid |
| 2 | idx_ipop_errloginfo_logkey |  | flogkey |
