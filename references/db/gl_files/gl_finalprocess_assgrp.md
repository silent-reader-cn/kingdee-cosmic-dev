# 核算维度取值-gl_finalprocess_assgrp

## 核算维度取值-主表 t_gl_amortassgrp

- **表名称：** 核算维度取值-主表
- **表名：** t_gl_amortassgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassgrprow | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 3 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_amortassgrp_pkey |  | fid |
| 2 | idx_gl_aortassgrp_org_rowid |  | forgid,fassgrprow |

---

## 值-多选基础资料表 t_gl_amortmulassgrp

- **表名称：** 值-多选基础资料表
- **表名：** t_gl_amortmulassgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 科目影响因素（旧） ai_vchentrytype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_amortmulassgrp |  | fentryid |
| 2 | pk_t_gl_amortmulassgrp |  | fpkid |

---

## 单据体-子表 t_gl_amortassgrpentry

- **表名称：** 单据体-子表
- **表名：** t_gl_amortassgrpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaluesstr | 核算项目值集合 | varchar | 2000 |  |  | null | 核算项目值集合 |
| 3 | ftxtval | 手工维度值 | varchar | 2000 |  |  | ' ' | 手工维度值 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ffieldnameid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_amortassgrpentry |  | fid |
| 2 | t_gl_amortassgrpentry_pkey |  | fentryid |
