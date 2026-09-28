# 组织分隔符配置-bos_org_config

## 组织分隔符配置-主表 t_org_config

- **表名称：** 组织分隔符配置-主表
- **表名：** t_org_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffullnamesep | 长名称分隔符 | varchar | 30 |  | √ | '_' | 长名称分隔符,枚举: _ :_ - :- . :. \| :\| \|\| :\|\| / :/ // :// |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_config |  | ffullnamesep |
| 2 | pk_t_org_config |  | fid |
