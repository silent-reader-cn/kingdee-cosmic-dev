# 企业信息收藏-mai_favoriteiac

## 企业信息收藏-主表 t_mai_favoriteiac

- **表名称：** 企业信息收藏-主表
- **表名：** t_mai_favoriteiac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffavordate | 收藏日期 | timestamp | 0 |  |  | null | 收藏日期 |
| 3 | fcompanyname | 企业名称 | varchar | 100 |  | √ | ' ' | 企业名称 |
| 4 | fuser | 收藏用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcompanyid | 企业编码 | varchar | 100 |  | √ | ' ' | 企业编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mai_favoriteiac |  | fid |
| 2 | idx_mai_favoriteiac_fcid_fuser |  | fcompanyid,fuser |
