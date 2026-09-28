# 职能组织时区-inte_bizorgtimezone

## 职能组织时区-主表 t_int_bizorgtimezone

- **表名称：** 职能组织时区-主表
- **表名：** t_int_bizorgtimezone

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 职能单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftimezoneid | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 4 | fviewid | fviewid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_int_bizorgtimezone_pkey |  | fid |
| 2 | t_int_bizorgtimezone_forgid_key |  | forgid |
