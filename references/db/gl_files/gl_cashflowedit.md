# 现金流量表编辑-gl_cashflowedit

## 现金流量表编辑-主表 t_gl_incomeedit

- **表名称：** 现金流量表编辑-主表
- **表名：** t_gl_incomeedit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 3 | ftype | 表类型 | varchar | 50 |  | √ | ' ' | 表类型 |
| 4 | forgviewid | 统计视图 | int8 | 64 |  | √ | 0 | [新增视图 bd_accountingsysviewsch](../fibd_files/bd_accountingsysviewsch.md) |
| 5 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_incomeedit_pkey |  | fid |
| 2 | idx_gl_incomeedit |  | faccountorgid |

---

## 单据体-子表 t_gl_incomeedit_pro

- **表名称：** 单据体-子表
- **表名：** t_gl_incomeedit_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [报表项目 gl_manage_rptitem](../gl_files/gl_manage_rptitem.md) |
| 3 | findex | 行序号 | int8 | 64 |  | √ | 0 | 行序号 |
| 4 | frowid | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fproject | fproject | varchar | 50 |  | √ | ' ' |  |
| 7 | forwindex | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_incomeedit_pro |  | fid,frowid |
| 2 | t_gl_incomeedit_pro_pkey |  | fentryid |
