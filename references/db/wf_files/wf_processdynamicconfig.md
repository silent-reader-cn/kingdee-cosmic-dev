# 流程动态方案配置-wf_processdynamicconfig

## 流程动态方案配置-主表 t_wf_dynconfscheme

- **表名称：** 流程动态方案配置-主表
- **表名：** t_wf_dynconfscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 3 | fname | 方案名称 | varchar | 500 |  | √ | ' ' | 方案名称 |
| 4 | fprocdefid | 流程定义id | int8 | 64 |  | √ | 0 | 流程定义id |
| 5 | fgraphxml | XML资源ID | int8 | 64 |  | √ | 0 | XML资源ID |
| 6 | fparentscheme | 扩展的方案id | int8 | 64 |  | √ | 0 | 扩展的方案id |
| 7 | fdescription | 方案描述 | varchar | 500 |  | √ | ' ' | 方案描述 |
| 8 | fbpmnjson | JSON资源ID | int8 | 64 |  | √ | 0 | JSON资源ID |
| 9 | fdefault | 是否是默认方案 | bpchar | 1 |  | √ | '0' | 是否是默认方案 |
| 10 | fstate | 方案启用状态 | varchar | 30 |  | √ | ' ' | 方案启用状态,枚举: 1 :启用 0 :禁用 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fconditionexpression | 应用条件表达式 | text | 0 |  |  | null | 应用条件表达式 |
| 15 | fsourcekey | 源方案编码 | varchar | 255 |  | √ | ' ' | 源方案编码 |
| 16 | fconditionid | 应用条件 | int8 | 64 |  | √ | 0 | 应用条件 |
| 17 | fnumber | 方案编码 | varchar | 255 |  | √ | ' ' | 方案编码 |
| 18 | fjsonpatch | JSON差量ID | int8 | 64 |  | √ | 0 | JSON差量ID |
| 19 | fconditiontext | 条件规则显示文字 | varchar | 184 |  | √ | ' ' | 条件规则显示文字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_dynconfscheme |  | fprocdefid |
| 2 | t_wf_dynconfscheme_pkey |  | fid |

---

## 流程动态方案配置-多语言表 t_wf_dynconfscheme_l

- **表名称：** 流程动态方案配置-多语言表
- **表名：** t_wf_dynconfscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 500 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 方案描述 | varchar | 500 |  | √ | ' ' | 方案描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fconditiontext | 条件规则显示文字 | varchar | 184 |  | √ | ' ' | 条件规则显示文字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_dynamicconfscheme_l |  | fid,flocaleid |
| 2 | t_wf_dynconfscheme_l_pkey |  | fpkid |
