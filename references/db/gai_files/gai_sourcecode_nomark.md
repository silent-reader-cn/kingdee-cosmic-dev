# 无来源标识记录-gai_sourcecode_nomark

## 无来源标识记录-主表 t_gai_sourcecode_nomark

- **表名称：** 无来源标识记录-主表
- **表名：** t_gai_sourcecode_nomark

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcodestr | 标识字符串 | varchar | 100 |  | √ | ' ' | 标识字符串 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 4 | fstacktrace | 堆栈记录 | varchar | 255 |  | √ | ' ' | 堆栈记录 |
| 5 | fstacktrace_tag | 堆栈记录_详情 | text | 0 |  |  | null | 堆栈记录_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_sourcecode_nomark |  | fcodestr |
| 2 | pk_gai_sourcecode_nomark |  | fid |
