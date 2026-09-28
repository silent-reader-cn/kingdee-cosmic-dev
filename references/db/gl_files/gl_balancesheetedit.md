# 资产负债表编辑-gl_balancesheetedit

## 资产负债表编辑-主表 t_gl_balancesheet

- **表名称：** 资产负债表编辑-主表
- **表名：** t_gl_balancesheet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 3 | forgviewid | 统计视图 | int8 | 64 |  | √ | 0 | 新增视图 bd_accountingsysviewsch |
| 4 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_balancesheet |  | faccountorgid |
| 2 | t_gl_balancesheet_pkey |  | fid |

---

## 资产-子表 t_gl_balancesheetassentry

- **表名称：** 资产-子表
- **表名：** t_gl_balancesheetassentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetid | 资产 | int8 | 64 |  | √ | 0 | 报表项目 gl_manage_rptitem |
| 3 | frowid | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_balancesheetassentry |  | fentryid |
| 2 | idx_gl_balancesheetassentry |  | fid |

---

## 负债-子表 t_gl_balancesheeteqentry

- **表名称：** 负债-子表
- **表名：** t_gl_balancesheeteqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fequityid | 负债及所有者权益 | int8 | 64 |  | √ | 0 | 报表项目 gl_manage_rptitem |
| 3 | frowid | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_balancesheeteqentry |  | fentryid |
| 2 | idx_gl_balancesheeteqentry |  | fid |
