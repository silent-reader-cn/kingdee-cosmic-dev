# 质检方案管理-task_proadminister

## 抽选组织-多选基础资料表 t_tk_selectedorg

- **表名称：** 抽选组织-多选基础资料表
- **表名：** t_tk_selectedorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 共享中心组织分配 task_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_selectedorg_pkey |  | fpkid |
| 2 | index_ssc_selectedorg |  | fid |

---

## 条件单据体-子表 t_tk_selectedfilter

- **表名称：** 条件单据体-子表
- **表名：** t_tk_selectedfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fflogic | 逻辑 | varchar | 30 |  | √ | ' ' | 逻辑,枚举: 0 :AND 1 :OR |
| 3 | fffieldname | 字段 | varchar | 100 |  | √ | ' ' | 字段 |
| 4 | fmark | fmark | varchar | 100 |  | √ | ' ' |  |
| 5 | ffieldname | ffieldname | varchar | 100 |  | √ | ' ' |  |
| 6 | ffvalue | ffvalue | varchar | 100 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ffleft | ( | varchar | 30 |  | √ | ' ' | (,枚举: : ( :( (( :(( ((( :((( |
| 9 | ffcomparedesc | 比较符 | varchar | 30 |  | √ | ' ' | 比较符 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffright | ) | varchar | 30 |  | √ | ' ' | ),枚举: : ) :) )) :)) ))) :))) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_selectedfilter_pkey |  | fentryid |
| 2 | index_ssc_selectedfilter |  | fid |

---

## 条件单据体-多语言表 t_tk_selectedfilter_l

- **表名称：** 条件单据体-多语言表
- **表名：** t_tk_selectedfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffvalue | 比较值 | varchar | 100 |  | √ | ' ' | 比较值 |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_selectedfilter_l |  | flocaleid |
| 2 | t_tk_selectedfilter_l_pkey |  | fpkid |

---

## 质检方案管理-多语言表 t_tk_proadminister_l

- **表名称：** 质检方案管理-多语言表
- **表名：** t_tk_proadminister_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 质检方案管理-主表 t_tk_proadminister

- **表名称：** 质检方案管理-主表
- **表名：** t_tk_proadminister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
