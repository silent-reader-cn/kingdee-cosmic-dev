# 分摊指导通知用户-pca_allocguide_knowuser

## 分摊指导通知用户-主表 t_pca_allocguide_knowuser

- **表名称：** 分摊指导通知用户-主表
- **表名：** t_pca_allocguide_knowuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fisknow | 是否已知 | bpchar | 1 |  | √ | '0' | 是否已知 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pca_allocguide_knowuser |  | fid |
| 2 | idx_pca_allocguide_knowuser_fuserid |  | fuserid |
