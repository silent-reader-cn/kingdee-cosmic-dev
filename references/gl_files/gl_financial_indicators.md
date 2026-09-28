# 财务关键指标-gl_financial_indicators

## 财务关键指标-主表 t_gl_financial_indicators

- **表名称：** 财务关键指标-主表
- **表名：** t_gl_financial_indicators

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 3 | ftype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型 |
| 4 | forgviewid | 统计视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |
| 5 | forgid | 核算组织ID | int8 | 64 |  | √ | 0 | 核算组织ID |
| 6 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_financial_indicators_pkey |  | fid |
| 2 | idx_gl_financial_indicators |  | forgid,fbooktypeid |

---

## 单据体-子表 t_gl_financial_indientry

- **表名称：** 单据体-子表
- **表名：** t_gl_financial_indientry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkpiname | 指标名称 | int8 | 64 |  | √ | 0 | 财务指标 gl_business_analskpi |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcalformula | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_financial_indientry |  | fid |
| 2 | t_gl_financial_indientry_pkey |  | fentryid |
