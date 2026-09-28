# 用户配置信息-gai_export_userprofile

## 用户配置信息-主表 t_gai_export_userprofile

- **表名称：** 用户配置信息-主表
- **表名：** t_gai_export_userprofile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexporttimes | 下载次数 | int8 | 64 |  | √ | 0 | 下载次数 |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fshowreadme | 显示欢迎信息 | bpchar | 1 |  | √ | '0' | 显示欢迎信息 |
| 5 | flastexporttime | 最近下载时间 | timestamp | 0 |  |  | null | 最近下载时间 |
| 6 | fmodfiyprofiletime | 配置修改时间 | timestamp | 0 |  |  | null | 配置修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_export_userprofile |  | fid |
