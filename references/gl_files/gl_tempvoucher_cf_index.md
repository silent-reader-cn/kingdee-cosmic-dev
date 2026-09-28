# 暂存凭证现金流量索引-gl_tempvoucher_cf_index

## 暂存凭证现金流量索引-主表 t_gl_tempvoucher_cf_index

- **表名称：** 暂存凭证现金流量索引-主表
- **表名：** t_gl_tempvoucher_cf_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcashflowitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 |
| 3 | fvoucherid | 凭证 | int8 | 64 |  | √ | 0 | 凭证 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_tempvoucher_cf_index |  | fid |
| 2 | idx_gl_tempvchcf_cforg |  | fcashflowitemid,forgid |
| 3 | idx_gl_tempvchcf_vch |  | fvoucherid |
