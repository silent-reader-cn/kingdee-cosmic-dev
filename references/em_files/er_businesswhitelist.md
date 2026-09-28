# 商旅免审白名单-er_businesswhitelist

## 商旅免审白名单-主表 t_er_busiwhitelist

- **表名称：** 商旅免审白名单-主表
- **表名：** t_er_busiwhitelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 白名单人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fenble | 是否生效 | bpchar | 1 |  | √ | '0' | 是否生效 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_busilist |  | fuserid,fenble |
| 2 | t_er_busiwhitelist_pkey |  | fid |
