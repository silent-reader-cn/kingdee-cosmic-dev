# 高新分摊比例左树-rdem_fzz_gx_ftbltree

## 单据体-子表 t_rdem_gxbltree_entry

- **表名称：** 单据体-子表
- **表名：** t_rdem_gxbltree_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsharetypeid | 分摊类型 | int8 | 64 |  | √ | 0 | [分摊类型 rdem_share_type](../rdem_files/rdem_share_type.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_gxbltree_entry |  | fentryid |
| 2 | idx_rdem_gxbltree_entry_fk |  | fid |

---

## 高新分摊比例左树-主表 t_rdem_fzz_gx_ftbltree

- **表名称：** 高新分摊比例左树-主表
- **表名：** t_rdem_fzz_gx_ftbltree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | fgroupdime | 分组维度 | varchar | 50 |  | √ | ' ' | 分组维度,枚举: taxorg :税务组织 costcenter :成本中心 staffnumber :人员工号 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzz_gx_ftbltree_m0 |  | fenddate |
| 2 | pk_rdem_fzz_gx_ftbltree |  | fid |
