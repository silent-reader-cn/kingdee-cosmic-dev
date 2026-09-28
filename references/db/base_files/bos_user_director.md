# 组织负责人-bos_user_director

## 组织负责人-主表 t_sec_director

- **表名称：** 组织负责人-主表
- **表名：** t_sec_director

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | fischief | 主负责人 | bpchar | 1 |  | √ | ' ' | 主负责人 |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdirectorid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_director_pkey |  | fid |
| 2 | ix_sec_opruleobj_director |  | fdirectorid |
