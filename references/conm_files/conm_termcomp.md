# 合同条款组件-conm_termcomp

## 单据体-多语言表 t_conm_termcompentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_conm_termcompentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftermcontent | 条款内容 | varchar | 2000 |  |  | ' ' | 条款内容 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | fdescription | varchar | 255 |  |  | ' ' |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_termcompentry_l_pkey |  | fpkid |
| 2 | idx_conm_termcompentry_l |  | fentryid,flocaleid |

---

## 合同条款组件-主表 t_conm_termcomp

- **表名称：** 合同条款组件-主表
- **表名：** t_conm_termcomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplateentryid | 合同模板分录ID | int8 | 64 |  | √ | 0 | 合同模板分录ID |
| 3 | fcontractid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_termcomp_pkey |  | fid |
| 2 | idx_conm_termcomp_contractid |  | fcontractid |

---

## 单据体-子表 t_conm_termcompentry

- **表名称：** 单据体-子表
- **表名：** t_conm_termcompentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | 合同条款分组 conm_termgroup |
| 3 | ftermentrychangetype | ftermentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftermid | 合同条款 | int8 | 64 |  | √ | 0 | 合同条款 conm_term |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_termcompentry |  | fid |
| 2 | t_conm_termcompentry_pkey |  | fentryid |
