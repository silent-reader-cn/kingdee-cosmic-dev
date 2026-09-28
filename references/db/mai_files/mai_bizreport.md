# 经营报告-mai_bizreport

## 经营报告-主表 t_mai_bizreport

- **表名称：** 经营报告-主表
- **表名：** t_mai_bizreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 报告名称 | varchar | 100 |  | √ | ' ' | 报告名称 |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsendtime | 发送日期 | timestamp | 0 |  |  | null | 发送日期 |
| 5 | fdata_tag | 数据_详情 | text | 0 |  |  | ' ' | 数据_详情 |
| 6 | freportcfg | 报告配置 | int8 | 64 |  | √ | 0 | 报告配置 |
| 7 | fdata | 数据 | varchar | 255 |  | √ | ' ' | 数据 |
| 8 | fgenid | 业务编码 | int8 | 64 |  | √ | 0 | 业务编码 |
| 9 | freadstatus | 已读 | bpchar | 1 |  | √ | '0' | 已读,枚举: 0 :未读 1 :已读 |
| 10 | fversion | 版本 | bpchar | 1 |  | √ | ' ' | 版本,枚举: 1 :new |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_bizreport_fgenid_fuser |  | fgenid,fuser |
| 2 | pk_mai_bizreport |  | fid |
