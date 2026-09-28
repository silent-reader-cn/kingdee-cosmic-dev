# 税务管控视图-tctb_org_view

## 税务管控视图-主表 t_bastax_org_view

- **表名称：** 税务管控视图-主表
- **表名：** t_bastax_org_view

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 实体方案名称 | varchar | 50 |  | √ | ' ' | 实体方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 7 | fnumber | 实体方案编码 | varchar | 30 |  | √ | ' ' | 实体方案编码 |
| 8 | fisdefault | fisdefault | bpchar | 1 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_org_view |  | fid |
| 2 | idx_idx_bastax_org_view |  | fnumber |

---

## 单据体-子表 t_tctb_org_view_detail

- **表名称：** 单据体-子表
- **表名：** t_tctb_org_view_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 3 | fparentid | 上级组织 | varchar | 100 |  | √ | ' ' | 上级组织 |
| 4 | flongnumber | 长编码 | varchar | 600 |  | √ | ' ' | 长编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | forg | 基础资料 | int8 | 64 |  | √ | 0 | [税务组织实体 tctb_org_entity](../tctb_files/tctb_org_entity.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_org_view_detail_pkey |  | fentryid |
| 2 | idx_tctb_org_view_detail_fk |  | fid |
