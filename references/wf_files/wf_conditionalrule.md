# 条件规则-wf_conditionalrule

## 条件规则-多语言表 t_wf_conditionrule_l

- **表名称：** 条件规则-多语言表
- **表名：** t_wf_conditionrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshowtext | 显示文字： | varchar | 184 |  | √ | ' ' | 显示文字： |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 条件描述： | varchar | 500 |  | √ | ' ' | 条件描述： |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_conditionrule_l_pkey |  | fpkid |
| 2 | idx_wf_conditionrule_localeid |  | fid,flocaleid |

---

## 条件规则-主表 t_wf_conditionrule

- **表名称：** 条件规则-主表
- **表名：** t_wf_conditionrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fexpression |  | text | 0 |  |  | null |  |
| 4 | fvalidtime | 生效时间： | timestamp | 0 |  |  | null | 生效时间： |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | fproperty | 属性 | varchar | 255 |  |  | null | 属性 |
| 7 | felementid | 节点ID： | varchar | 255 |  | √ | ' ' | 节点ID： |
| 8 | fdescription | 条件描述： | varchar | 500 |  | √ | ' ' | 条件描述： |
| 9 | fshowtext | 显示文字： | varchar | 184 |  | √ | ' ' | 显示文字： |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftype | 类型： | varchar | 30 |  | √ | ' ' | 类型：,枚举: sequenceFlow :连线条件 autoApproval :自动审批条件 participant :参与人条件 processStartUp :流程启动条件 skip :跳过条件 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fplugin | 业务插件： | text | 0 |  |  | null | 业务插件： |
| 15 | fversion | 版本 | varchar | 36 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_conditionrule_pkey |  | fid |
| 2 | idx_wf_conditionrule_pedf |  | fprocdefid |
| 3 | idx_wf_conditionrule_type |  | ftype |

---

## 单据体-子表 t_wf_conditiondetail

- **表名称：** 单据体-子表
- **表名：** t_wf_conditiondetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket | 左括号 | varchar | 10 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( ((( :((( |
| 3 | fvalue | 值 | text | 0 |  |  | null | 值 |
| 4 | frightbracket | 右括号 | varchar | 10 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) ))) :))) |
| 5 | fparamnumber | 参数编码 | varchar | 500 |  | √ | ' ' | 参数编码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentitynumber | 被选中的实体名称 | varchar | 255 |  | √ | ' ' | 被选中的实体名称 |
| 8 | fvaluetype | 值类型 | varchar | 100 |  | √ | ' ' | 值类型 |
| 9 | foperation | 操作符 | varchar | 30 |  | √ | ' ' | 操作符 |
| 10 | flogic | 逻辑符 | varchar | 30 |  | √ | ' ' | 逻辑符,枚举: && :并且 || :或者 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_conditiondetail_id |  | fid |
| 2 | t_wf_conditiondetail_pkey |  | fentryid |
