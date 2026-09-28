# 合规方案检查项F7-pds_conformitemf7

## 合规方案检查项F7-主表 t_src_conformentry

- **表名称：** 合规方案检查项F7-主表
- **表名：** t_src_conformentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 合规管控方案 | int8 | 64 |  | √ | 0 | [合规管控方案 src_conformscheme](../pds_files/src_conformscheme.md) |
| 2 | fcompobjid | fcompobjid | int8 | 64 |  | √ | 0 |  |
| 3 | fcontroltype | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 0 :不控制 1 :提醒 2 :禁止 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 6 | fdescription | 检查内容描述 | varchar | 255 |  | √ | ' ' | 检查内容描述 |
| 7 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 8 | flogtype | 日志记录方式 | bpchar | 1 |  | √ | ' ' | 日志记录方式,枚举: 1 :记录异常明细 2 :记录所有明细 3 :不记录明细 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpluginname | 插件 | varchar | 100 |  | √ | ' ' | 插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_conformentry |  | fentryid |
| 2 | idx_src_conformentry_fid |  | fid |
