# 组件页面配置分录-pds_compconfig_entry

## 组件页面配置分录-主表 t_pds_compconfigentry

- **表名称：** 组件页面配置分录-主表
- **表名：** t_pds_compconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 组件页面配置 | int8 | 64 |  | √ | 0 | [组件页面配置 pds_compconfig](../pds_files/pds_compconfig.md) |
| 2 | fdisplayname | 显示的名称 | varchar | 50 |  | √ | ' ' | 显示的名称 |
| 3 | ffieldname | 字段名称 | varchar | 300 |  | √ | ' ' | 字段名称 |
| 4 | fismustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fiseditable | 是否可编辑 | bpchar | 1 |  | √ | '0' | 是否可编辑 |
| 7 | ffieldid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 8 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |
| 9 | fiswriteback | 是否可回写 | bpchar | 1 |  | √ | '0' | 是否可回写 |
| 10 | fisexport | 是否可引出 | bpchar | 1 |  | √ | '0' | 是否可引出 |
| 11 | fisclearup | 需要清空 | bpchar | 1 |  | √ | '0' | 需要清空 |
| 12 | fisimport | 是否可引入 | bpchar | 1 |  | √ | '0' | 是否可引入 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_compconfigentry |  | fentryid |
| 2 | idx_pds_compconfigentry_fid |  | fid |
