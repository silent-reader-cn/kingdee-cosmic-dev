# 场景管理-plm_rengine_scene

## 场景管理-多语言表 t_plm_egn_scene_l

- **表名称：** 场景管理-多语言表
- **表名：** t_plm_egn_scene_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_scene_l |  | fpkid |
| 2 | idx_plm_scene_l |  | fid,flocaleid |

---

## 输入参数-子表 t_plm_egn_input_entry

- **表名称：** 输入参数-子表
- **表名：** t_plm_egn_input_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finputname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 3 | finputnumber | 参数标识 | varchar | 50 |  | √ | ' ' | 参数标识 |
| 4 | findex | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmultiple | 允许多选 | varchar | 50 |  | √ | ' ' | 允许多选,枚举: 0 : 1 :是 2 :否 |
| 6 | ftreelv | 业务对象属性层级 | int8 | 64 |  | √ | 0 | 业务对象属性层级 |
| 7 | fparamsobject | 业务对象/基础资料 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fpresetisedit | 预置是否已更新 | bpchar | 1 |  | √ | '0' | 预置是否已更新 |
| 9 | fdateformat | 掩码 | varchar | 50 |  | √ | ' ' | 掩码,枚举: yyyy-MM-dd :YYYY-MM-DD yyyy/MM/dd :YYYY/MM/DD yy-MM/dd :YY-MM/DD yyyy-MM :YYYY-MM yyyy/MM :YYYY/MM yyyy :YYYY |
| 10 | fdynprop | 字段 | text | 0 |  |  | ' ' | 字段 |
| 11 | fparamstype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 number :数字 boolean :布尔 dynamicObject :业务对象字段 date :日期 basedata :基础资料 enum :枚举 |
| 12 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcombofield | 下拉项 | text | 0 |  |  | ' ' | 下拉项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_egn_input_entry |  | fentryid |
| 2 | idx_plm_egn_input_entry |  | finputnumber |

---

## 输出参数-多语言表 t_plm_egn_output_entry_l

- **表名称：** 输出参数-多语言表
- **表名：** t_plm_egn_output_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | foutputname | 参数名称 | varchar | 255 |  | √ | ' ' | 参数名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_egn_output_entry_l |  | fpkid |
| 2 | idx_plm_egn_output_entry_l |  | fentryid,flocaleid |

---

## 输出参数-子表 t_plm_egn_output_entry

- **表名称：** 输出参数-子表
- **表名：** t_plm_egn_output_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | findex | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmultiple | 允许多选 | varchar | 50 |  | √ | ' ' | 允许多选,枚举: 0 : 1 :是 2 :否 |
| 4 | foutputname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 5 | fparamsobject | 业务对象/基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fpresetisedit | 预置是否已更新 | bpchar | 1 |  | √ | '0' | 预置是否已更新 |
| 7 | fdateformat | 掩码 | text | 0 |  |  | ' ' | 掩码,枚举: yyyy-MM-dd :YYYY-MM-DD yyyy/MM/dd :YYYY/MM/DD yy-MM/dd :YY-MM/DD yyyy-MM :YYYY-MM yyyy/MM :YYYY/MM yyyy :YYYY |
| 8 | fdynprop | 字段 | text | 0 |  |  | ' ' | 字段 |
| 9 | fparamstype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 number :数字 boolean :布尔 dynamicObject :业务对象字段 date :日期 basedata :基础资料 enum :枚举 |
| 10 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | foutputnumber | 参数标识 | varchar | 50 |  | √ | ' ' | 参数标识 |
| 13 | fcombofield | 下拉项 | text | 0 |  |  | ' ' | 下拉项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_output_entry |  | foutputnumber |
| 2 | pk_t_plm_egn_output_entry |  | fentryid |

---

## 场景管理-主表 t_plm_egn_scene

- **表名称：** 场景管理-主表
- **表名：** t_plm_egn_scene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fbizappid | 所属应用 | varchar | 18 |  | √ | ' ' | 业务应用实体（规则引擎） plm_rengine_bizapp |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fiseditrule | 允许在规则中心编辑规则 | bpchar | 1 |  | √ | '1' | 允许在规则中心编辑规则 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 16 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 17 | fiseditscene | 场景是否允许编辑 | bpchar | 1 |  | √ | '1' | 场景是否允许编辑 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_scene |  | fid |
| 2 | idx_plm_scene_app |  | fbizappid |
| 3 | idx_plm_scene_num |  | fnumber |

---

## 输入参数-多语言表 t_plm_egn_input_entry_l

- **表名称：** 输入参数-多语言表
- **表名：** t_plm_egn_input_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finputname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_egn_input_entry_l |  | fpkid |
| 2 | idx_plm_egn_input_entry_l |  | fentryid,flocaleid |
