# 资产负债表公式编辑-gl_balancesheetexpression

## 单据体-子表 t_gl_balancesheetexpentry

- **表名称：** 单据体-子表
- **表名：** t_gl_balancesheetexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsign | 运算符号 | varchar | 1 |  | √ | ' ' | 运算符号,枚举: + :+ - :- |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | frptitemid | 报表项目 | int8 | 64 |  | √ | 0 | [报表项目 gl_manage_rptitem](../gl_files/gl_manage_rptitem.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 7 | ffetchrule | 取数规则 | varchar | 2 |  | √ | ' ' | 取数规则,枚举: 1 :期初余额 2 :期末余额 7 :年初余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_balancesheetexpentry |  | fid |
| 2 | t_gl_balancesheetexpentry_pkey |  | fentryid |

---

## 资产负债表公式编辑-主表 t_gl_balancesheetexpmain

- **表名称：** 资产负债表公式编辑-主表
- **表名：** t_gl_balancesheetexpmain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 3 | fistotalrow | 合计行 | bpchar | 1 |  | √ | '0' | 合计行 |
| 4 | forgviewid | 统计视图 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 5 | forgid | 核算组织ID | int8 | 64 |  | √ | 0 | 核算组织ID |
| 6 | forwid | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 7 | fcolumnkey | 列号 | varchar | 50 |  | √ | ' ' | 列号 |
| 8 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 9 | frowtag | 行标识 | varchar | 50 |  | √ | ' ' | 行标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_balancesheetexpmain_pkey |  | fid |
| 2 | idx_gl_balancesheetexpmain |  | forgid,forwid |
