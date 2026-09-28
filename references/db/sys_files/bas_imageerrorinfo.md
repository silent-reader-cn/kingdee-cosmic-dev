# 影像错误记录-bas_imageerrorinfo

## 影像错误记录-主表 t_bas_imageerrorinfo

- **表名称：** 影像错误记录-主表
- **表名：** t_bas_imageerrorinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ferrorinfo | 错误信息 | varchar | 1000 |  | √ | ' ' | 错误信息 |
| 4 | fimagenumber | 影像编码 | varchar | 100 |  | √ | ' ' | 影像编码 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fbillid | 单据id | varchar | 100 |  | √ | ' ' | 单据id |
| 7 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 8 | foperation | 操作 | bpchar | 1 |  | √ | '1' | 操作,枚举: 0 :创建影像 1 :删除 2 :推待办 3 :退扫 4 :取消退扫 5 :影像审核 6 :通知可邮寄 |
| 9 | fimageid | 影像映射id | varchar | 30 |  | √ | ' ' | 影像映射id |
| 10 | fretryok | 补偿成功 | int4 | 32 |  | √ | 0 | 补偿成功 |
| 11 | fretrycount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 12 | fretryresult | 重试结果 | bpchar | 1 |  | √ | '0' | 重试结果,枚举: 0 :失败 1 :成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_imageerrorinfo |  | fid |
| 2 | idx_bas_imageerrorinfo_imgnum |  | fimagenumber |
