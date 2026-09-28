# 往来通知单勾稽日志-gl_acnotice_checklog

## 往来通知单勾稽日志-主表 t_gl_acnotice_checklog

- **表名称：** 往来通知单勾稽日志-主表
- **表名：** t_gl_acnotice_checklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | fvoucherid | int8 | 64 |  | √ | 0 | fvoucherid |
| 3 | fopentryid | fopentryid | int8 | 64 |  | √ | 0 | fopentryid |
| 4 | floccheck | floccheck | bpchar | 1 |  | √ | '0' | floccheck |
| 5 | fisupdate | fisupdate | bpchar | 1 |  | √ | '0' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | fentryid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_acnotice_checklog |  | fid |
| 2 | idx_gl_acnotice_checklog |  | fvoucherid,fentryid,fopentryid |
