# 历史条件规则模型-wf_hiconditionalrulemodel

## 历史条件规则模型-主表 t_wf_hiconditionrule

- **表名称：** 历史条件规则模型-主表
- **表名：** t_wf_hiconditionrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人： | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fexpression | 条件表达式： | text | 0 |  |  | null | 条件表达式： |
| 4 | fvalidtime | 生效时间： | timestamp | 0 |  |  | null | 生效时间： |
| 5 | fprocdefid | 流程定义ID： | int8 | 64 |  | √ | 0 | 流程定义ID： |
| 6 | fdescription | 规则描述： | varchar | 500 |  | √ | ' ' | 规则描述： |
| 7 | fshowtext | 显示文字： | varchar | 184 |  | √ | ' ' | 显示文字： |
| 8 | fcreatedate | 创建时间： | timestamp | 0 |  |  | null | 创建时间： |
| 9 | fconditionalruleid | 条件规则ID： | int8 | 64 |  | √ | 0 | 条件规则ID： |
| 10 | fmodifydate | 修改时间： | timestamp | 0 |  |  | null | 修改时间： |
| 11 | finvalidtime | 失效时间： | timestamp | 0 |  |  | null | 失效时间： |
| 12 | fplugin | 插件： | text | 0 |  |  | null | 插件： |
| 13 | fversion | 版本： | varchar | 36 |  | √ | ' ' | 版本： |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiconditionrule_pdef |  | fprocdefid |
| 2 | t_wf_hiconditionrule_pkey |  | fid |

---

## 历史条件规则模型-多语言表 t_wf_hiconditionrule_l

- **表名称：** 历史条件规则模型-多语言表
- **表名：** t_wf_hiconditionrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshowtext | 显示文字： | varchar | 184 |  | √ | ' ' | 显示文字： |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 规则描述： | varchar | 500 |  | √ | ' ' | 规则描述： |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hiconditionrule_l_pkey |  | fpkid |
| 2 | idx_wf_hiconditionrule_loc |  | fid,flocaleid |
