# 上一次被使用的分摊标准-pca_alloc_laststd

## 上一次被使用的分摊标准-主表 t_pca_alloc_laststd

- **表名称：** 上一次被使用的分摊标准-主表
- **表名：** t_pca_alloc_laststd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 3 | fstdgroupid | 分摊标准 | int8 | 64 |  | √ | 0 | [自定义分摊标准（组） pca_cusalloc_stdgroup](../pca_files/pca_cusalloc_stdgroup.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_alloc_laststd |  | fid |
| 2 | idx_pca_alloc_laststd_ca |  | fcostaccountid |
