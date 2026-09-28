# 税务报表分配关系表-gl_taxassigntable

## 税务报表分配关系表-主表 t_gl_taxassigntable

- **表名称：** 税务报表分配关系表-主表
- **表名：** t_gl_taxassigntable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 4 | ftype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型 |
| 5 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_taxassigntable_pkey |  | fid |
| 2 | idx_gl_taxassigntable |  | fuseorgid,faccounttableid |
